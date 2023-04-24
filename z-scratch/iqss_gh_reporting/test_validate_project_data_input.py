from unittest import TestCase
import pandas as pd
from iqss_gh_reporting.project_data_io import required_df_column_header_names_present

def test_valid_sprint_column_names_missing():
    required_sprint_column_names = ['Name', 'Status', 'Start Date', 'End Date']
    submitted_sprint_column_names = pd.Series(['Name', 'Status', 'End Date'])
    assert valid_sprint_column_names(required_sprint_column_names, submitted_sprint_column_names) == False


def test_valid_sprint_column_names_all_present():
    required_sprint_column_names = ['Name', 'Status', 'Start Date', 'End Date']
    submitted_sprint_column_names = pd.Series(['Name', 'Status', 'Start Date', 'End Date'])
    assert valid_sprint_column_names(required_sprint_column_names, submitted_sprint_column_names) == True


def test_valid_sprint_column_names_none_required():
    submitted_sprint_column_names = pd.Series(['Name', 'Status', 'Start Date', 'End Date'])
    assert valid_sprint_column_names(None, submitted_sprint_column_names) == True


def test_valid_sprint_column_names_none_submitted():
    required_sprint_column_names = ['Name', 'Status', 'Start Date', 'End Date']
    submitted_sprint_column_names = None
    assert valid_sprint_column_names(required_sprint_column_names, submitted_sprint_column_names) == False


def test_valid_sprint_column_names_empty_required():
    required_sprint_column_names = []
    submitted_sprint_column_names = pd.Series(['Name', 'Status', 'Start Date', 'End Date'])
    assert valid_sprint_column_names(required_sprint_column_names, submitted_sprint_column_names) == True


def test_valid_sprint_column_names_empty_submitted():
    required_sprint_column_names = ['Name', 'Status', 'Start Date', 'End Date']
    submitted_sprint_column_names = pd.Series([])
    assert valid_sprint_column_names(required_sprint_column_names, submitted_sprint_column_names) == False



