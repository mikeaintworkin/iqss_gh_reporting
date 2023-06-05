#!/usr/bin/env python3

# from datetime import datetime
# from pathvalidate import sanitize_filename
# from pathvalidate import sanitize_filepath
import argparse
import os
# import pandas as pd
# import re
# import yaml

#
# from iqss_gh_reporting import legacy as pdio
# from iqss_gh_reporting import pdata as pdata
# from iqss_gh_reporting import transformer as transformer
# from iqss_gh_reporting import transformer as xfmr
# from iqss_gh_reporting import utils as utils
# from iqss_gh_reporting import fetch_from_repository
from fetch_from_repository import GraphQLFetcher
import graphql_query_lib as iq_qry_lib


def arg_parse():
    parser = argparse.ArgumentParser(prog='', description='', epilog="")
    parser.add_argument('--loginOrg', dest='loginOrg', default="IQSS", type=str)
    parser.add_argument('--repo', dest='repo', default="dataverse", type=str)
    return parser.parse_args()


def main():
    # ================================================================================================================
    # The objective of this frame is to work through the following steps:
    # - read in a graphql file to find a pr and return its information
    # - prepare the python that does the querying and returns the results to be a library
    # ================================================================================================================
    print(f"Running {__file__} as the main program")
    args = {}
    args = arg_parse()
    # get OAUTH token
    key = 'GITHUB_TOKEN'
    auth_token_val = os.getenv(key, "novalue")

    functions = iq_qry_lib.queries
    query_dict = functions['query_get_all_prs']()
    print(query_dict)
    print(args.repo)
    query_dict['query_vars'] = {
        "loginOrg": args.loginOrg,
        "firstFew": 100,
        "repo": args.repo,
    }

    fetcher = GraphQLFetcher(auth_token_val, query_dict)
    fetcher.save_result_to_file()


if __name__ == "__main__":
    main()
