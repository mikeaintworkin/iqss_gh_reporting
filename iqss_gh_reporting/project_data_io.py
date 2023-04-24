from datetime import timedelta

# from argparse import ArgumentParser
# from dict2xml import dict2xml
# from argparse import ArgumentParser
from github import Github
# from gql import gql, Client
# from gql.transport.aiohttp import AIOHTTPTransport
# from json2xml import json2xml
from pathvalidate import sanitize_filename
# from typing import Literal
# import argparse
# import asyncio
import datetime
# import json
import os
import pandas as pd
import re
import copy


class RequiredDfColumnHeaderNames:
    # ===================================================================================================================
    # This is used when writing data collected from the API out to a flat file.
    # It's a way (albeit clunky) to that the data gets consistent data headers.
    # .
    # ===================================================================================================================

    # This dictionary should be edited to to be what is expected.
    # prolly in a real app this would be a config file.
    def __init__(self):
        # These are required mappings
        self.names = {
            "project": "Project",
            "column": "Column",
            "type": "Type",
            "number": "Number",
            "labels": "Labels",
            "repo": "Repo",
            "state": "State",
        }
        # These are additional mappings
        # These are headers that are not required as part of the input data we are processing but that
        # we would like to standardize
        self.map = {
            "size": "Size"
        }

    def value(self, name: str = None):
        # return a names or map value
        if name in self.names:
            return str(self.names[name])
        if name in self.map:
            return str(self.map[name])
        return "RequiredDfColumnHeaderNames:NO_VALUE_DEFINED for " + name

    def names(self):
        # col names
        return list(self.names.keys())

    def values(self):
        # col values
        return list(self.names.values())

    def print(self):
        print(f"Column names: {self.names}")


def list_contains_at_least(required_list: list = None, submitted_list: list = None):
    # ===================================================================================================================
    # This takes a required list of strings and a submitted list of strings.
    # It checks to see if the submitted list contains at least the required list.
    #
    # It is used to check that the column names in a dataframe are what is expected.
    # It is used to check that the subset of sprint column values that we use to define what is active in a sprint
    #  are actually present in the sprint column data. e.g. The code compares teh contents of:
    #  RequiredSprintColumnValues with the unique list of values extracted from the sprint column data.
    # ===================================================================================================================
    print(f" required list entries: {required_list}")
    print(f" submitted list entries: {submitted_list}")

    if submitted_list is None:
        print("No entries were submitted.")
        return False
    if len(list(set(submitted_list))) != len(submitted_list):
        print("Duplicate column names found.")
        return False
    missing_names = [col for col in required_list if col not in list(set(submitted_list))]
    if missing_names:
        print(f"Missing entries: {missing_names}")
        return False
    else:
        print("All desired entries are present.")
        return True


def write_dataframe(df: pd.DataFrame = None,
                    out_dir: str = '/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk',
                    out_name: str = 'output'):
    # ===================================================================================================================
    # This writes the contents of a dataframe to a tab delimited file.
    # ===================================================================================================================
    out_file = out_dir + '/' + pd.Timestamp.now().strftime("%Y_%m_%d-%H_%M_%S") + \
               "-" + sanitize_filename(out_name) + ".tsv"
    print(f"Saving result to file.")
    print(f" {out_file}")
    df.to_csv(out_file, sep='\t', index=False)


class RequiredSprintColumnValues:
    # ===================================================================================================================
    # This defines a list of the sprint column values that we include as part of an active sprint.
    # ===================================================================================================================
    # Notes:
    # This list should be edited to to be what is expected.
    # prolly in a real app this would be a config file.

    def __init__(self):
        self.names = [
            "This Sprint 🏃‍♀️ 🏃",
            "IQSS Team - In Progress  💻",
            "Ready for Review ⏩",
            "In Review 🔎"
        ]

    def list(self):
        return self.names

    def print(self):
        print(f"Column values: {self.names}")


class DFFromFile:
    # ===================================================================================================================
    # This reads a previously collected set of sprint data from a file.
    # no validation is done on the file contents.
    # ===================================================================================================================
    def __init__(self, in_dir: str = None, file_name: str = None):
        self.df = None
        print(" Reading in data from a file.")
        print(f" input file directory: {in_dir}, input file name: {file_name}")
        input_file = in_dir + '/' + file_name
        print(f" input_file: {input_file}")

        # there's a library I can use to do this.  I'll do it later.
        if (file_name is None) or (in_dir is None) or (not os.path.isdir(in_dir)):
            print("Attempt to read input from file. No valid initialization data.  Exiting.")
        else:
            self.df = pd.read_csv(input_file, sep='\t')

    def dataframe(self):
        return self.df


class LegacyProjectCards:
    # ===================================================================================================================
    # represents a query of data of all the cards from a legacy GitHub project
    # The query drills down: organization > project > card content (Issue or pr)
    # Initialization is separate from the query.
    # The thought is that maybe objects like this will know about a certain flavor of project and how to query it.
    # This particular query is not going to stay. We're going to move to projectV2 for the sprints.
    # ===================================================================================================================
    #
    #    input: see inti line#
    #         : The out_dir is where any files are written out to
    #   output: The outputfile name is generated based on the project name and the date/time
    #  precond: The query and output are specific to this project configuration
    #         :  These columns must be present
    #         :  ["Project", "Column", "Card", "CardURL", "CardType", "Number", "Labels", "Repo", "State",
    #         :    "CreatedAt", "UpdatedAt", "ClosedAt"]
    #         :  That list will be passed in as a list.
    # postcond:  output will contain the data from the columns described in the precondition
    #    descr:
    #
    #
    # Sample calls:
    # github_project_cards = utils.GithubProjectCardsPandas(
    #     access_token=auth_token_val,
    #     organization_name=args.organization_name,
    #     project_name=args.proj_name,
    #     out_dir=args.out_dir
    # )
    #
    # github_project_cards.get_project_cards()
    # github_project_cards.print_project_cards()
    # github_project_cards.save_project_cards()
    #
    #
    # --------------------------------------------------------------------------------------------------------------------
    # init will return true if it was able to retrieve the data
    def __init__(self, access_token: str, organization_name: str, project_name: str):
        # prereq: out_dir and outputfile are assumed to be valid
        # come back here and do the validation later
        self.date_stamp = pd.Timestamp.now().strftime("%Y_%m_%d-%H_%M_%S")

        # internal init
        self.card_count = 0
        self.rhn = RequiredDfColumnHeaderNames()
        self.project_cards = pd.DataFrame(
            columns=[
                self.rhn.value("project"),
                self.rhn.value("column"),
                "Card",
                "CardURL",
                self.rhn.value("type"),
                self.rhn.value("number"),
                self.rhn.value("labels"),
                self.rhn.value("repo"),
                self.rhn.value("state"),
                "CreatedAt",
                "UpdatedAt",
                "ClosedAt"
                ]
            )
        # external init
        self.client = Github(access_token, per_page=100)
        self.project_name = project_name
        self.organization_name = organization_name
        self.organization_api_object = None

    def fetch_data(self):

        self.organization_api_object = self.client.get_organization(self.organization_name)
        if not self.organization_api_object:
            print(f"Cannot populate organization Objecct")
            return False

        # Find the project we care about
        if not self._fetch_project_api_obj():
            print(f"Cannot populate project we care about")
            return False

        if not self._get_project_cards_api_obj():
            print(f"Cannot populate project cards")
            return False
        return True

    # define the project object from the api call that we care about
    # return true if we are successful
    def _fetch_project_api_obj(self):
        projects = self.organization_api_object.get_projects()
        # find our project
        for p in projects:
            print(f"projects: looking to match {self.project_name} with {p.name}")
            if p.name == self.project_name:
                self.project_object = p
                return True

        print(f"project {self.project_name} not found")
        return False

    # return true if we are successful
    def _get_project_cards_api_obj(self):

        # return the legacy project columns names
        # check to make sure that they contain the critical columns we care about.
        columns = self.project_object.get_columns()
        three_months_ago = datetime.datetime.utcnow() - timedelta(days=90)

        self.card_count = 0
        for column in columns:
            column_name = column.name
            cards = column.get_cards(archived_state='not_archived')
            print(f"start: {self.card_count} cards processed: {self.project_object.name}, Column {column.name}")
            for card in cards:
                self.card_count += 1
                card_content = card.get_content()
                if card_content is not None and card.updated_at >= three_months_ago:
                    regex1 = re.compile(r"(/issues/|/pull/)")
                    regex2 = re.compile(r"(issues|pull)")
                    card_type = regex1.search(card_content.html_url).group(0)
                    card_type = regex2.search(card_type).group(0)
                    if self.card_count % 50 == 0:
                        print(f">>>>>> {self.card_count} # cards {self.project_object.name}: {column.name} \
                        ,{card_type} ,{card_content.number},{card_content.repository.name} ,{card_content.title}")
                    new_row = {
                        self.rhn.value("project"): self.project_object.name,
                        self.rhn.value("column"): column_name,
                        "Card": card_content.title,
                        "CardURL": card_content.html_url,
                        self.rhn.value("type"): card_type,
                        self.rhn.value("number"): card_content.number,
                        self.rhn.value("labels"): card_content.labels,
                        self.rhn.value("repo"): card_content.repository.name,
                        self.rhn.value("state"): card_content.state,
                        "CreatedAt": card_content.created_at,
                        "UpdatedAt": card_content.updated_at,
                        "ClosedAt": card_content.closed_at
                    }
                    self.project_cards = pd.concat([self.project_cards, pd.DataFrame([new_row])], ignore_index=True)
            print(f"  end: {self.card_count} cards processed: {self.project_object.name}, Column {column.name}")
        return True

    def get_dataframe_copy(self):
        return self.project_cards.copy()

    def dataframe(self):
        return self.project_cards

    def print_project_cards(self):
        print(self.project_cards.to_string(index=False))


class SprintSummaryFrame:
    # ===================================================================================================================
    # This takes a dataframe containing raw information from a sprint
    # It makes a copy of the the dataframe that is passed in and changes that.
    # It creates a new dataframe that contains the summarized information for the sprint.
    #  - In the copied dataframe
    #     - If no column called size exists, it creates one and extracts the size from the labels.
    #  - It creates a new dataframe based on the copied dataframe
    #     - This new dataframe contains the summarized information for the sprint.
    #  You can:
    #    - get the new copied dataframe
    #    - get the newlye created dataframe
    # ===================================================================================================================
    def __init__(self,
                 df_in: pd.DataFrame = None):
        self.rhn = RequiredDfColumnHeaderNames()
        self.rcv = RequiredSprintColumnValues()
        self.df = None
        if df_in is None:
            print(f"Failed to pass in a dataframe")
            return

        self.df = pd.DataFrame(columns=df_in.columns, data=copy.deepcopy(df_in.values))
        self.sprint_col_values = list(self.df[self.rhn.value('column')].unique())
        self.sprint_active_col_values = self.rcv.list()
        # verify that the minimum df headers exist
        # verify that the minimum sprint column names exist
        if list_contains_at_least(self.rhn.values(), self.df.columns) and \
           list_contains_at_least(self.sprint_active_col_values, self.sprint_col_values):
            print(f"Passes header name and sprint column values checks")
        else:
            print(f"Failed header name or sprint column values check")
            return

        # missing an else statement that exits here
        # create the output dataframe
        self.df_summary = pd.DataFrame(columns=["Column", "Size"])

        self._clean_labels()
        self._add_size_column()
        self._summarize_size_column()
        self._summarize_size_in_sprint_cols()
        self._print_summary()

    def print_issues(self):
        print(self.df.to_string(index=False))

    def _clean_labels(self):
        # Make sure there is at least an empty string in the labels column
        for index, row in self.df.iterrows():
            if not isinstance(row[self.rhn.value('labels')], str):
                self.df.at[index, self.rhn.value('labels')] = ""

    def _add_size_column(self):
        # -----------------------------------------------------------------------------------------------------------------
        # This function adds a column to the dataframe to store the size as extracted from the "Size: X"
        # It is careful to use the predefined column name for the size column.
        # -----------------------------------------------------------------------------------------------------------------
        if self.rhn.value('size') not in self.df.Column:
            self.df[self.rhn.value('size')] = 0
        for index, row in self.df.iterrows():
            size_num = 0
            label_list = row[self.rhn.value('labels')].split(',')
            lower_list = [label.lower() for label in label_list]
            size_label = [label.strip() for label in lower_list if 'size:' in label]
            if len(size_label) > 0:
                size_label_str = ' '.join(size_label)
                search_result = re.search(r'[0-9]+', size_label_str)
                if search_result is not None:
                    search_result = re.search(r'[0-9]+', size_label_str).group()
                    size_num = int(search_result)
                self.df.at[index, self.rhn.value('size')] = size_num
                print(f" num:{row[self.rhn.value('number')]} state:{row[self.rhn.value('column')]} \
                    s:{size_num}  labels:{row[self.rhn.value('labels')]}")

    def _summarize_size_column(self):
        for col_val in self.sprint_col_values:
            # I have no idea what this next line does
            sumnum = self.df[self.df[self.rhn.value('column')] == col_val][self.rhn.value('size')].sum()
            new_row = {
                self.rhn.value('column'): col_val,
                self.rhn.value('size'): sumnum
            }
            self.df_summary = pd.concat([self.df_summary, pd.DataFrame([new_row])], ignore_index=True)
            print(f"{sumnum}\t{col_val}")

    def _summarize_size_in_sprint_cols(self):
        # now create a list of the columns we consider to be active sprint columns
        sumnum = 0
        for name in self.sprint_active_col_values:
            sumnum = sumnum + self.df[self.df[self.rhn.value('column')] == name][self.rhn.value('size')].sum()

        new_row = {
            self.rhn.value('column'): "ActiveSprint",
            self.rhn.value('size'): sumnum
        }
        self.df_summary = pd.concat([self.df_summary, pd.DataFrame([new_row])], ignore_index=True)
        print(f"{sumnum}\tInTheSprint")

    def _add_additional_columns(self):
        new_row = {
            "Date": "DATEHERE",
            "SprintName": "SPRINTNAMEHERE"
        }
        self.df_summary = pd.concat([self.df_summary, pd.DataFrame([new_row])], ignore_index=True)

    def _print_summary(self):
        print('\t'.join(map(str, list(self.df_summary.columns))))
        for index, row in self.df_summary.iterrows():
            print('\t'.join(map(str, list(row))))
