#!/usr/bin/env python3

from datetime import datetime
# from pathvalidate import sanitize_filename
# from pathvalidate import sanitize_filepath
import argparse
import os
import json
# import pandas as pd
# import re
# import yaml

#
# from iqss_gh_reporting import legacy as pdio
# from iqss_gh_reporting import pdata as pdata
# from iqss_gh_reporting import transformer as transformer
# from iqss_gh_reporting import transformer as xfmr
# from iqss_gh_reporting import utils as utils
from iqss_gh_reporting import fetch_from_repository
# from fetch_from_repository import GraphQLFetcher
from iqss_gh_reporting import graphql_query_lib as iq_qry_lib


def arg_parse():
    parser = argparse.ArgumentParser(prog='', description='', epilog="")
    parser.add_argument('--loginOrg', dest='loginOrg', default="IQSS", type=str)
    parser.add_argument('--repo', dest='repo', default="dataverse", type=str)
    parser.add_argument('--output_dir', dest='output_dir', default="/tmp", type=str)
    parser.add_argument('--number', dest='number', default="9409", type=int)
    parser.add_argument('--output_file_name', dest='output_file_name', default=datetime.now().strftime("%Y%m%d-%H%M%S"), type=str)
    parser.add_argument('--query_key', dest='query_key', default="query_get_all_prs", type=str)
    return parser.parse_args()

def parse_issues_closed_by_pr(query_dict, pr_dict):
    # ================================================================================================================
    # This function takes the dictionary that is returned by the query_get_one_pr query and returns a list of issues
    # that are closed by the pr.
    #
    # ================================================================================================================
    print(f"parse_issues_closed_by_pr: {pr_dict['repository']['pullRequest']['closingIssuesReferences']['nodes'][0]}")
    print(f"parse_issues_closed_by_pr: {pr_dict['repository']['pullRequest']['closingIssuesReferences']['nodes'][0]['repository']['name']}")
    print(f"parse_issues_closed_by_pr: {pr_dict['repository']['pullRequest']['closingIssuesReferences']['nodes'][0]['title']}")
    print(f"parse_issues_closed_by_pr: {pr_dict['repository']['pullRequest']['closingIssuesReferences']['nodes'][0]['number']}")
    print(f"parse_issues_closed_by_pr: {pr_dict['repository']['pullRequest']['closingIssuesReferences']['nodes'][0]['id']}")
    print(f"parse_issues_closed_by_pr: {pr_dict['repository']['pullRequest']['closingIssuesReferences']['nodes'][0]['url']}")
    print(f"parse_issues_closed_by_pr: {pr_dict['repository']['pullRequest']['closingIssuesReferences']['nodes'][0]['closed']}")
    print(f"parse_issues_closed_by_pr: {pr_dict['repository']['pullRequest']['closingIssuesReferences']['nodes'][0]['closedAt']}")
    print(f"parse_issues_closed_by_pr: {pr_dict['repository']['pullRequest']['closingIssuesReferences']['nodes'][0]['labels']['nodes'][0]['name']}")





def main():
    # ================================================================================================================
    # The objective of this frame is to work through the following steps:
    # - read in a graphql file to find a pr and return its information
    # - prepare the python that does the querying and returns the results to be a library
    # ================================================================================================================
    print(f"Running {__file__} as the main program")
    args = arg_parse()

    # get OAUTH token
    # Don't forget to export the token as an environment variable
    key = 'GITHUB_TOKEN'
    auth_token_val = os.getenv(key, "novalue")

    query_dict = (iq_qry_lib.queries[args.query_key]())
    # query_dict = functions
    # print(args.repo)
    query_dict['query_vars'] = {
        "loginOrg": args.loginOrg,
        "firstFew": 100,
        "repo": args.repo,
        "number": args.number
    }
    #print(f" Query dictionary")
    #print(f" ---- \n {json.dumps(query_dict, indent=4)} \n ----  \n")

    fetcher = fetch_from_repository.GraphQLFetcher(auth_token_val, query_dict)
    fetcher.print_results()
    fetcher.save_result_to_file(file_path=args.output_dir, output_file_name=args.output_file_name + ".json")

    parse_issues_closed_by_pr(query_dict,fetcher.dict)

if __name__ == "__main__":
    main()
