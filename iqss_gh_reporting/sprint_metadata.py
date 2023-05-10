from datetime import timedelta

# from argparse import ArgumentParser
# from dict2xml import dict2xml
# from argparse import ArgumentParser
from github import Github
# from gql import gql, Client
# from gql.transport.aiohttp import AIOHTTPTransport
# from json2xml import json2xml
from pathvalidate import sanitize_filename
from pathvalidate import sanitize_filepath
# from typing import Literal
# import argparse
# import asyncio
import datetime
# import json
import os
import pandas as pd
import re
import copy
from iqss_gh_reporting import pdata

"""
The purpose of this module is to provide a class that will validate metadata related to running a sprint report.
There are two types of metadata associated with the sprint report.
GitHub  metadata is used to control the data that is retrieved from GitHub.

Administrative metadata
------


Administrative metadata is used to control the execution of the sprint report.
This includes the sprint name, the sprint start date, the sprint end date, and the sprint duration.
api:
organization_name: IQSS
project_name: IQSS/dataverse
collection_flag: unknown
collection_timestamp: test
dest_dir_name: ~/iqss_gh_reporting/run/out
file:
src_dir_name: ~/iqss_gh_reporting/run/in
src_file_name: test.tsv
sprint_name: test
src_type: file

Also 
- The list of required dataframe column headers that must be presetn.


Ensure that some columns that will be needed later are present in the data frame.
 - Size
 - comments 
 - closingIssuesReferences


GitHub metadata
------

- The list of values in the dataframe header called "Column" that represent the states in the sprint.
- The values returned for the 
- labels must be a comma separated list of strings.





"""
\

src_file_name: test.tsv
sprint_name: test
