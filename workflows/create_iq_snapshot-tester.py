#!/usr/bin/env python3

from datetime import datetime
from iqss_gh_reporting import legacy as pdio
from iqss_gh_reporting import pdata as ghpdata
from iqss_gh_reporting import transformer as transformer
from iqss_gh_reporting import transformer as xfmr
from iqss_gh_reporting import utils as utils
import argparse
import os
import re
import yaml
from legacy import get_kickoff_issue

def main():
    print(f"Running {__file__} as the main program")
    yaml_file = os.path.expanduser("~/iqss_gh_reporting/test/in" + '/' + 'input_file.yaml')
    with open(yaml_file) as file:
        ydata = yaml.load(file, Loader=yaml.FullLoader)
    parser = argparse.ArgumentParser(
        prog='create_iq_snapshot_init',
        description='run this at the beginning of the sprint to set the defaults for the sprint',
        epilog='<>')


    parser.add_argument('--sprint_name', dest='sprint_name', default=ydata['sprint_name'], type=str, help='XXX')
    parser.add_argument('--collection_flag', dest='collection_flag', default=ydata['collection_flag'], type=str, help='XXX')
    parser.add_argument('--collection_timestamp', dest='collection_timestamp', default=ydata['collection_timestamp'], type=str, help='XXX')
    parser.add_argument('--organization_name', dest='organization_name', default=ydata['api']['organization_name'], type=str, help='XXX')
    parser.add_argument('--project_name', dest='project_name', default=ydata['api']['project_name'], type=str, help='XXX')
    parser.add_argument('--src_file_name', dest='src_file_name', default=os.path.expanduser(ydata['file']['src_file_name']), type=str, help='XXX')
    parser.add_argument('--src_dir_name', dest='src_dir_name', default=os.path.expanduser(ydata['file']['src_dir_name']), type=str, help='XXX')
    parser.add_argument('--src_from', dest='src_type', default=ydata['src_type'], type=str, help='XXX')
    parser.add_argument('--src_orig_snapshot_file_name', dest='src_orig_snapshot_file_name', default=ydata['src_orig_snapshot_file_name'], type=str, help='XXX')
    args = parser.parse_args()
    # parser.print_help()
    args_dict = vars(args)
    yaml_string = yaml.dump(args_dict, default_flow_style=False)
    print(yaml_string)

    sprint_data = ghpdata.GHProjectData(
        src_type=args.src_type,
        workflow_name=os.path.basename(__file__),
        sprint_name=args.sprint_name,
        collection_flag=args.collection_flag,
        src_dir_name=args.src_dir_name,
        src_file_name=args.src_orig_snapshot_file_name,
        dest_dir_name=os.path.expanduser(ydata['dest_dir_name']),
        data_collected_time=args.collection_timestamp,
        organization_name=args.organization_name,
        project_name=args.project_name

    )
    # sprint_data.validate_metadata()
    sprint_end_data = ghpdata.GHProjectData(
        src_type=args.src_type,
        workflow_name=os.path.basename(__file__),
        sprint_name=args.sprint_name,
        collection_flag=args.collection_flag,
        src_dir_name=args.src_dir_name,
        src_file_name=args.src_file_name,
        dest_dir_name=os.path.expanduser(ydata['dest_dir_name']),
        data_collected_time=args.collection_timestamp,
        organization_name=args.organization_name,
        project_name=args.project_name

    )

    if args.src_type == "file":
        # read original sprint snapshot
        sprint_data.df = utils.read_dataframe_file(
            in_dir=args.src_dir_name,
            file_name=args.src_orig_snapshot_file_name
        )
        # read end of sprint data
        sprint_end_data.df = utils.read_dataframe_file(
            in_dir=args.src_dir_name,
            file_name=args.src_file_name
        )


    sprint_data.write(postfix="orig")
    # xfmrd_df = xfmr.SprintCardSizer(sprint_data).df
    # sprint_data.df = xfmrd_df
    # sprint_data.write(postfix="sized")
    # prs = transformer.PrPointsFetcher(sprint_data)
    # utils.write_dataframe(df=prs.df_zero_rows())
    # SprintSizeSummarizer creates a new dataframe so I need create a variable that I can reference to get the results
    # summarized_data = xfmr.SprintSizeSummarizer(sprint_data)
    # summarized_data.write("summary")

    get_kickoff_issue()
    xziser = xfmr.PRSizer(sp_data_sprint_snap=sprint_end_data, sp_data_sprint_orig=sprint_data)


if __name__ == "__main__":
    main()
