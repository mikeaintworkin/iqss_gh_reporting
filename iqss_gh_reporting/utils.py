# Credits: ChatGPT
import datetime
import json

# Use PyGithub to get the project cards
from github import Github
from typing import Literal
import re
from pathvalidate import sanitize_filename
import pandas as pd


# ===================================================================================================================
# This class summarizes the columns in a project board.
# It requires that the pandas dataframe object that is passed in has the columns that it expects.
# It calculates the sum of the size column for each column in the project board.
# It also calculates the sum of the sized items that we consider to be active.
# .
# .
# .
# ===================================================================================================================
#
#    input:
#         :
#   output:
#  precond:
#         :  These columns in: _column_headers_exist must exist
#         :  The dataframe is assumed to have a list of labels in the Labels column and one of them is assumed to be
#         :  a size label.
#         :  One of the values for "Column" is assumed to be "Done 🚀"
# postcond:  output will contain the data from the columns described in the precondition
#    descr:
#
#
# Sample calls:
# rpt = utils.SprintSummaryFrame(in_dir='/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk/',file_name='2023_04_20-15_54_44-IQSSdataverse-legacy.tsv')
#
#
# --------------------------------------------------------------------------------------------------------------------
class SprintSummaryFrame:
    #def __init__(self, df: pd.DataFrame = None, in_dir: str = None, out_dir: str = in_dir, file_name: str = None):
    def __init__(self,
                 hproject: str = "Project",
                 hcolumn: str = "Column",
                 htype: str = "CardType",
                 hnumber: str = "Number",
                 hlabels: str = "Labels",
                 hrepo: str = "Repo",
                 hstate: str = "State",
                 hcol_val_eq_thissprint: str = "This Sprint 🏃‍♀️ 🏃 ", #come back and remote this extra space
                 hcol_val_eq_wip: str = "IQSS Team - In Progress  💻",
                 hcol_val_eq_readyforreview: str = "Ready for Review ⏩",
                 hcol_val_eq_inreview: str = "Review 🔎",
                 df: pd.DataFrame = None,
                 in_dir: str = None,
                 out_dir: str = None,
                 file_name: str = None):
        # these are the column headers that we expect to find in the dataframe
        self.desired_headers = {
            "hproject": hproject ,
            "hrepo": hrepo,
            "hcolumn": hcolumn,
            "htype": htype,
            "hnumber": hnumber,
            "hstate": hstate,
            "hlabels": hlabels
        }

        # are we reading in the data from a file?
        # if given a dataframe and file information as input, we'll try for the file
        #  and ignore the dataframe.
        self.df_orig = None
        if file_name is not None:
            if in_dir is not None:
                print(" Reading in data from a file.")
                print(f" input file directory: {in_dir}, input file name: {file_name}")
                input_file = in_dir + '/' + file_name
                self.df_orig = pd.read_csv(input_file, sep='\t')
            else:
                print(f" input file directory: {in_dir}, input file name: {file_name}")
                print("Attempt to read input from file. No valid initialization data.  Exiting.")
                exit(1)

        if self.df_orig is None:
            # at this point we've read in a dataframe or we were sent one.
            # or something is wrong.
            if df is None:
                print("Attempted to read in from a file.")
                print("Attempted to read in from a data frame.")
                print("No valid initialization data.  Exiting.")
                exit(1)
            else:
                self.df_orig = df

        self.orig_data_hcolumn_values = list(self.df_orig[self.desired_headers['hcolumn']].unique())
        self.sprint_col = [hcol_val_eq_thissprint, hcol_val_eq_wip, hcol_val_eq_readyforreview, hcol_val_eq_inreview]

        if not self._headers_exist():
            print("Missing columns headers.  Exiting.")
            exit(1)

        if not self._column_names_exist():
            print("Missing Sprint States.  Exiting.")
            exit(1)

        # create the output dataframe
        self.df_summary = pd.DataFrame(columns=["Column", "Size"])
        self.df_summary.out_dir = out_dir
        if out_dir is None:
            self.df_summary.out_dir = in_dir
        if self.df_summary.out_dir is None:
            self.df_summary.out_dir = "."
        print(f"Summary Output directory: {self.df_summary.out_dir}")
        self._clean_labels()
        self._add_size_column()
        self._summarize_size_column()
        self._summarize_size_in_sprint_cols()

    # was the df that was passed in to initialize the object missing any of the columns that we need?
    # check for existence of specific columns
    def _headers_exist(self):
        missing_columns = [col for col in self.desired_headers.values() if col not in self.df_orig.columns]
        if missing_columns:
            print(f"Missing columns: {missing_columns}")
            return False
        else:
            print("All desired columns are present.")
            return True

    def _column_names_exist(self):
        missing_names = [col for col in self.sprint_col if col not in list(self.df_orig[self.desired_headers['hcolumn']].unique())]
        if missing_names:
            print(f"Missing names: {missing_names}")
            return False
        else:
            print("All desired columns are present.")
            return True


    def print_issues(self):
        print(self.df.to_string(index=False))

    def _clean_labels(self):
        for index, row in self.df_orig.iterrows():
            if not isinstance(row[self.desired_headers['hlabels']], str):
                self.df_orig.at[index, 'Labels'] = ""


    # This function adds a column to the dataframe called 'size' and populates it with the size of the issue
    #  if the issue has a size label
    # this needs some work.  It's not very robust.
    def _add_size_column(self):
        if not 'size' in self.df_orig.Column:
            self.df_orig['size'] = 0
        for index, row in self.df_orig.iterrows():
            size_num = 0
            label_list = row[self.desired_headers['hlabels']].split(',')
            lower_list = [label.lower() for label in label_list]
            size_label = [label.strip() for label in lower_list if 'size:' in label]
            if len(size_label) > 0:
                size_label_str = ' '.join(size_label)
                search_result = re.search(r'[0-9]+',size_label_str)
                if search_result is not None:
                    search_result = re.search(r'[0-9]+', size_label_str).group()
                    size_num = int(search_result)
                self.df_orig.at[index, 'size'] = size_num
                #if row[self.desired_headers['hcolumn']] != 'Done 🚀':
                print(f" num:{row[self.desired_headers['hnumber']]} state:{row[self.desired_headers['hcolumn']]} s:{size_num}  labels:{row[self.desired_headers['hlabels']]}")

    #self.orig_data_hcolumn_values = list(self.df_orig[self.desired_headers['hcolumn']].unique())
    #self.sprint_col = [hcol_val_eq_thissprint, hcol_val_eq_wip, hcol_val_eq_readyforreview, hcol_val_eq_inreview]
    def _summarize_size_column(self):
        for col_val in self.orig_data_hcolumn_values:
            sumnum = self.df_orig[self.df_orig[self.desired_headers['hcolumn']] == col_val]['size'].sum()
            new_row = {
                self.desired_headers['hcolumn']: col_val,
                'Size': sumnum
            }
            self.df_summary = pd.concat([self.df_summary, pd.DataFrame([new_row])], ignore_index=True)
            print(f"{sumnum}\t{col_val}")

    def _summarize_size_in_sprint_cols(self):
        # now create a list of the columns I care about using a heuristic
        sumnum = 0
        for name in self.sprint_col:
            sumnum = sumnum + self.df_orig[self.df_orig[self.desired_headers['hcolumn']] == name]['size'].sum()
        new_row = {
            'Column': "ActiveSprint",
            'Size': sumnum
        }
        self.df_summary = pd.concat([self.df_summary, pd.DataFrame([new_row])], ignore_index=True)
        print(f"{sumnum}\tActiveSprint")




    def print_issues_by_columns(self):
        self._clean_labels()
        self._add_size_column()
        unique_names = list(self.df['column'].unique())
        for col_name in unique_names:
            filtered_df = self.df[self.df['column'] == col_name]
            print(filtered_df)



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
class GithubLegacyProjectCardsPandas:
    def __init__(self, access_token: str, organization_name: str, project_name: str, out_dir: str, headers: list):
        # external init
        self.client = Github(access_token, per_page=100)
        self.organization = self.client.get_organization(organization_name)
        self.project_name = project_name
        self.out_dir = out_dir

        # internal init
        self.card_count = 0
        self.project_cards = pd.DataFrame(columns=["Project", "Column", "Card", "CardURL", "CardType", "Number", "Labels", "Repo", "State", "CreatedAt", "UpdatedAt", "ClosedAt"])
        self.date_stamp = pd.Timestamp.now().strftime("%Y_%m_%d-%H_%M_%S")
        # prereq: out_dir and outputfile are assumed to be valid
        self.out_dir = out_dir
        self.outputfile = self.date_stamp + "-" + sanitize_filename(project_name)  + "-legacy"

    def get_project_cards(self):
        projects = self.organization.get_projects()
        project = None
        self.card_count = 0

        # find our project
        for p in projects:
            print(f"projects: looking to match {self.project_name} with {p.name}")
            if p.name == self.project_name:
                project = p
                break
        # Let's get the cards
        if project is not None:
            columns = project.get_columns()
            for column in columns:
                column_name = column.name
                cards = column.get_cards()
                print(f"start: {self.card_count} cards processed: {project.name}, Column {column.name}")
                for card in cards:
                    self.card_count += 1
                    card_content = card.get_content()
                    #
                    if card_content is not None:
                        regex1 = re.compile(r"(/issues/|/pull/)")
                        regex2 = re.compile(r"(issues|pull)")
                        card_type = regex1.search(card_content.html_url).group(0)
                        card_type = regex2.search(card_type).group(0)
                        if self.card_count % 50 == 0:
                            print(f">>>>>> {self.card_count} cards processed: {project.name}: Column {column.name} ,{card_type} ,{card_content.number} ,{card_content.repository.name} ,{card_content.title}")


                        # do I care about the actual type returned?
                        # if card_content.type in [Literal"Issue", Literal"PullRequest"]:

                        new_row = {
                            "Project": project.name,
                            "Column": column_name,
                            "Card": card_content.title,
                            "CardURL": card_content.html_url,
                            "CardType": card_type,
                            "Number": card_content.number,
                            "Labels": card_content.labels,
                            "Repo": card_content.repository.name,
                            "State": card_content.state,
                            "CreatedAt": card_content.created_at,
                            "UpdatedAt": card_content.updated_at,
                            "ClosedAt": card_content.closed_at
                        }
                        self.project_cards = pd.concat([self.project_cards, pd.DataFrame([new_row])], ignore_index=True)


                print(f"  end: {self.card_count} cards processed: {project.name}, Column {column.name}")
        return

    def print_project_cards(self):
        print(self.project_cards.to_string(index=False))

    def save_project_cards(self):
        output_to = self.out_dir + "/" + self.outputfile + ".tsv"
        print(f"Saving result to file.")
        print(f" {output_to}")
        self.project_cards.to_csv(output_to, sep='\t', index=False)

