from datetime import timedelta

# from argparse import ArgumentParser
# from dict2xml import dict2xml
# from argparse import ArgumentParser
from github import Github
# from gql import gql, Client
# from gql.transport.aiohttp import AIOHTTPTransport
# from json2xml import json2xml
from iqss_gh_reporting import transformer
from pathvalidate import sanitize_filename
from pathvalidate import sanitize_filepath
# from typing import Literal
# import argparse
# import asyncio
from datetime import datetime
# import json
import os
import pandas as pd
import re
import copy
from pathvalidate import sanitize_filepath


class GHProjectData:
    # ===================================================================================================================
    # Represents the dataframe and supporting metadata for a workflow that processes sprint data
    # ===================================================================================================================
    def __init__(self,
                 src_type: str = None,
                 workflow_name: str = None,
                 dest_dir_name: str = None,
                 collection_flag: str = None,
                 sprint_name: str = None,
                 src_dir_name: str = None,
                 src_file_name: str = None,
                 organization_name: str = None,
                 project_name: str = None,
                 data_collected_time= None,
                 output_file_base_name=None
                 ):
        self._df = None

        self._v = {
            'organization_name': str(organization_name),
            'project_name': str(project_name),
            'collection_flag': str(collection_flag),
            'data_collected_time': data_collected_time,
            'sprint_name': str(sprint_name),
            'in_dir': sanitize_filepath(src_dir_name, platform="auto"),
            'in_file': sanitize_filename(src_file_name, platform="auto"),
            'workflow_name': str(workflow_name),
            'src_type': str(src_type),

            'out_dir':  sanitize_filepath(dest_dir_name + '/' + sprint_name, platform="auto"),
            'output_file_base_name': str(output_file_base_name)
        }

        if src_type not in "api" and src_type not in "file":
            raise ValueError(f"Error: src_type: must be one of 'file', 'api', 'unknown'")

        # Optionally, the data_collected_time can be set in the yaml file.
        # If it's not set, or if src_type is api then set it to the current time
        # Todo: reimplement this logic elsewhere to fully support it
        if src_type == "file":
            if data_collected_time is None or len(data_collected_time) == 0:
                self._v['data_collected_time'] = pd.Timestamp.now().strftime("%Y_%m_%d_%H%M%S")
            # if we're reprocessing a file, we need to make sure that the output file goes back where it came from
            # above this, I default to assuming src_type is set to api
            self._v['out_dir'] = dest_dir_name
            if self._v['out_dir'] is None or len(self._v['out_dir']) == 0:
                self._v['out_dir'] = self._v['in_dir']
            self._v['output_file_base_name'] = self._set_output_file_base_name_4file()
        else:
            self._v['data_collected_time'] = pd.Timestamp.now().strftime("%Y_%m_%d_%H%M%S")
            if self._v['collection_flag'] not in ["start", "snapshot", "end", "unknown"]:
                raise ValueError(f"Error: sprint_snap_status must be one of: 'start', 'snapshot', 'end', 'unknown'")
            self._v['output_file_base_name'] = self._set_output_file_base_name_4api()

        os.makedirs(str(self._v['out_dir']), exist_ok=True)
        print(f"directory exists or was created now: {self._v['out_dir']}")


        self._log = None
        self._initialize_log()
        self._validate_headers()
        self._validate_metadata()
        self._validate_sprint_status_values()

    def _set_output_file_base_name_4file(self):
        # --------------------------------------------------------------------------------------------------------
        # set output file base name to:
        # output_file_base_name	-src_type	-workflow_name	-(timestamp)
        # --------------------------------------------------------------------------------------------------------
        if self._v['output_file_base_name'] is None or len(self._v['output_file_base_name']) == 0:
            self._v['output_file_base_name'] = str(os.path.basename(self._v['in_file']))

        self._v['output_file_base_name'] = os.path.splitext(self._v['output_file_base_name'])[0]
        f = transformer.string_cleaned(self._v['output_file_base_name'])
        wfn = self._v['workflow_name']
        if wfn is not None and len(wfn) > 0:
            f = f + "-" + transformer.string_cleaned(wfn)

        f = f + "-" + transformer.string_cleaned(self._v['src_type']) \
            + "-" + self._v['data_collected_time']

        f = sanitize_filename(f, platform="auto")
        return f

    def _set_output_file_base_name_4api(self):
        # --------------------------------------------------------------------------------------------------------
        # set output file base name to:
        # sprint_name	-collection_flag	-src_type	-workflow_name	-(timestamp)
        # --------------------------------------------------------------------------------------------------------
        f = \
            transformer.string_cleaned(self._v['sprint_name']) \
            + "-" + transformer.string_cleaned(self._v['collection_flag'])
        wfn = self._v['workflow_name']
        if wfn is not None and len(wfn) > 0:
            f = f + "-" + transformer.string_cleaned(wfn)

        f = f + "-" + transformer.string_cleaned(self._v['src_type']) \
            + "-" + self._v['data_collected_time']
        f = sanitize_filename(f, platform="auto")
        print(f"output_file_base_name 4api: {f}")
        return f

    def _initialize_log(self):
        col_headers = [
            "DateTime",
            "CurrentContext",
            "Comment"
        ]
        self._log = pd.DataFrame(columns=col_headers)
        self.add_log_entry(
            context="init",
            comment="initializing data object."
        )
        for key, value in self._v.items():
            self.add_log_entry(
                context="init",
                comment=key + " = " + str(value)
            )

    def add_log_entry(self, context: str = "none", comment: str = "none"):
        new_row = {
            "DateTime": pd.Timestamp.now().strftime("%Y_%m_%d-%H_%M_%S"),
            "CurrentContext": context,
            "Comment": comment
        }
        self._log = pd.concat([self._log, pd.DataFrame([new_row])], ignore_index=True)

    def write_log(self):
        # ===================================================================================================================
        # This writes the contents of work log to a file
        # ===================================================================================================================
        out_file = self._v['out_dir'] + '/' + self._v['output_file_base_name'] + "-log.tsv"
        print(f"Writing Log to:.")
        print(f" {out_file}")
        self._log.to_csv(out_file, sep='\t', index=False)

    # def get_issue(self, pr: Card = None):
    #      # -------------------------------------------------------------------------------------------
    #      #
    #      # -------------------------------------------------------------------------------------------
    #      filtered_df = self._df[(self._df['Number'] == pr.number) & (self._df['Repo'] == pr.repo])]
    #      print(filtered_df)
    #      return

    @property
    def dest_dir_name(self):
        return self._v['out_dir']

    @property
    def dest_file_name(self):
        return self._v['output_file_base_name']

    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, df: pd.DataFrame = None):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("df must be a Pandas DataFrame")
        self._df = df

    @property
    def log(self):
        return self._log

    @property
    def data_src_type(self):
        return self._v['src_type']

    @property
    def data_collected_time(self):
        return self._v['data_collected_time']

    @property
    def sprint_name(self):
        return self._v['sprint_name']

    @property
    def workflow_name(self):
        return self._v['workflow_name']

    @property
    def out_dir(self):
        return self._v['out_dir']

    @property
    def organization_name(self):
        return self._v['organization_name']

    @property
    def project_name(self):
        return self._v['project_name']

    def write(self, postfix: str = ""):
        # ===================================================================================================================
        # This writes the contents of a dataframe to a tab delimited file.
        # ===================================================================================================================
        out_file = sanitize_filepath(self._v['out_dir'], platform="auto") \
                   + '/' + sanitize_filename(self._v['output_file_base_name'], platform="auto") \
                   + '-' \
                   + postfix \
                   + ".tsv"
        print(f"Saving result to file.")
        print(f" {out_file}")
        self._df.to_csv(out_file, sep='\t', index=False)

    def _validate_metadata(self):
        # ===================================================================================================================
        # This validates the metadata for the data object.
        # ===================================================================================================================
        return True

    def _validate_headers(self):
        # ===================================================================================================================
        # This validates the column headers for the data object dataframe.
        # It will ensure that any df with an object of this type has a consistent set of column headers.
        # ===================================================================================================================
        return True

    def _validate_sprint_status_values(self):
        # ===================================================================================================================
        # This validates the possible values associated with the "Column" column header from teh sprint.
        # It will ensure that any df with an object of this type has a consistent set of column headers.
        # It will need to take into account that the sprint may have been created with a different set of column header
        #  values than the current set of column header values.
        # ===================================================================================================================
        return True

# class Card:
#     def __init__(self, number: str, repo: str, labels_str: str, labels: list = None):
#         # ===================================================================================================================
#         # This creates an object that is generic enough to be used to represent an issue or a pr
#         # For simplicity, all of the properties are public
#         # properties:
#         #  number: str - the number (e.g. Issue number or PR number)
#         #  repo: str - the repo name
#         #  labels_str: str - the labels as a comma separated string
#         #  labels: list - the labels as a list
#         # ===================================================================================================================
#         # self.project =
#         # self.column =
#         # self.title =
#         # self.cardurl =
#         # self.type =
#         # self.createdat =
#         # self.updatedat =
#         # self.closedat =
#         self.state = None
#         self.size = None
#         self.number = number
#         self.repo = repo
#         self.comment = None
#         # comeBackAndFix - this is too simplistic.
#         if labels is None:
#             labels = labels_str.split(",")
#         elif labels_str is None:
#             labels_str = ",".join(labels)
#         self.labels = labels
#         self.labels_str = labels_str
