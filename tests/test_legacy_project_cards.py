from unittest import mock
import pytest
from legacy import get_kickoff_issue
from datetime import datetime
from iqss_gh_reporting import legacy as pdio
from iqss_gh_reporting import pdata as ghpdata
from iqss_gh_reporting import transformer as transformer
from iqss_gh_reporting import transformer as xfmr
from iqss_gh_reporting import utils as utils
import argparse
import os
import re
import yaml

class TestGetKickoffIssue:

    def test_get_kickoff_issue(self):
        # arrange
        def test_get_kickoff_issue(number: str = "87", repo_owner:str = "IQSS",
                              repo: str = "dataverse",
                              access_token: str = "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"):
            return_value = get_kickoff_issue()
            print(return_value)

