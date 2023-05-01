#!python

import argparse
import os
import argparse
import os
import re
from datetime import datetime
import yaml

from iqss_gh_reporting import legacy_project_cards as pdio
from iqss_gh_reporting import pdata as ghpdata
from iqss_gh_reporting import utils as utils
from iqss_gh_reporting import transformer as transformer


def main():
    # ===================================================================================================================
    # workflow
    #  - Query the legacy dataverse project API.
    #  - Write the results to a file
    #  - Write a summary of the column stats to a file and to the screen
    #
    # ===================================================================================================================
    #    input:
    #   output:
    #  precond:
    # postcond:  output will contain the data from the columns described in the precondition
    #  e.g.use:
    # --------------------------------------------------------------------------------------------------------------------
    print(f"Running {__file__} as the main program")
    yaml_file = os.path.expanduser("~/iqss_gh_reporting/run/in" + '/' + 'input_file.yaml')
    with open(yaml_file) as file:
        ydata = yaml.load(file, Loader=yaml.FullLoader)
    parser = argparse.ArgumentParser(
        prog='create_iq_snapshot_init_sprint.py',
        description='run this at the beginning of the sprint to set the defaults for the sprint',
        epilog='<>')


    parser.add_argument('--sprint_name', dest='sprint_name', default=ydata['any']['sprint_name'], type=str, help='XXX')
    parser.add_argument('--collection_flag', dest='collection_flag', default=ydata['any']['collection_flag'], type=str, help='XXX')
    parser.add_argument('--collection_timestamp', dest='collection_timestamp', default=ydata['any']['collection_timestamp'], type=str, help='XXX')
    parser.add_argument('--organization_name', dest='organization_name', default=ydata['api']['organization_name'], type=str, help='XXX')
    parser.add_argument('--project_name', dest='project_name', default=ydata['api']['project_name'], type=str, help='XXX')
    parser.add_argument('--src_file_name', dest='src_file_name', default=os.path.expanduser(ydata['file']['src_file_name']), type=str, help='XXX')
    parser.add_argument('--src_dir_name', dest='src_dir_name', default=os.path.expanduser(ydata['file']['src_dir_name']), type=str, help='XXX')
    args = parser.parse_args()
    # parser.print_help()
    args_dict = vars(args)
    yaml_string = yaml.dump(args_dict, default_flow_style=False)
    print(yaml_string)

    Summary_of_this_run = \
        "This workflow is used to summarize the size of the cards in a sprint.\n" \
        + " The input is the legacy project api. \n" \
        + " output file names are all synced so that it is obvious that they ran together.\n" \
        + " the original input \n" \
        + " the original  input modified with a size column\n" \
        + " A one line (2 including header) summary.\n" \
        + " 4/28/23 23:40 fixed a bug which was including Sprint Ready in ActiveSprint\n" \
        + " "
    with open(yaml_file) as file:
        ydata = yaml.load(file, Loader=yaml.FullLoader)
    parser = argparse.ArgumentParser(
        prog='create_iq_snapshot_init_sprint.py',
        description='run this at the beginning of the sprint to set the defaults for the sprint',
        epilog='<>')

    parser.add_argument('--sprint_name', dest='sprint_name', default=ydata['any']['sprint_name'], type=str, help='XXX')
    parser.add_argument('--collection_flag', dest='collection_flag', default=ydata['any']['collection_flag'], type=str, help='XXX')
    parser.add_argument('--collection_timestamp', dest='collection_timestamp', default=ydata['any']['collection_timestamp'], type=str, help='XXX')
    parser.add_argument('--organization_name', dest='organization_name', default=ydata['api']['organization_name'], type=str, help='XXX')
    parser.add_argument('--project_name', dest='project_name', default=ydata['api']['project_name'], type=str, help='XXX')
    parser.add_argument('--src_file_name', dest='src_file_name', default=os.path.expanduser(ydata['file']['src_file_name']), type=str, help='XXX')
    parser.add_argument('--src_dir_name', dest='src_dir_name', default=os.path.expanduser(ydata['file']['src_dir_name']), type=str, help='XXX')
    args = parser.parse_args()

    # identify where we are sourcing the data from
    src_type = "api"

    # input:
    # get OAUTH token
    auth_token_val = os.getenv('GITHUB_TOKEN', "novalue")
    if auth_token_val == "novalue":
        print("You must set the GITHUB_TOKEN environment variable to run this program")
        exit(1)

    sprint_data = ghpdata.GHProjectData(
        src_type=src_type,
        workflow_name=os.path.basename(__file__),
        sprint_name=args.sprint_name,
        collection_flag=args.collection_flag,
        dest_dir_name=ydata['any']['dest_dir_name'],
        data_collected_time=args.collection_timestamp,
        organization_name=args.organization_name,
        project_name=args.project_name
    )
    lpr = pdio.LegacyProjectCards(
        access_token=auth_token_val,
        organization_name=sprint_data.organization_name,
        project_name=sprint_data.project_name)
    sprint_data.df = lpr.df
    sprint_data.add_log_entry(context="utils", comment=Summary_of_this_run)
    sprint_data.write_log()

    utils.write_dataframe(df=sprint_data.df, out_dir=sprint_data.dest_dir, out_name=sprint_data.dest_file + "-orig")

    sprint_data.transform(transformer.SprintCardSizer())
    utils.write_dataframe(df=sprint_data.df, out_dir=sprint_data.dest_dir, out_name=sprint_data.dest_file + "-sized")

    # SprintSizeSummarizer creates a new dataframe, so I need create a variable that I can reference to get the results
    summarize = transformer.SprintSizeSummarizer(sprint_name=sprint_data.sprint_name,
                                                 timestamp=sprint_data.data_collected_time)
    sprint_data.transform(summarize)
    utils.write_dataframe(df=summarize.df_summary, out_dir=sprint_data.dest_dir,
                          out_name=sprint_data.dest_file + "-summary")


if __name__ == "__main__":
    main()
