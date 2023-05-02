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
from datetime import datetime
# import json
import os
import pandas as pd
import re
import copy


class GHProjectData:
    # ===================================================================================================================
    # Represents the dataframe and supporting metadata for a workflow that processes sprint data
    # collected in init:
    #                  src_type: str,
    #                  sprint_snap_status: str,
    #                  workflow_name: str,
    #                  src_dir_name: str,
    #                  src_file_name: str,
    #                  dest_dir_name: str,
    #                  data_collected_time: str = None,
    #                  sprint_name: str = "no sprint name"
    # df - data frame containing data to be processed
    # sprint_snap_status - Expected to be one of: Start, snapshot, End, unknown. Not enforced.
    # timestamp= - timestamp of the data collection. This is used to mark the time that the data was collected.
    #    in the case where the data is of type 'api' it is ignored.
    #    in the case where the data is of type 'file' it is the only way we know when the data was collected.
    #    (note this logic can likely be automated in some way)
    # src_type=
    # sprint_name= - name of the sprint. This is used to help mark when the data was collected.
    # dest_dir  - where are we directing output
    # workflow_name - intended to be the name of the python file that is running the workflow.
    #
    # example of things that I expect to put in the log:
    # DateTime,CurrentContext,Comment
    # 2023_04_27-18_12_36,GHProjectData,initializing data object.| workflow timestamp:2023_04_26-17_32_18
    # 2023_04_27-18_12_36,GHProjectData,initializing data object.| sprint name:No Sprint Name
    # 2023_04_27-18_12_36,GHProjectData,initializing data object.| workflow name: Workflow: 2023_04_26-17_32_18-No Sprint Name-mn-snapshot_sprint_from_file
    # 2023_04_27-18_12_36,GHProjectData,initializing data object.| Destination: /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/results/2023_04_26-17_32_18-No Sprint Name-mn-snapshot_sprint_from_file-log.txt
    # 2023_04_27-18_12_36,GHProjectData,initializing data object.| workflow file name: mn-snapshot_sprint_from_file
    # 2023_04_27-18_12_36,GHProjectData,initializing data object.| source type file
    # 2023_04_27-18_12_36,DFFromFile,Created dataframe from file: /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk//2023_04_26-17_32_18-output.tsv.
    # 2023_04_27-18_12_36,SprintCardSizer,Added the size column. 
    # 2023_04_27-18_12_36,SprintSizeSummarizer,Summarize the sprint
    # ===================================================================================================================
    def __init__(self,
                 src_type: str,
                 workflow_name: str,
                 dest_dir_name: str,
                 collection_flag: str = None,
                 sprint_name: str = "no sprint name",
                 src_dir_name: str = None,
                 src_file_name: str = None,
                 data_collected_time: str = None,
                 organization_name: str = None,
                 project_name: str = None
                 ):
        self._df = None

        if collection_flag not in ["start", "snapshot", "end", "unknown"]:
            raise ValueError(f"Error: sprint_snap_status must be one of: 'start', 'snapshot', 'end', 'unknown'")

        if src_type not in ["file", "api"]:
            raise ValueError(f"Error: src_type: must be one of 'file', 'api', 'unknown'")

        self._v = {}
        self._v['organization_name'] = organization_name
        self._v['project_name'] = project_name
        self._v['snapshot_type'] = collection_flag
        self._v['this_run_time'] = pd.Timestamp.now().strftime("%Y%m%d%H%M%S")
        self._v['sprint_name'] = sprint_name
        self._v['in_dir'] = sanitize_filepath(src_dir_name, platform="auto")
        self._v['in_file'] = sanitize_filename(src_file_name, platform="auto")
        self._v['out_dir'] = sanitize_filepath(dest_dir_name, platform="auto")
        self._v['workflow_name'] = os.path.splitext(os.path.basename(workflow_name))[0]
        self._v['src_type'] = src_type

        self._v['data_collected_time'] = self._set_data_collection_time(data_collected_time)
        self._v['out_file'] = self._set_out_file_name()
        self._log = None
        self._initialize_log()

    def _set_out_file_name(self):
        f = \
            self._v['data_collected_time'] \
            + "-" + self._v['sprint_name'] \
            + "-" + self._v['snapshot_type'] \
            + "-" + self._v['workflow_name'] \
            + "-" + self._v['src_type'] \
            + "-" + self._v['this_run_time']
        f = sanitize_filename(f, platform="auto")
        f = f.replace(' ', '')
        f = f.replace(',', '')
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
        out_file = self._v['out_dir'] + '/' + self._v['out_file'] + "-log.tsv"
        print(f"Writing Log to:.")
        print(f" {out_file}")
        self._log.to_csv(out_file, sep='\t', index=False)

    def _set_data_collection_time(self, dct: str):
        # -------------------------------------------------------------------------------------------
        # "file","api", "unknown" - indicates the source of the data.
        #
        # the --src_file_name is assumed to start with a timestamp that marks the original date/time that it
        #  was collected using the API.
        # Here are a few examples.
        # - 2023_04_26-15_38_22-output.tsv
        # - 2023_04_26-153822-output.tsv
        # - 20230426_153822-output.tsv
        # -------------------------------------------------------------------------------------------
        # if source is a file, then assume the prefix of the file name is the date/time that the data was collected.
        if self._v['src_type'] == "file":
            if dct is None:
                regex1 = re.compile(r"(^[0-9_-]+)")
                return regex1.search(os.path.basename(self._v['in_file'])).group(0)
        elif self._v['src_type'] == "api":
            return datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        elif dct is None:
            return "data_collected_time_not_specified"
        return dct

    @property
    def this_run_time(self):
        return self._v['this_run_time']

    @property
    def dest_dir(self):
        return self._v['out_dir']

    @property
    def dest_file(self):
        return self._v['out_file']

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
                   + '/' + sanitize_filename(self._v['out_file'], platform="auto") \
                   + '-' \
                   + postfix \
                   + ".tsv"
        print(f"Saving result to file.")
        print(f" {out_file}")
        self._df.to_csv(out_file, sep='\t', index=False)

    def validate_metadata(self):
        # ===================================================================================================================
        # This validates the metadata for the data object.
        # ===================================================================================================================
        return True
