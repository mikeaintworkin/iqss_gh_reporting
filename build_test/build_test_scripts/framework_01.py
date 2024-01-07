#!/usr/bin/env python3

from datetime import datetime
from iqss_gh_reporting import legacy as pdio
from iqss_gh_reporting import pdata as pdata
from iqss_gh_reporting import transformer as transformer
from iqss_gh_reporting import transformer as xfmr
from iqss_gh_reporting import utils as utils
from pathvalidate import sanitize_filename
from pathvalidate import sanitize_filepath
import argparse
import os
import pandas as pd
import re
import yaml


class PRSizer:
    """
    Populate missing sizes for PRs generated during this sprint from their sized issues

    Parameters:
    ----------
    df_snap: input; This snapshot data as input
    df_snap: output; the data is modified

    Raise:
    -----
    ValueError
        DataFrame is empty
    KeyError
        DataFrame is missing the label field or key field

    Return:
    ------
    DataFrame

    What it does:
    ------
    Does this PR have a "closingIssuesReferences" issue?
    The answer is yes if:
     - The df_snap dataframe has  a "closingIssuesReferences" header
     - The closingIssuesReferences column has a number in it.

    If yes:
    - retrieve the information we need from the closingIssuesReferences issue by looking it up in the df_sprint_start dataframe
    if no:
    - Use the API to retrieve the issue number from the PR

    Retrieve the issue information we need from the issue by looking it up in the df_sprint_start dataframe

    Return it in df_snap

    Input Assumptions:
    ------
    By using the pdata object, I will be able to assume that the dataframe has the following columns:
    - "Closes" - a comma separated list of issue numbers as int
    - "Type" - with value "pull" for Pull Requests
    - "Column"
    - "Size"
    - "Number"

    Output notes:
    ------
    If the list of "closingIssuesReferences" issues is > 1, then the first one found in df_sprint_start is used.

    TODO:
    ------
    - Build out the pdata validation code in the init for that class so that I don't have to do the validation here.
    - In this code, reference the column headers using the standard names from the pdata class. I think I should
      always use th static mapping class  to reference the column headers.

    """
    def __init__(self, sp_data_sprint_snap: pdata = None, sp_data_sprint_orig: pdata = None):
        # ----------------------------------------------------------------------------------------------------------
        # Initialize:
        # sp_data_sprint_snap as self._df_snap - this is a copy of the snashot data that we are processing.
        #                                      It is treated as read/write
        # _df_2b_sized - a subset of rows from sp_data_sprint_snap that contains the PRs that we need sizes for.
        #
        # sp_data_sprint_orig as _df_orig - this is the snapshot at the start of the sprint. It is treated as read/only
        # ----------------------------------------------------------------------------------------------------------
        if not isinstance(sp_data_sprint_snap.df, pd.DataFrame):
            raise TypeError("sp_data_snap.df must be a Pandas DataFrame")
        if not isinstance(sp_data_sprint_orig.df, pd.DataFrame):
            raise TypeError("sp_data_snap.df must be a Pandas DataFrame")

        self._sprint_col_values = []
        self._df_merged = None

        self._df_snap = sp_data_sprint_snap.df.copy(deep=True)
        self._df_orig = sp_data_sprint_orig.df.copy(deep=True)

        self._df_snap = self._must_have_closes_column()
        self._df_2b_sized = self._get_pr_rows_that_are_missing_size()
        if len(self._df_2b_sized) == 0:
            #Todo: log "No PRs to size. Returning original data"
            print("No PRs to size. Returning original data")

        self._set_prs_sizes()

    def _get_pr_rows_that_are_missing_size(self):
        # ----------------------------------------------------------------------------------------------------------
        # input is the original dataframe.
        # cut it down to just the rows that are PRs that need to be sized
        # return that subset
        # ----------------------------------------------------------------------------------------------------------
        fdf = self._df_snap[self._df_snap['Column'].isin(xfmr.RequiredSprintColumnValues.NAMES)]
        fdf = fdf[fdf['Size'] == 0]
        fdf = fdf[fdf['Type'] == "pull"]
        print(f"Found {len(fdf)} PRs that need to be sized")
        return fdf

    def _must_have_closes_column(self):
        # ----------------------------------------------------------------------------------------------------------
        # input is self._df_snap
        # if it has a header called "Closes" then return original dataframe unchanged
        # otherwise return the modified dataframe with the "Closes" header added
        # ToDo: This should be moved to the pdata class or the validation class
        # ToDo: The column header should be referenced using the static mapping class
        # ----------------------------------------------------------------------------------------------------------
        missing_column = "Closes"
        if missing_column not in self._df_snap.columns:
            print(f"Adding column {missing_column} to dataframe")
            return self._df_snap.assign(**{missing_column: None})
        return self._df_snap

    def _set_prs_sizes(self ):
        # ----------------------------------------------------------------------------------------------------------
        # Input is _df_2b_sized
        # in _df_2b_sized the columns with these headers will be populated:
        # - closingIssuesReferences
        # - Size
        # - labels
        #
        # Assumes that:
        # - _df_2b_sized is not empty (Otherwise we would have previously returned)
        # - _df_2b_sized has a column called "Closes"
        # - There is only a single string value in the column "Closes" if present
        # ----------------------------------------------------------------------------------------------------------
        # Loop through the rows of the dataframe containing the PRs that need sizes
        for index, row in self._df_2b_sized.iterrows():
            print(f"This PR is missing a size: {row}")
            # First look in the the datda we have. Maybe the Closes colum is populated.
            issue_num = self._get_issue_num_this_pr_closes(row)
            # Not there? Look in GitHub for the issue that is closed by this PR
            if issue_num is not None:
                print(f"Found issue number: {issue_num}")
                print(f"We have an issue number, now get the issue and it's related data")


    def _get_issue_num_this_pr_closes(self, row: pd.Series):
        # ----------------------------------------------------------------------------------------------------------
        # return the list of issue numbers from one pr row in the df
        # This takes into account that we know that the PyGitHub library returns a single string with the issue
        #  url. There is no list for now.
        # I've grouped this code all together into one function so that within the loop that calls this I
        #  can have simply one call to get the issue number and test for None.
        # ----------------------------------------------------------------------------------------------------------
        issue_url = str(row["Closes"])
        #Is the issue number in the Closes column in the current snapshot data
        issue_num = self._extract_issue_num_from_url(issue_url)
        if issue_num is not None:
            return issue_num
        issue_num = self._fetch_issue_num_from_github(row)
        if issue_num is not None:
            return issue_num

    def _fetch_issue_num_from_github(self, row: pd.Series):
        # this means we need to look up the PR in GitHub.
        # we'll use graphql for this. We will need either the repo or the project name to get the info
        # we will return the issue number. (we will limit this to just ONE issue)
        # we will also return the size of the issue
        pr_numb = None
        pr_repo = None
        #login info 1
        #login info 2
        # left off here. Working on query in test_frame_02


    def _extract_issue_num_from_url(self, issue_url: str):
        # ----------------------------------------------------------------------------------------------------------
        # Input is a string that is not None
        # Return None or a string representation of the issue number
        # the issue_url will look like: https://github.com/thisaintwork/iqss_gh_reporting/issues/12
        # ----------------------------------------------------------------------------------------------------------

        if issue_url is None:
            print("No issue url is defined.")
            return None
        # Regular expression pattern
        pattern = r"/(\d+)"
        # Extract the number using re.search
        match = re.search(pattern, issue_url)
        # Check if a match is found
        number = None
        if match:
            number = match.group(1)
            print("issue:", number)
            return number
        if number is None:
            print("There was text there but no issue num could be extracted")
            return None
        return number



    #def _set_empty_prs_sizes(self):
        # ----------------------------------------------------------------------------------------------------------
        # Input is the dataframe containing the list of PRs that need sizes
        #
        # Do we have a column called Closes
        # - Size
        # - labels
        #
        # Assumes that:
        # - _df_2b_sized is not empty (Otherwise we would have previously returned)
        # ----------------------------------------------------------------------------------------------------------

    #
    # def _get_issue_closes_pr_info_from_df(self, issue_num: int):
    #     df_tmp = self._df_orig.loc['Number'] == issue_num]
    #     # df_tmp = df_tmp.loc['Repo'] == repo]
    #     # for index_sp, row_sp in
    #     # if result_row is not None:
    #     #     df.loc['Size'] = result_row['Size']
    #
    # def _get_closed_by(self):
    #     # ----------------------------------------------------------------------------------------------------------
    #     # in _df_2b_sized the columns with these headers will be populated:
    #     # - closingIssuesReferences
    #     # - Size
    #     # - labels
    #     #
    #     # Assumes that:
    #     # - _df_2b_sized is not empty (Otherwise we would have previously returned)
    #     # ----------------------------------------------------------------------------------------------------------
    #     # Loop through the rows of the dataframe and
    #     # retrieve the PR information from the df_sprint_start dataframe if possible
    #     for issue in self._get_prs_needs_size_numbers():
    #         if self._get_issue_closes_pr_info_from_df(issue):
    #             print(f"Found issue in df_sprint_start: {issue}")
    #         else:
    #             print(f"Did not find issue in df_sprint_start: {issue}")
    #
    # # def _get_kickoff_issue(self, issue: str, repo: str):
    # #     # ----------------------------------------------------------------------------------------------------------
    # #     # query for this issue in the self._orig dataframe
    # #     # TODO: for now this code assumes that the original issue can be assumed to be in the  self._orig dataframe
    # #     # The reason fo this is that nothing new is supposed to be added after the sprint starts.
    # #     # In particular for PRs, if a PR is created after the sprint starts, it is supposed to be sized and therefore
    # #     #  will not be on this list.
    # #     # ----------------------------------------------------------------------------------------------------------
    # #     # find the row in the kickoff sprint data that matches this Issue Number and Repo
    # #     # return the row from the kickoff sprint data
    # #     result_row =
    # #     if len(result) == 0:
    # #         return None
    # #     else:
    # #         # check that there is a header=Size value in the row
    # #         # check that there is a header=labels value in the row
    # #         # add the size to the PR row
    # #         # Todo: The labels must be a coma separated list of strings
    # #         self._df_2b_sized.at[index, "Size"] = result_row["Size"]
    # #         self._df_2b_sized.at[index, "Labels"] = \
    # #         self._df_2b_sized.at[index, "Labels"].append(result_row["Size"])
    # #     return result_row
    #
    #
    #
    #
    #
    # # def get(self, sprint_start_data: pdata = None):
    # #     # ----------------------------------------------------------------------------------------------------------
    # #     # - It creates an internal dataframe with rows where
    # #     # - the column is in one of the columns that make up an Active Sprint item
    # #     # - the size is 0
    # #     # - the type is a PullRequest
    # #     # ----------------------------------------------------------------------------------------------------------
    # #     # Problem: data collected from the legacy project does not have a closingIssuesReferences column.
    # #     #  you can't return the closingIssuesReferences Issue directly with the other data in this query.
    # #     #  For the first runs, I'm going to manually add that data to the snapshot
    # #     #
    # #     self._df_merged, = pd.merge(self._df, sprint_start_data, left_on='closingIssuesReferences', right_on='Number')
    # #     issue_num = self._df_merged['Number_y']
    # #     issue_repo = self._df_merged['Repo_y']
    # #     #attached_issues = merged['Attached Issue']
    #
    # # def write_back(self):
    # #     # ----------------------------------------------------------------------------------------------------------
    # #     # Write the updated pr size data back to the original PR in GitHub
    # #     # ----------------------------------------------------------------------------------------------------------
    # #     return


def main():
    # ================================================================================================================
    # The objective of this frame is to work through the following steps:
    # - read in a dataframe (real data)
    # - find a PR in the frame that has a zero size
    # - retrieve the closes data
    #   - Figure out what that data looks like. Is it a list? is it a string?
    # - lookup each of the issues in the list in a dataframe
    #   - successfully return the data for each of the issues
    #   - fail to look up the data for one or more of the issues.
    # - lookup each of the issues in the list in GitHub
    #   - successfully return the data for each of the issues
    #   - fail to look up the data for one or more of the issues.
    # ================================================================================================================

    print(f"Running {__file__} as the main program")
    yaml_file = os.path.expanduser(os.getcwd() + '/' + 'input_file.yaml')
    data = utils.read_yaml(yaml_file)
    if data is None:
        raise ValueError(f"Error: there must be a valid input.yaml file in the current working dir: {os.getcwd()}")

    with open(yaml_file) as file:
        ydata = yaml.load(file, Loader=yaml.FullLoader)
    yaml_string = yaml.dump(ydata, default_flow_style=False)
    print(f"input arguments:\n\n{yaml_string}")

    # set workflow specific variables
    summary_of_this_run = '''
         This workflow is used to summarize the size of the cards in a sprint.
         The input is a file that was retrieved from the API. 
         output file names are all synced so that it is obvious that they ran together.
         - the original input 
         - the original  input modified with a size column
         - A one line (2 including header) summary.
         - 4/28/23 23:40 fixed a bug which was including Sprint Ready in ActiveSprint
         '''

    # identify where we are sourcing the data from
    # This is meant to be hardcoded here

    sprint_data = pdata.GHProjectData(
        src_type=ydata['src_type'],
        workflow_name=ydata['workflow_name'],
        sprint_name=ydata['sprint_name'],
        collection_flag=ydata['collection_flag'],
        src_dir_name=ydata['src_dir_name'],
        src_file_name=ydata['src_file_name'],
        dest_dir_name=sanitize_filepath(ydata['output_base_dir'] + '/' + data['sprint_name'], platform="auto"),
        organization_name=ydata['organization_name'],
        project_name=ydata['project_name']
    )

    # sprint_data.validate_metadata()
    sprint_end_data = pdata.GHProjectData(
        src_type=ydata['src_type'],
        workflow_name=ydata['workflow_name'],
        sprint_name=ydata['sprint_name'],
        collection_flag=ydata['collection_flag'],
        src_dir_name=ydata['src_dir_name'],
        src_file_name=ydata['src_file_name'],
        dest_dir_name=sanitize_filepath(ydata['output_base_dir'] + '/' + data['sprint_name'], platform="auto"),
        organization_name=ydata['organization_name'],
        project_name=ydata['project_name']
    )

    if ydata['src_type'] == "file":
        sprint_data.df = utils.read_dataframe_file(
            in_dir=ydata['src_dir_name'],
            file_name=ydata['src_file_name']
        )
        # sprint_data.validate_metadata()
        sprint_end_data.df = utils.read_dataframe_file(
            in_dir=ydata['src_dir_name'],
            file_name=ydata['src_file_name']
        )
        sprint_data.add_log_entry(context="utils", comment=summary_of_this_run)
    elif ydata['src_type'] == "api":
        # get OAUTH token
        auth_token_val = os.getenv('GITHUB_TOKEN', "novalue")
        if auth_token_val == "novalue":
            print("You must set the GITHUB_TOKEN environment variable to run with 'api' flag for this program")
            exit(1)

        sprint_data.df = pdio.LegacyProjectCards(
            access_token=auth_token_val,
            organization_name=sprint_data.organization_name,
            project_name=sprint_data.project_name).df
    else:
        raise ValueError("src_type must be 'file' or 'api'")

    sprint_data.add_log_entry(context="pdio", comment=summary_of_this_run)
    sprint_data.write_log()
    sprint_data.write(postfix="orig")
    prs =PRSizer(sprint_data, sprint_end_data)



if __name__ == "__main__":
    main()
