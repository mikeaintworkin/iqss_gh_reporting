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


def write_dataframe(df: pd.DataFrame = None,
                    comments: str = "",
                    out_dir: str = '/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk',
                    out_name: str = 'output'):
    # ===================================================================================================================
    # This writes the contents of a dataframe to a tab delimited file.
    # ===================================================================================================================
    out_file = sanitize_filepath(out_dir, platform="auto") + '/' + sanitize_filename(out_name, platform="auto") + ".tsv"
    print(f"Saving result to file.")
    print(f" {out_file}")
    df.to_csv(out_file, sep='\t', index=False)

def print_dataframe(df: pd.DataFrame = None):
    # ===================================================================================================================
    # This prints the contents of a dataframe to the console.
    # ===================================================================================================================
    print(df.to_csv(sep='\t', index=False))


def read_dataframe_file(in_dir: str = None, file_name: str = None):
    # ===================================================================================================================
    # This reads a previously collected set of sprint data from a file.
    # no validation is done on the file contents.
    # ===================================================================================================================
    print(" Reading in data from a file.")
    print(f" input file directory: {in_dir}, input file name: {file_name}")
    input_file = in_dir + '/' + file_name
    print(f" input_file: {input_file}")

    # there's a library I can use to do this.  I'll do it later.
    if (file_name is None) or (in_dir is None) or (not os.path.isdir(in_dir)):
        print("Attempt to read input from file. No valid initialization data.  Exiting.")
    else:
        return pd.read_csv(input_file, sep='\t')

