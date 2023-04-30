import pytest
from unittest import TestCase
import pandas as pd
import os

from iqss_gh_reporting.legacy_project_cards import list_contains_at_least
from iqss_gh_reporting.legacy_project_cards import DFFromFile
from iqss_gh_reporting.legacy_project_cards import SprintSizeSummarizer
from iqss_gh_reporting.legacy_project_cards import RequiredSprintColumnValues
from iqss_gh_reporting.legacy_project_cards import SprintCardSizer
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


class TestRequiredSprintColumnValues:

    def test_list(self):
        names = RequiredSprintColumnValues.list()
        assert isinstance(names, list)
        assert len(names) == 4
        assert "This Sprint 🏃‍♀️ 🏃" in names
        assert "IQSS Team - In Progress  💻" in names
        assert "Ready for Review ⏩" in names
        assert "In Review 🔎" in names

    def test_print(self, capsys):
        RequiredSprintColumnValues.print()
        captured = capsys.readouterr()
        assert captured.out.strip() == "values: ['This Sprint 🏃\\u200d♀️ 🏃', 'IQSS Team - In Progress  💻', 'Ready for Review ⏩', 'In Review 🔎']"


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


class TestSprintSizeSummarizer:

    def test_init_with_none(self):
         with pytest.raises(TypeError):
             sss = SprintSizeSummarizer(None)

    def test_init_with_empty_df(self):
        df = pd.DataFrame(columns=["column", "size"])
        sss = SprintSizeSummarizer(df)
        assert sss.df_summary.empty

    def test_init_with_invalid_df(self):
        df = pd.DataFrame(columns=["invalid_column"])
        df.loc[0, "invalid_column"] = "value"
        with pytest.raises(ValueError):
            sss = SprintSizeSummarizer(df)

    def test_init_with_valid_df(self):
        df = pd.DataFrame({
            "column": ["To Do", "In Progress", "Done"],
            "size": [5, 3, 2]
        })
        sss = SprintSizeSummarizer(df)
        assert not sss.df_summary.empty

    def test_sprint_summary(self):
        # "project": "Project",
        # "column": "Column",
        # "type": "Type",
        # "number": "Number",
        # "labels": "Labels",
        # "repo": "Repo",
        # "state": "State",
        df = pd.DataFrame({
            "Column": ["This Sprint 🏃‍♀️ 🏃", "IQSS Team - In Progress  💻", "Ready for Review ⏩","In Review 🔎"],
            "Size": [5, 3, 2,20],
            "Project": ["Project 1", "Project 2", "Project 3", "Project 4"],
            "Number": [1, 2, 3, 4],
            "Labels": ["Size: 1", "Label 2", "Label 3", "Label 4"],
            "Repo": ["Repo 1", "Repo 2", "Repo 3", "Repo 4"],
            "State": ["State 1", "State 2", "State 3", "State 4"],
            "Type": ["State 1", "State 2", "State 3", "State 4"]

        })
        sss = SprintSizeSummarizer(df)
        summary = sss.sprint_summary()
        assert isinstance(summary, pd.DataFrame)
        assert len(summary) == 5         # includes ActiveSprint row

    # def test_sprint_summary_line(self):
    #     df = pd.DataFrame({
    #         "column": ["To Do", "In Progress", "Done"],
    #         "size": [5, 3, 2]
    #     })
    #     sss = SprintSizeSummarizer(df)
    #     summary_line = sss.sprint_summary_line("2023-04-25", "Sprint 1")
    #     assert isinstance(summary_line, str)
    #     assert "2023-04-25" in summary_line
    #     assert "Sprint 1" in summary_line




class TestSprintCardSizer:
    def test_init_with_invalid_input(self):
        with pytest.raises(TypeError):
            sizer = SprintCardSizer("not a dataframe")

    def test_init_with_none(self):
         with pytest.raises(TypeError):
             sss = SprintCardSizer(None)


    def test_init_with_invalid_df(self):
        df = pd.DataFrame(columns=["invalid_column"])
        df.loc[0, "invalid_column"] = "value"
        with pytest.raises(ValueError):
            sss = SprintSizeSummarizer(df)

    def test_init_with_empty_dataframe(self):
        df = pd.DataFrame(columns=["number", "column", "labels"])
        sizer = SprintCardSizer(df)
        assert sizer._SprintCardSizer__df.empty

    def test_init_with_invalid_headers(self):
        df = pd.DataFrame(columns=["invalid_column"])
        df.loc[0, "invalid_column"] = "value"
        with pytest.raises(ValueError):
            sizer = SprintCardSizer(df)


    def test_init_with_invalid_sprint_values(self):
        # valid headers, invalid sprint values
        # valid: "Column": ["This Sprint 🏃‍♀️ 🏃", "IQSS Team - In Progress  💻", "Ready for Review ⏩","In Review 🔎"],
        df = pd.DataFrame({
            "Column": ["This Sprint 🏃‍♀️ 🏃", "IQSS Team - In Progress  💻", "Ready for Review ⏩", "In ReviewXXX 🔎"],
            "Size": [5, 3, 2,20],
            "Project": ["Project 1", "Project 2", "Project 3", "Project 4"],
            "Number": [1, 2, 3, 4],
            "Labels": ["Size: 1", "Label 2", "Label 3", "Label 4"],
            "Repo": ["Repo 1", "Repo 2", "Repo 3", "Repo 4"],
            "State": ["State 1", "State 2", "State 3", "State 4"],
            "Type": ["State 1", "State 2", "State 3", "State 4"]

        })
        with pytest.raises(ValueError):
            sizer = SprintCardSizer(df)


    def test_add_size_column_to_dataframe(self):
        df = pd.DataFrame(columns=["number", "column", "labels"])
        df.loc[0] = [1, "This Sprint 🏃‍♀️ 🏃", "Size: 5, Other Label"]
        sizer = SprintCardSizer(df)
        sizer._add_size_column()
        assert "size" in sizer._SprintCardSizer__df.columns
        assert sizer._SprintCardSizer__df["size"][0] == 5

    def test_add_size_column_to_dataframe_with_existing_column(self):
        df = pd.DataFrame(columns=["number", "column", "labels", "size"])
        df.loc[0] = [1, "This Sprint 🏃‍♀️ 🏃", "Size: 5, Other Label", 0]
        sizer = SprintCardSizer(df)
        sizer._add_size_column()
        assert sizer._SprintCardSizer__df["size"][0] == 0
        assert "Size column already exists" in capsys.readouterr().out

