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


class RequiredDfColumnHeaderNames:
    # This dictionary should be edited to to be what is expected.
    # prolly in a real app this would be a config file.
    def __init__(self):
        self.names = {
            "project": "Project",
            "column": "Column",
            "type": "CardType",
            "number": "Number",
            "labels": "Labels",
            "repo": "Repo",
            "state": "State"
        }

    def col(self, name: str = None):
        return str(self.names[name])

    def col_names(self):
        return list(self.names.keys())

    def col_values(self):
        return list(self.names.values())

    def print(self):
        print(f"Column names: {self.names}")

# ===================================================================================================================
# .
# .
# .
# ===================================================================================================================
#
#    input:
#         :
#   output:
#  precond: required_list is defined.
# postcond:
#    descr:
#
#
#         if not list_contains_at_least_required_entries(
#                 required_list=RequiredDfColumnHeaderNames().col_names(),
#                 submitted_list=[column.name for column in columns]
#
#         ):
#             print(f"required column_head_names not present")
#
#
# --------------------------------------------------------------------------------------------------------------------


def list_contains_at_least_required_entries(required_list: list = None, submitted_list: list = None):
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


def WriteDf(df: pd.DataFrame = None,
            out_dir: str = '/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk',
            out_name: str = 'output'):
    out_file = out_dir + '/' + pd.Timestamp.now().strftime("%Y_%m_%d-%H_%M_%S")+ "-" + sanitize_filename(out_name) + ".tsv"
    print(f"Saving result to file.")
    print(f" {out_file}")
    df.to_csv(out_file, sep='\t', index=False)


# this should not be run until you have verified that the column names are correct.
# e.g. if there is no column that is expected to contain these values in the input
# then it's not worth even running this.




class RequiredExactSprintColumnValues:
    # This list should be edited to to be what is expected.
    # prolly in a real app this would be a config file.

    def __init__(self):
        self.names = [
            "This Sprint 🏃‍♀️ 🏃",
            "IQSS Team - In Progress  💻",
            "Ready for Review ⏩",
            "Review 🔎"
        ]

    def all(self):
        return self.names

    def print(self):
        print(f"Column values: {self.names}")


class DFFromFile:
    def __init__(self, in_dir: str = None, file_name: str = None):
        self.df = None
        print(" Reading in data from a file.")
        print(f" input file directory: {in_dir}, input file name: {file_name}")
        input_file = in_dir + '/' + file_name
        print(f" input_file: {input_file}")

        if (file_name is None) or (in_dir is None) or (not os.path.isdir(in_dir)):
            print("Attempt to read input from file. No valid initialization data.  Exiting.")
        else:
            self.df = pd.read_csv(input_file, sep='\t')


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
                self.rhn.col("project"),
                self.rhn.col("column"),
                "Card",
                "CardURL",
                self.rhn.col("type"),
                self.rhn.col("number"),
                self.rhn.col("labels"),
                self.rhn.col("repo"),
                self.rhn.col("state"),
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
                card_content = card.get_content()
                if card_content is not None and card.updated_at >= three_months_ago:
                    self.card_count += 1
                    regex1 = re.compile(r"(/issues/|/pull/)")
                    regex2 = re.compile(r"(issues|pull)")
                    card_type = regex1.search(card_content.html_url).group(0)
                    card_type = regex2.search(card_type).group(0)
                    if self.card_count % 50 == 0:
                        print(f">>>>>> {self.card_count} # cards {self.project_object.name}: {column.name} \
                        ,{card_type} ,{card_content.number} \
                        ,{card_content.repository.name} ,{card_content.title}")

                    new_row = {
                        self.rhn.col("project"): self.project_object.name,
                        self.rhn.col("column"): column_name,
                        "Card": card_content.title,
                        "CardURL": card_content.html_url,
                        self.rhn.col("type"): card_type,
                        self.rhn.col("number"): card_content.number,
                        self.rhn.col("labels"): card_content.labels,
                        self.rhn.col("repo"): card_content.repository.name,
                        self.rhn.col("state"): card_content.state,
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




# #################################################################################################################

