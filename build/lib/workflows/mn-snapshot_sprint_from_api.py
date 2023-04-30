import argparse
import os
import argparse
import os
import re
from datetime import datetime

from iqss_gh_reporting import legacy_project_cards as pdio
from iqss_gh_reporting import pdata as ghpdata
from iqss_gh_reporting import utils as utils
from iqss_gh_reporting import transformer as transformer


if __name__ == "__main__":
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
    # set workflow specific variables
    Summary_of_this_run = \
        "This workflow is used to summarize the size of the cards in a sprint.\n" \
        + " The input is the legacy project api. \n" \
        + " output file names are all synced so that it is obvious that they ran together.\n" \
        + " the original input \n" \
        + " the original  input modified with a size column\n" \
        + " A one line (2 including header) summary.\n" \
        + " 4/28/23 23:40 fixed a bug which was including Sprint Ready in ActiveSprint\n" \
        + " "

    # set workflow specific variables for defaults for arg parser
    d_sprint_name = "April 26, 2023"
    d_collection_flag = "snapshot"
    d_org_name = "IQSS"
    d_proj_name = "IQSS/dataverse"
    d_dest_dir_name = "/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk/"
    d_collection_timestamp = None




    # identify where we are sourcing the data from
    src_type = "api"

    parser = argparse.ArgumentParser(description=' information')
    parser.add_argument('--org_name', dest='organization_name', default=d_org_name, type=str, help='XXX')
    parser.add_argument('--proj_name', dest='proj_name', default=d_proj_name, type=str, help='XXX')

    parser.add_argument('--sprint_name', dest='sprint_name', default=d_sprint_name, type=str, help='XXX')
    parser.add_argument('--dest_dir_name', dest='dest_dir_name', default=d_dest_dir_name,type=str, help='XXX')
    parser.add_argument('--data_time_collected', dest='collection_timestamp', default=None,type=str, help='XXX')
    parser.add_argument('--collection_flag', dest='collection_flag', default=d_collection_flag,type=str, help='XXX')
    args = parser.parse_args()

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
        dest_dir_name=args.dest_dir_name,
        data_collected_time=args.collection_timestamp,
        organization_name=args.organization_name,
        project_name=args.proj_name
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
