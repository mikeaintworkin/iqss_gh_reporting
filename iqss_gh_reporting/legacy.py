from datetime import timedelta

# from argparse import ArgumentParser
# from dict2xml import dict2xml
# from argparse import ArgumentParser
from github import Github
# from gql import gql, Client
# from gql.transport.aiohttp import AIOHTTPTransport
# from json2xml import json2xml
from pathvalidate import sanitize_filename
from pathvalidate import sanitize_filepath
# from typing import Literal
# import argparse
# import asyncio
import datetime
# import json
import os
import pandas as pd
import re
import copy
from iqss_gh_reporting.transformer import RequiredDfColumnHeaderNames


#
def get_kickoff_issue(number: str = "87", repo_owner: str = "IQSS",
                      repo: str = "dataverse-frontend",
                      access_token: str = "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"):
    # ----------------------------------------------------------------------------------------------------------
    # Take a PR and use the legacy GitHub API to get the issue that kicked it off.
    # As best I can tell
    # - the only way to get the information is to retrieve the value of the issue_url.
    # - The native API describes this as a list. However pyGitHub returns only a string.
    # - I did a quick test where I added a second issue to an active PR and did a lookup to confirm this.
    # - My operating assumption is that the value of pr.issue_url will return the first issue
    # - I tried to create an test pull request without an issue. It looks like it needs two different
    # - branches.  I'm not sure what to make of this. for now I'm going to assume that the value will
    #   always be at least an empty stirn
    # ----------------------------------------------------------------------------------------------------------
    client = Github(access_token)
    repo_string = repo_owner + '/' + repo
    repo = client.get_repo(repo_string)
    pr = repo.get_pull(int(number))

    # get the list of issues that pr closes and filter out the ones that are already closed
    # In reality issue_url returns only a single issue as a string
    issue_number = re.search(r'(?<=issues/)\d+', pr.issue_url).group(0)
    issues = [].append(issue_number)
    print(f"Issue #{issue_number}")
    # The code current can only return a list of 1 issue
    return issues


class LegacyProjectCards:
    # ===================================================================================================================
    # represents a query of data of all the cards from a legacy GitHub project
    # The query drills down: organization > project > card content (Issue or pr)
    # you can:
    # - get the dataframe
    # - get the number of cards
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
    # --------------------------------------------------------------------------------------------------------------------
    # init will return true if it was able to retrieve the data
    def __init__(self, access_token: str, organization_name: str, project_name: str):
        # prereq: out_dir and outputfile are assumed to be valid
        # come back here and do the validation later
        self.date_stamp = pd.Timestamp.now().strftime("%Y_%m_%d-%H_%M_%S")

        # internal init
        self._card_count = 0
        self._project_cards = pd.DataFrame(
            columns=[
                RequiredDfColumnHeaderNames.value("project"),
                RequiredDfColumnHeaderNames.value("column"),
                RequiredDfColumnHeaderNames.value("Card"),
                RequiredDfColumnHeaderNames.value("CardURL"),
                RequiredDfColumnHeaderNames.value("type"),
                RequiredDfColumnHeaderNames.value("number"),
                RequiredDfColumnHeaderNames.value("labels"),
                RequiredDfColumnHeaderNames.value("repo"),
                RequiredDfColumnHeaderNames.value("state"),
                RequiredDfColumnHeaderNames.value("CreatedAt"),
                RequiredDfColumnHeaderNames.value("UpdatedAt"),
                RequiredDfColumnHeaderNames.value("ClosedAt"),
                RequiredDfColumnHeaderNames.value("ClosedBy")
                ]
            )
        # external init
        self._client = Github(access_token, per_page=100)
        self._project_name = project_name
        self._organization_name = organization_name
        self._organization_api_object = None
        self._fetch_data()

    def _fetch_data(self):

        self._organization_api_object = self._client.get_organization(self._organization_name)
        if not self._organization_api_object:
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
        projects = self._organization_api_object.get_projects()
        # find our project
        for p in projects:
            print(f"projects: looking to match {self._project_name} with {p.name}")
            if p.name == self._project_name:
                self._project_object = p
                return True

        print(f"project {self._project_name} not found")
        return False

    # return true if we are successful
    def _get_project_cards_api_obj(self):

        # return the legacy project columns names
        # check to make sure that they contain the critical columns we care about.
        columns = self._project_object.get_columns()
        # three_months_ago = datetime.datetime.utcnow() - timedelta(days=90)

        self._card_count = 0
        for column in columns:
            column_name = column.name
            cards = column.get_cards(archived_state='not_archived')
            print(f"start: {self._card_count} cards processed: {self._project_object.name}, Column {column.name}")
            for card in cards:
                self._card_count += 1
                card_content = card.get_content()
                # if card_content is not None and card.updated_at >= three_months_ago:
                if card_content is not None:
                    regex1 = re.compile(r"(/issues/|/pull/)")
                    regex2 = re.compile(r"(issues|pull)")
                    card_type = regex1.search(card_content.html_url).group(0)
                    card_type = regex2.search(card_type).group(0)
                    card_type = 'undefined' if card_type not in ['issues', 'pull'] else card_type
                    if self._card_count % 50 == 0:
                        print(f">>>>>> {self._card_count} # cards {self._project_object.name}: {column.name} \
                        ,{card_type} ,{card_content.number},{card_content.repository.name} ,{card_content.title}")

                    # If the card is associated with a pull request, include the associated issues
                    # in PyGitHub, the only thing we have to workwith is the issue_url
                    # The legacy api says that this isa list of URLs, but PyGithub returns a single URL
                    this_pr_closes = ""
                    if card_type == "pull":
                        if hasattr(card_content, 'issue_url'):
                            this_pr_closes = this_pr_closes + ";" + "has attr issue_url"
                            if card_content.issue_url is not None:
                                this_pr_closes = card_content.issue_url
                            else:
                                this_pr_closes = this_pr_closes + ";" + "issue_url is None"
                        else:
                            this_pr_closes  = this_pr_closes + ";" + "has no attr issue_url"

                    new_row = {
                        RequiredDfColumnHeaderNames.value("project"): self._project_object.name,
                        RequiredDfColumnHeaderNames.value("column"): column_name,
                        RequiredDfColumnHeaderNames.value("Card"): card_content.title,
                        RequiredDfColumnHeaderNames.value("CardURL"): card_content.html_url,
                        RequiredDfColumnHeaderNames.value("type"): card_type,
                        RequiredDfColumnHeaderNames.value("number"): card_content.number,
                        RequiredDfColumnHeaderNames.value("labels"): card_content.labels,
                        RequiredDfColumnHeaderNames.value("repo"): card_content.repository.name,
                        RequiredDfColumnHeaderNames.value("state"): card_content.state,
                        RequiredDfColumnHeaderNames.value("CreatedAt"): card_content.created_at,
                        RequiredDfColumnHeaderNames.value("UpdatedAt"): card_content.updated_at,
                        RequiredDfColumnHeaderNames.value("ClosedAt"): card_content.closed_at,
                        RequiredDfColumnHeaderNames.value("Closes"): this_pr_closes
                    }
                    self._project_cards = pd.concat([self._project_cards, pd.DataFrame([new_row])], ignore_index=True)
            print(f"  end: {self._card_count} cards processed: {self._project_object.name}, Column {column.name}")
        return True

    @property
    def df(self):
        return self._project_cards

    def print_project_cards(self):
        print(self._project_cards.to_string(index=False))

    @property
    def card_count(self):
        return self._card_count

    @property
    def type(self):
        return type(self).__name__


