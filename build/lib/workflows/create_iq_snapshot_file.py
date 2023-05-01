import argparse
import os
import re
from datetime import datetime

from iqss_gh_reporting import legacy_project_cards as pdio
from iqss_gh_reporting import pdata as ghpdata
from iqss_gh_reporting import utils as utils
from iqss_gh_reporting import transformer as transformer

def main():
    print(f"Running {__file__} as the main program")

    # set workflow specific variables
    Summary_of_this_run = \
        "This workflow is used to summarize the size of the cards in a sprint.\n" \
        + " The input is a file that was retrieved from the API. \n" \
        + " output file names are all synced so that it is obvious that they ran together.\n" \
        + " the original input \n" \
        + " the original  input modified with a size column\n" \
        + " A one line (2 including header) summary.\n" \
        + " 4/28/23 23:40 fixed a bug which was including Sprint Ready in ActiveSprint\n" \
        + " "


    # set workflow specific variables for defaults for arg parser
    d_src_file_name = "2023_04_26-17_32_18-output.tsv"
    d_src_dir_name = "/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk/"
    d_dest_dir_name = "/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk/"
    d_sprint_name = "No Sprint Name"
    d_collection_timestamp = "undefined"
    d_collection_flag = "unknown"

    d_sprint_name = "April 12, 2023"
    d_collection_flag = "start"
    d_src_file_name = "2023_04_12-sprint-20230412-1632-02.csv"
    d_src_dir_name ="/home/perftest/DevCode/github-com-mreekie/GitHubProjects/wustep-github-project-exporter/output"
    d_collection_timestamp = "20230412-1632"

    d_sprint_name = "April 12, 2023"
    d_collection_flag = "end"
    d_src_file_name = "2023_04_26-11_21_13-output-final_sprint_snapshot-00.tsv"
    d_src_dir_name ="/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk/"
    d_collection_timestamp = "2023_04_26-11_21_13"


    d_sprint_name = "April 26, 2023"
    d_collection_flag = "start"
    d_src_file_name = "2023_04_26-15_38_22-output.tsv"
    d_src_dir_name ="/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk/"
    d_collection_timestamp = "2023_04_26-15_38_22"


    # identify where we are sourcing the data from
    src_type = "file"

    parser = argparse.ArgumentParser(description=' information')
    parser.add_argument('--sprint_name', dest='sprint_name', default=d_sprint_name, type=str, help='XXX')
    parser.add_argument('--dest_dir_name', dest='dest_dir_name', default=d_dest_dir_name,type=str, help='XXX')
    parser.add_argument('--data_time_collected', dest='collection_timestamp', default=None,type=str, help='XXX')
    parser.add_argument('--collection_flag', dest='collection_flag', default=d_collection_flag,type=str, help='XXX')
    parser.add_argument('--src_file_name', dest='src_file_name', default=d_src_file_name, type=str, help='XXX')
    parser.add_argument('--src_dir_name', dest='src_dir_name', default=d_src_dir_name,type=str, help='XXX')
    args = parser.parse_args()

    sprint_data = ghpdata.GHProjectData(
                                        src_type=src_type,
                                        workflow_name=os.path.basename(__file__),
                                        sprint_name=args.sprint_name,
                                        collection_flag=args.collection_flag,
                                        src_dir_name=args.src_dir_name,
                                        src_file_name=args.src_file_name,
                                        dest_dir_name=args.dest_dir_name,
                                        data_collected_time=args.collection_timestamp
                                        )
    sprint_data.df = utils.read_dataframe_file(in_dir=args.src_dir_name, file_name=args.src_file_name)
    sprint_data.add_log_entry(context="utils", comment=Summary_of_this_run)
    sprint_data.write_log()

    utils.write_dataframe(df=sprint_data.df, out_dir=sprint_data.dest_dir, out_name=sprint_data.dest_file + "-orig")

    sprint_data.transform(transformer.SprintCardSizer())
    utils.write_dataframe(df=sprint_data.df, out_dir=sprint_data.dest_dir, out_name=sprint_data.dest_file + "-sized")

    # SprintSizeSummarizer creates a new dataframe so I need create a variable that I can reference to get the results
    summarize = transformer.SprintSizeSummarizer(sprint_name=sprint_data.sprint_name, timestamp=sprint_data.data_collected_time)
    sprint_data.transform(summarize)
    utils.write_dataframe(df=summarize.df_summary, out_dir=sprint_data.dest_dir, out_name=sprint_data.dest_file + "-summary")

