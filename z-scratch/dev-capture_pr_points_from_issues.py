import argparse
import os

from iqss_gh_reporting import legacy as pdio

if __name__ == "__main__":
    # ===================================================================================================================
    # workflow
    #  - I am creating the class that will process pull requests that were created from issues that have points
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
    parser.add_argument('--file_name', dest='file_name', default="2023_04_26-11_21_13-output-final_sprint_snapshot-test_data.tsv", type=str, help='XXX')
    parser.add_argument('--dir_name', dest='dir_name', \
                        default="/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk/", \
                        type=str, help='XXX')
    args = parser.parse_args()

    dfff = pdio.DFFromFile(
        in_dir=args.dir_name,
        file_name=args.file_name)
    dfSzer = pdio.SprintCardSizer(df_in=dfff.dataframe())
    pdio.write_dataframe(dfSzer.dataframe())
    spsumrzr = pdio.SprintSizeSummarizer(df_in=dfSzer.dataframe())
    print(spsumrzr.sprint_summary_line())

