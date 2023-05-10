#!/usr/bin/env python3

import argparse
import os
import re
from datetime import datetime
import yaml

from iqss_gh_reporting import legacy_project_cards as pdio
from iqss_gh_reporting import pdata as ghpdata
from iqss_gh_reporting import utils as utils
from iqss_gh_reporting import transformer as xfmr

def main():
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

    # set workflow specific variables
    summary_of_this_run = '''
        This workflow is used to summarize the size of the cards in a sprint.
        The input is a file that was retrieved from the API. 
        output file names are all synced so that it is obvious that they ran together.
        - the original input 
        - the original  input modified with a size column
        - A one line (2 including header) summary.
        - 4/28/23 23:40 fixed a bug which was including Sprint Ready in ActiveSprint
        '''


    # identify where we are sourcing the data from
    # This is meant to be hardcoded here
    src_type = "file"

    sprint_data = ghpdata.GHProjectData(
        src_type=src_type,
        workflow_name=os.path.basename(__file__),
        sprint_name=args.sprint_name,
        collection_flag=args.collection_flag,
        src_dir_name=args.src_dir_name,
        src_file_name=args.src_file_name,
        dest_dir_name=os.path.expanduser(ydata['any']['dest_dir_name']),
        data_collected_time=args.collection_timestamp
        )
    sprint_data.df = utils.read_dataframe_file(
        in_dir=args.src_dir_name,
        file_name=args.src_file_name
        )
    sprint_data.add_log_entry(context="utils", comment=summary_of_this_run)
    sprint_data.write_log()

    utils.write_dataframe(df=sprint_data.df, out_dir=sprint_data.dest_dir, out_name=sprint_data.dest_file + "-orig")

    xfmrd_df = xfmr.SprintCardSizer(sprint_data).df
    utils.write_dataframe(df=xfmrd_df, out_dir=sprint_data.dest_dir, out_name=sprint_data.dest_file + "-sized")

    sprint_data.df = xfmrd_df

    # SprintSizeSummarizer creates a new dataframe so I need create a variable that I can reference to get the results
    summarized_df = xfmr.SprintSizeSummarizer(sprint_data).df_summary
    utils.write_dataframe(df=summarized_df, out_dir=sprint_data.dest_dir, out_name=sprint_data.dest_file + "-summary")


if __name__ == "__main__":
    main()
