import argparse
import os

from iqss_gh_reporting import project_data_io as pdio

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
    parser = argparse.ArgumentParser(description='query related information')
    parser.add_argument('--org_name', dest='organization_name', default="IQSS", type=str, help='XXX')
    parser.add_argument('--proj_name', dest='proj_name', default="IQSS/dataverse", type=str, help='XXX')
    args = parser.parse_args()
    print(f" --org_name {args.organization_name}")
    print(f"--proj_name {args.proj_name}")

    # input:
    # get OAUTH token
    auth_token_val = os.getenv('GITHUB_TOKEN', "novalue")
    if auth_token_val == "novalue":
        print("You must set the GITHUB_TOKEN environment variable to run this program")
        exit(1)
    df = pdio.LegacyProjectCards(
        access_token=auth_token_val,
        organization_name=args.organization_name,
        project_name=args.proj_name)
    df.fetch_data()
    df.print_project_cards()
    pdio.write_dataframe(df=df.dataframe()) # raw data
    dfsum = pdio.SprintSummaryFrame(df_in=df.dataframe())