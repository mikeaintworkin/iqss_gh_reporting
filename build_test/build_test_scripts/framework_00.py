#!/usr/bin/env python3
from datetime import datetime
from iqss_gh_reporting import legacy as pdio
from iqss_gh_reporting import pdata as pdata
from iqss_gh_reporting import process_labels_util as plu
from iqss_gh_reporting import transformer as transformer
from iqss_gh_reporting import transformer as xfmr
from iqss_gh_reporting import utils as utils
from legacy import get_kickoff_issue
from pathvalidate import sanitize_filename
from pathvalidate import sanitize_filepath
import argparse
import os
import re
import yaml


def main():
    # ================================================================================================================
    # The objective of this frame is to work through the following steps:
    # - call the legacy API
    # - stop the code inside legacy.py at the point where it retrieves pull request
    #
    # This will run based on the contents of the yaml file.
    # use the pip installed version of the create_iq_snapshot_init running in the scripts directory via
    # test_frame_00.sh to setup  for the debug run.
    # ================================================================================================================
    print(f"Running {__file__} as the main program")
    print(f"Running {__file__} as the main program")
    yaml_file = os.path.expanduser(os.getcwd() + '/' + 'input_file.yaml')
    data = utils.read_yaml(yaml_file)
    if data is None:
        raise ValueError(f"Error: there must be a valid input.yaml file in the current working dir: {os.getcwd()}")

    with open(yaml_file) as file:
        ydata = yaml.load(file, Loader=yaml.FullLoader)
    yaml_string = yaml.dump(ydata, default_flow_style=False)
    print(f"input arguments:\n\n{yaml_string}")

    sprint_data = pdata.GHProjectData(
        src_type=ydata['src_type'],
        workflow_name=ydata['workflow_name'],
        sprint_name=ydata['sprint_name'],
        collection_flag=ydata['collection_flag'],
        src_dir_name=ydata['src_dir_name'],
        src_file_name=ydata['src_file_name'],
        dest_dir_name=sanitize_filepath(ydata['output_base_dir'] + '/' + data['sprint_name'], platform="auto"),
        organization_name=ydata['organization_name'],
        project_name=ydata['project_name']
    )
    # get OAUTH token
    auth_token_val = os.getenv('GITHUB_TOKEN', "novalue")
    if auth_token_val == "novalue":
        print("You must set the GITHUB_TOKEN environment variable to run with 'api' flag for this program")
        exit(1)

    sprint_data.df = pdio.LegacyProjectCards(
        access_token=auth_token_val,
        organization_name=sprint_data.organization_name,
        project_name=sprint_data.project_name).df


    sprint_data.write(postfix="orig")


if __name__ == "__main__":
    main()
