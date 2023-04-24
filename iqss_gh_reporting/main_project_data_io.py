import argparse
import os

from project_data_io import LegacyProjectCards, WriteDf

if __name__ == "__main__":
    print(f"Running {__file__} as the main program")
    parser = argparse.ArgumentParser(description='query related information')
    parser.add_argument('--org_name', dest='organization_name', default="IQSS", type=str, help='XXX')
    parser.add_argument('--proj_name', dest='proj_name', default="IQSS/dataverse", type=str, help='XXX')
    args = parser.parse_args()
    print(f" --org_name {args.organization_name}")
    print(f"--proj_name {args.proj_name}")

    # input:
    # get OAUTH token
    key = 'GITHUB_TOKEN'
    auth_token_val = os.getenv(key, "novalue")
    df = LegacyProjectCards(
        access_token=auth_token_val,
        organization_name=args.organization_name,
        project_name=args.proj_name)
    #df.fetch_data()
    df.print_project_cards()
    newdf = df.get_dataframe_copy()
    WriteDf(df=df.dataframe())

# from pathvalidate.argparse import validate_filename_arg, validate_filepath_arg,  sanitize_filename_arg, sanitize_filepath_arg



    # # input:
    # # get the command line arguments:
    # # prereq: give every argument a default value
    # parser = argparse.ArgumentParser(description='query related information')
    # parser.add_argument('--in_dir', dest='in_dir', default='/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk', type=validate_filepath_arg)
    # parser.add_argument('--file_name', dest='file', default='input.tsv', type=validate_filename_arg)
    # args = parser.parse_args()
    #
    # df = DFFromFile(in_dir=args.in_dir, file_name=args.file)
