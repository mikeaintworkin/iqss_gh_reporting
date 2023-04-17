import os
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import asyncio

import os
import json
import argparse
from json2xml import json2xml
from dict2xml import dict2xml
import utils

# Main
# Get all the items
#   input: I need these to initialize the query: access_token, organization_name, repo_name
#
#
#
#  output:
#  prereq: vars_in and query_str are closely related and are assumed to be correct.
# postreq:
#   descr:
#
#
if __name__ == "__main__":
    print(f"Running {__file__} as the main program")

    # input:
    # get the command line arguments:
    parser = argparse.ArgumentParser(description='query related information')
    parser.add_argument('--out_dir', dest='out_dir', default='/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk/', type=str, help='Name of the query file')
    parser.add_argument('--org_name', dest='organization_name', default="IQSS", type=str, help='XXX')
    # parser.add_argument('--org_name', dest='organization_name', default="HMDC", type=str, help='XXX')
    parser.add_argument('--proj_name', dest='proj_name', default="OdumInstitute", type=str, help='XXX')
    args = parser.parse_args()

    # get OAUTH token
    key = 'GITHUB_TOKEN'
    auth_token_val = os.getenv(key, "novalue")


    # vars_in = {"loginOrg": args.organization_name, "firstFew": 100, "repo": args.repo_name}
    github_project_cards = utils.GithubProjectCards(
        access_token=auth_token_val,
        organization_name=args.organization_name,
        project_name=args.proj_name,
        out_dir=args.out_dir
    )

    github_project_cards.get_project_cards()
    github_project_cards.print_project_cards()
    github_project_cards.save_project_cards()
