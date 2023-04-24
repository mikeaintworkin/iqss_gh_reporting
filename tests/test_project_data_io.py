import pytest
from unittest import TestCase
import pandas as pd
import os

from iqss_gh_reporting.project_data_io import list_contains_at_least
from iqss_gh_reporting.project_data_io import DFFromFile
from iqss_gh_reporting.project_data_io import GithubLegacyProjectCardsPandas


class RequiredDfColumnHeaderNamesPresent(TestCase):

    def list_contains_at_least_required_entries_names_missing(self):
        print(f">> start list_contains_at_least_required_entries_names_missing")
        required_sprint_column_names = ['Name', 'Status', 'Start Date', 'End Date']
        submitted_sprint_column_names = ['Name', 'Status', 'End Date']
        assert list_contains_at_least(required_sprint_column_names,
                                      submitted_sprint_column_names) is False

    def list_contains_at_least_required_entries_names_all_present(self):
        print(f">> start list_contains_at_least_required_entries_names_all_present")
        required_sprint_column_names = ['Name', 'Status', 'Start Date', 'End Date']
        submitted_sprint_column_names = ['Name', 'Status', 'Start Date', 'End Date']
        assert list_contains_at_least(required_sprint_column_names,
                                      submitted_sprint_column_names) is True

    def list_contains_at_least_required_entries_names_none_submitted(self):
        print(f">> start list_contains_at_least_required_entries_names_none_submitted")
        required_sprint_column_names = ['Name', 'Status', 'Start Date', 'End Date']
        submitted_sprint_column_names = None
        assert list_contains_at_least(required_sprint_column_names,
                                      submitted_sprint_column_names) is False

    def list_contains_at_least_required_entries_names_empty_submitted(self):
        print(f">> start list_contains_at_least_required_entries_names_empty_submitted")
        required_sprint_column_names = ['Name', 'Status', 'Start Date', 'End Date']
        submitted_sprint_column_names = []
        assert list_contains_at_least(required_sprint_column_names,
                                      submitted_sprint_column_names) is False

    def list_contains_at_least_required_entries_names_duplicate_submitted(self):
        print(f">> start list_contains_at_least_required_entries_names_duplicate_submitted")
        required_sprint_column_names = ['Name', 'Status', 'Start Date', 'End Date']
        submitted_sprint_column_names = ['Name', 'Status', 'Start Date', 'End Date', 'Start Date']
        assert list_contains_at_least(required_sprint_column_names,
                                      submitted_sprint_column_names) is False


class TestDFFromFile(TestCase):
    def test_DFFromFile_init_valid_file(self):
        print(">> start test_DFFromFile_init_valid_file")
        # Test case for valid input file
        in_dir = "/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/tests/wrk"
        file_name = "input_file.csv"
        df_file = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df_file.to_csv(os.path.join(in_dir, file_name), sep='\t', index=False)
        df_obj = DFFromFile(in_dir=in_dir, file_name=file_name)
        assert isinstance(df_obj.df, pd.DataFrame)
        assert df_obj.df.equals(df_file)
        print(">> end test_DFFromFile_init_valid_file")

    def test_DFFromFile_init_missing_file(self):
        print(">> start test_DFFromFile_init_missing_file")
        # Test case for missing input file
        df_obj = DFFromFile(in_dir="/path/to/input/dir", file_name="missing_file.csv")
        assert df_obj.df is None
        print(">> end test_DFFromFile_init_missing_file")

    def test_DFFromFile_init_missing_dir(self):
        print(">> start test_DFFromFile_init_missing_dir")
        # Test case for missing input directory
        df_obj = DFFromFile(in_dir="missing_dir", file_name="input_file.csv")
        assert df_obj.df is None
        print(">> end test_DFFromFile_init_missing_dir")

