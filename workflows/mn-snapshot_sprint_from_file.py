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
    parser.add_argument('--file_name', dest='file_name', default="2023_04_24-18_53_30-output.tsv", type=str, help='XXX')
    parser.add_argument('--dir_name', dest='dir_name', \
                        default="/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk/", \
                        type=str, help='XXX')
    args = parser.parse_args()

    # input:
    # get OAUTH token
    auth_token_val = os.getenv('GITHUB_TOKEN', "novalue")
    if auth_token_val == "novalue":
        print("You must set the GITHUB_TOKEN environment variable to run this program")
        exit(1)


    df = pdio.DFFromFile(
        in_dir=args.dir_name,
        file_name=args.filename)
    dfsum = pdio.SprintSummaryFrame(df_in=df.dataframe())
