from datetime import timedelta

# from argparse import ArgumentParser
# from dict2xml import dict2xml
# from argparse import ArgumentParser
# github library: https://github.com/PyGithub/PyGithub
#                 https://pygithub.readthedocs.io/en/stable/introduction.html
#                 2023_09_29 V2.1.1
#
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


class LegacyProjectCards:
    # ===================================================================================================================
    # represents a query of data of all the cards from a legacy GitHub project
    # The query drills down: organization > project > card content (Issue or pr)
    # you can:
    # - get the dataframe
    # - get the number of cards
    # this makes use of the

    # ===================================================================================================================
    #
    #    input:
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
                RequiredDfColumnHeaderNames.value("card"),
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

        # The documentation seems wrong here.
        # https://pygithub.readthedocs.io/en/stable/github.html?highlight=get_organization#github.MainClass.Github.get_organization
        #  get_organization(login: str) → Organization
        #       Calls:	GET /orgs/{org}
        # The actual parameter is the organization name. My code is correct.
        self._organization_api_object = self._client.get_organization(self._organization_name)
        if not self._organization_api_object:
            print(f"Cannot populate organization Objecct")
            return False

        # Find the project we care about
        if not self._fetch_project_api_obj():
            print(f"Cannot populate project we care about")
            return False

        # TODO: I think the logic here is bad.
        # #56 I've got code failing inside this call.
        # I think there is some sort of chicken/egg thing happening. Like - I'm testing to see if something is empty
        # but the test to see if it's empty is failing when it's empty
        # I think this may be where I need to be catching an exception?
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
        print(f"Pandas version:{pd.__version__}")
        # return the legacy project columns names
        # check to make sure that they contain the critical columns we care about.
        # https://pygithub.readthedocs.io/en/stable/github_objects/ProjectColumn.html
        columns = self._project_object.get_columns()
        # three_months_ago = datetime.datetime.utcnow() - timedelta(days=90)

        self._card_count = 0
        self._card_count_used = 0
        for column in columns:

            # https://pygithub.readthedocs.io/en/stable/github_objects/ProjectColumn.html?highlight=project
            cards = column.get_cards(archived_state="not_archived")
            print(f"start: {self._card_count_used}, {self._card_count} cards processed: {self._project_object.name}, Column {column.name}")
            for card in cards:
                self._card_count += 1
                # get_content() can take "PullRequest" or "Issue" as an argument
                # These notes are from the source code!
                # https://github.com/PyGithub/PyGithub/blob/master/github/ProjectCard.py
                # Note that the content_url for any card will be an "issue" URL, from
                # which you can retrieve either an Issue or a PullRequest. Unfortunately
                # the API doesn't make it clear which you are dealing with.

                card_content = card.get_content()
                # debug: print(card_content)
                # if card_content is not None and card.updated_at >= three_months_ago:
                if card_content is not None:
                    self._card_count_used +=1
                    regex1 = re.compile(r"(/issues/|/pull/)")
                    sub_string = regex1.search(str(card_content.html_url)).group(0).replace("/", "")
                    card_type = "Issue"
                    if sub_string == "pull":
                        card_type = "PullRequest"
                    # debug
                    # print(f">>>>>> {self._card_count} # cards {self._project_object.name}: {column.name} \
                    # ,{card_type} ,{card_content.number},{card_content.repository.name} ,{card_content.title}")
                    if self._card_count % 50 == 0:
                        print(f">>>>>> {self._card_count_used}, {self._card_count} vcards processed: {self._project_object.name}: {column.name} \
                        ,{card_type} ,{card_content.number},{card_content.repository.name} ,{card_content.title}")

                    new_row = {
                        # '' if XXXX is None else str(XXXX),
                        RequiredDfColumnHeaderNames.value("project"): '' if self._project_object.name is None else str(self._project_object.name),
                        RequiredDfColumnHeaderNames.value("column"):  '' if column.name is None else str(column.name),
                        RequiredDfColumnHeaderNames.value("card"): '' if card_content.title is None else str(card_content.title),
                        RequiredDfColumnHeaderNames.value("CardURL"): '' if card_content.html_url is None else str(card_content.html_url),
                        RequiredDfColumnHeaderNames.value("type"): '' if card_type is None else str(card_type),
                        RequiredDfColumnHeaderNames.value("number"): card_content.number,
                        RequiredDfColumnHeaderNames.value("labels"): '' if card_content.labels is None else str(card_content.labels),
                        RequiredDfColumnHeaderNames.value("repo"): '' if card_content.repository.name is None else str(card_content.repository.name),
                        RequiredDfColumnHeaderNames.value("state"):  '' if card_content.state is None else str(card_content.state),
                        RequiredDfColumnHeaderNames.value("CreatedAt"): '' if card_content.created_at is None else str(card_content.created_at),
                        RequiredDfColumnHeaderNames.value("UpdatedAt"): '' if card_content.updated_at is None else str(card_content.updated_at),
                        RequiredDfColumnHeaderNames.value("ClosedAt"): '' if card_content.closed_at is None else str(card_content.closed_at),
                        RequiredDfColumnHeaderNames.value("ClosedBy"): '' if card_content.closed_by is None else str(card_content.closed_by)

                    }
                    # debug:
                    # print(f"{new_row}\n====\n")
                    # print(f"{pd.DataFrame([new_row])}\n====\n")
                    # print(f"{self._project_cards}\n====\n")
                    self._project_cards = pd.concat([self._project_cards, pd.DataFrame([new_row])], ignore_index=True)
            print(f"  end: {self._card_count_used}, {self._card_count} cards processed: {self._project_object.name}, Column {column.name}")
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
