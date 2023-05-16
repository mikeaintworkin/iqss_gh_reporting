#!/usr/bin/env python3

from datetime import datetime
from iqss_gh_reporting import legacy as pdio
from iqss_gh_reporting import pdata as pdata
from iqss_gh_reporting import transformer as transformer
from iqss_gh_reporting import transformer as xfmr
from iqss_gh_reporting import utils as utils
from pathvalidate import sanitize_filename
from pathvalidate import sanitize_filepath
from fetch_from_repository import GraphQLFetcher
import graphql_query_lib as iq_qry_lib
from graphql import parse
import argparse
import os
import pandas as pd
import re
import yaml

def main():
    # ================================================================================================================
    # The objective of this frame is to work through the following steps:
    # - read in a graphql file to find a pr and return its information
    # - prepare the python that does the querying and returns the results to be a library
    # ================================================================================================================
   print(f"Running {__file__} as the main program")
    # get OAUTH token
    key = 'GITHUB_TOKEN'
    auth_token_val = os.getenv(key, "novalue")
    query_dict = iq_qry_lib.query_get_all_prs()
    query_dict['query_vars'] = {
        "loginOrg": "IQSS",
        "firstFew": 100,
        "repo": "dataverse",
    }

    fetcher = GraphQLFetcher(auth_token_val, query_dict)
    fetcher.save_result_to_file()

if __name__ == "__main__":
    main()
