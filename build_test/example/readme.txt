barry@ubuntux64:~/PycharmProjects/iqss_gh_reporting/build_test/example$ ./build_and_run_example.sh

<info>
file: ./build_and_run_example.sh
pwd: /home/barry/PycharmProjects/iqss_gh_reporting/build_test/example
</info>

<msg>

Section: build the project to create new commands

./build_and_run_example.sh assumes that the directory it is running in is one level below in the directory heirarchy
from build_and_deploy_local.sh

e.g. pwd=./iqss_gh_reporting/build_test/build_test_scripts
e.g. pwd=./iqss_gh_reporting/build_test/example


build_and_deploy_local.sh will be (must be) run from the build_test directory
</msg>
++ press <enter> to continue ++


<info>
file: ./build_and_run_example.sh
pwd: /home/barry/PycharmProjects/iqss_gh_reporting/build_test/example
</info>

<msg>
Successfully Verified existence of the build script: /home/barry/PycharmProjects/iqss_gh_reporting/build_test/example/../build_and_deploy_local.sh
</msg>
++ press <enter> to continue ++

~/PycharmProjects/iqss_gh_reporting/build_test ~/PycharmProjects/iqss_gh_reporting/build_test/example

<info>
file: ./build_and_deploy_local.sh
pwd: /home/barry/PycharmProjects/iqss_gh_reporting/build_test
</info>

<msg>

The script is going to to build the sources and then deploy it with pip

This script MUST be run from the ./build_test directory in the project tree.
e.g ./PycharmProjects/iqss_gh_reporting/build_test
where ~/PycharmProjects/iqss_gh_reporting is the root of the project

e.g. We are looking for ../setup.py
</msg>
++ press <enter> to continue ++


<info>
file: ./build_and_deploy_local.sh
pwd: /home/barry/PycharmProjects/iqss_gh_reporting/build_test
</info>

<msg>
Successfully Verified existence of the build script: ../setup.py
</msg>
++ press <enter> to continue ++

~/PycharmProjects/iqss_gh_reporting ~/PycharmProjects/iqss_gh_reporting/build_test

<info>
file: ./build_and_deploy_local.sh
pwd: /home/barry/PycharmProjects/iqss_gh_reporting
</info>

<msg>
Begin Building...
</msg>
++ press <enter> to continue ++

running bdist_wheel
running build
running build_py
running build_scripts
copying and adjusting workflows/create_iq_snapshot_init -> build/scripts-3.10
copying and adjusting workflows/create_iq_snapshot -> build/scripts-3.10
copying and adjusting workflows/process_labels -> build/scripts-3.10
copying and adjusting workflows/run_a_gql_query -> build/scripts-3.10
/usr/lib/python3/dist-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
warnings.warn(
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64/wheel
creating build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/__init__.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/process_labels_util.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/sprint_metadata.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/fetch_from_repository.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/legacy.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/graphql_query_lib.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/graphql_query_exec.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/pdata.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/utils.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/transformer.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/fetch_from_repository_library.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
running install_egg_info
running egg_info
writing iqss_gh_reporting.egg-info/PKG-INFO
writing dependency_links to iqss_gh_reporting.egg-info/dependency_links.txt
writing requirements to iqss_gh_reporting.egg-info/requires.txt
writing top-level names to iqss_gh_reporting.egg-info/top_level.txt
reading manifest file 'iqss_gh_reporting.egg-info/SOURCES.txt'
adding license file 'LICENSE.txt'
writing manifest file 'iqss_gh_reporting.egg-info/SOURCES.txt'
Copying iqss_gh_reporting.egg-info to build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.5.egg-info
running install_scripts
creating build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.5.data
creating build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.5.data/scripts
copying build/scripts-3.10/create_iq_snapshot -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.5.data/scripts
copying build/scripts-3.10/create_iq_snapshot_init -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.5.data/scripts
copying build/scripts-3.10/process_labels -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.5.data/scripts
copying build/scripts-3.10/run_a_gql_query -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.5.data/scripts
changing mode of build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.5.data/scripts/create_iq_snapshot to 775
changing mode of build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.5.data/scripts/create_iq_snapshot_init to 775
changing mode of build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.5.data/scripts/process_labels to 775
changing mode of build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.5.data/scripts/run_a_gql_query to 775
adding license file "LICENSE.txt" (matched pattern "LICEN[CS]E*")
creating build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.5.dist-info/WHEEL
creating 'dist/iqss_gh_reporting-0.5-py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
adding 'iqss_gh_reporting/__init__.py'
adding 'iqss_gh_reporting/fetch_from_repository.py'
adding 'iqss_gh_reporting/fetch_from_repository_library.py'
adding 'iqss_gh_reporting/graphql_query_exec.py'
adding 'iqss_gh_reporting/graphql_query_lib.py'
adding 'iqss_gh_reporting/legacy.py'
adding 'iqss_gh_reporting/pdata.py'
adding 'iqss_gh_reporting/process_labels_util.py'
adding 'iqss_gh_reporting/sprint_metadata.py'
adding 'iqss_gh_reporting/transformer.py'
adding 'iqss_gh_reporting/utils.py'
adding 'iqss_gh_reporting-0.5.data/scripts/create_iq_snapshot'
adding 'iqss_gh_reporting-0.5.data/scripts/create_iq_snapshot_init'
adding 'iqss_gh_reporting-0.5.data/scripts/process_labels'
adding 'iqss_gh_reporting-0.5.data/scripts/run_a_gql_query'
adding 'iqss_gh_reporting-0.5.dist-info/LICENSE.txt'
adding 'iqss_gh_reporting-0.5.dist-info/METADATA'
adding 'iqss_gh_reporting-0.5.dist-info/WHEEL'
adding 'iqss_gh_reporting-0.5.dist-info/top_level.txt'
adding 'iqss_gh_reporting-0.5.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel

<info>
file: ./build_and_deploy_local.sh
pwd: /home/barry/PycharmProjects/iqss_gh_reporting
</info>

<msg>
Begin Installing...
</msg>
++ press <enter> to continue ++

Defaulting to user installation because normal site-packages is not writeable
Processing /home/barry/PycharmProjects/iqss_gh_reporting
Preparing metadata (setup.py) ... done
Requirement already satisfied: PyGithub in /home/barry/.local/lib/python3.10/site-packages (from iqss-gh-reporting==0.5) (1.58.2)
Requirement already satisfied: aiohttp in /home/barry/.local/lib/python3.10/site-packages (from iqss-gh-reporting==0.5) (3.8.4)
Requirement already satisfied: gql in /home/barry/.local/lib/python3.10/site-packages (from iqss-gh-reporting==0.5) (3.4.1)
Requirement already satisfied: graphql-py in /home/barry/.local/lib/python3.10/site-packages (from iqss-gh-reporting==0.5) (0.8.1)
Requirement already satisfied: numpy in /home/barry/.local/lib/python3.10/site-packages (from iqss-gh-reporting==0.5) (1.24.3)
Requirement already satisfied: pandas in /home/barry/.local/lib/python3.10/site-packages (from iqss-gh-reporting==0.5) (2.0.2)
Requirement already satisfied: pathvalidate in /home/barry/.local/lib/python3.10/site-packages (from iqss-gh-reporting==0.5) (3.0.0)
Requirement already satisfied: pyyaml in /usr/lib/python3/dist-packages (from iqss-gh-reporting==0.5) (5.4.1)
Requirement already satisfied: attrs>=17.3.0 in /home/barry/.local/lib/python3.10/site-packages (from aiohttp->iqss-gh-reporting==0.5) (23.1.0)
Requirement already satisfied: charset-normalizer<4.0,>=2.0 in /home/barry/.local/lib/python3.10/site-packages (from aiohttp->iqss-gh-reporting==0.5) (3.1.0)
Requirement already satisfied: multidict<7.0,>=4.5 in /home/barry/.local/lib/python3.10/site-packages (from aiohttp->iqss-gh-reporting==0.5) (6.0.4)
Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /home/barry/.local/lib/python3.10/site-packages (from aiohttp->iqss-gh-reporting==0.5) (4.0.2)
Requirement already satisfied: yarl<2.0,>=1.0 in /home/barry/.local/lib/python3.10/site-packages (from aiohttp->iqss-gh-reporting==0.5) (1.9.2)
Requirement already satisfied: frozenlist>=1.1.1 in /home/barry/.local/lib/python3.10/site-packages (from aiohttp->iqss-gh-reporting==0.5) (1.3.3)
Requirement already satisfied: aiosignal>=1.1.2 in /home/barry/.local/lib/python3.10/site-packages (from aiohttp->iqss-gh-reporting==0.5) (1.3.1)
Requirement already satisfied: graphql-core<3.3,>=3.2 in /home/barry/.local/lib/python3.10/site-packages (from gql->iqss-gh-reporting==0.5) (3.2.3)
Requirement already satisfied: backoff<3.0,>=1.11.1 in /home/barry/.local/lib/python3.10/site-packages (from gql->iqss-gh-reporting==0.5) (2.2.1)
Requirement already satisfied: ply>=3.6 in /home/barry/.local/lib/python3.10/site-packages (from graphql-py->iqss-gh-reporting==0.5) (3.11)
Requirement already satisfied: python-dateutil>=2.8.2 in /home/barry/.local/lib/python3.10/site-packages (from pandas->iqss-gh-reporting==0.5) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in /usr/lib/python3/dist-packages (from pandas->iqss-gh-reporting==0.5) (2022.1)
Requirement already satisfied: tzdata>=2022.1 in /home/barry/.local/lib/python3.10/site-packages (from pandas->iqss-gh-reporting==0.5) (2023.3)
Requirement already satisfied: deprecated in /home/barry/.local/lib/python3.10/site-packages (from PyGithub->iqss-gh-reporting==0.5) (1.2.14)
Requirement already satisfied: pyjwt>=2.4.0 in /home/barry/.local/lib/python3.10/site-packages (from pyjwt[crypto]>=2.4.0->PyGithub->iqss-gh-reporting==0.5) (2.7.0)
Requirement already satisfied: pynacl>=1.4.0 in /usr/lib/python3/dist-packages (from PyGithub->iqss-gh-reporting==0.5) (1.5.0)
Requirement already satisfied: requests>=2.14.0 in /usr/lib/python3/dist-packages (from PyGithub->iqss-gh-reporting==0.5) (2.25.1)
Requirement already satisfied: cryptography>=3.4.0 in /usr/lib/python3/dist-packages (from pyjwt[crypto]>=2.4.0->PyGithub->iqss-gh-reporting==0.5) (3.4.8)
Requirement already satisfied: cffi>=1.4.1 in /home/barry/.local/lib/python3.10/site-packages (from pynacl>=1.4.0->PyGithub->iqss-gh-reporting==0.5) (1.15.1)
Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.8.2->pandas->iqss-gh-reporting==0.5) (1.16.0)
Requirement already satisfied: idna>=2.0 in /usr/lib/python3/dist-packages (from yarl<2.0,>=1.0->aiohttp->iqss-gh-reporting==0.5) (3.3)
Requirement already satisfied: wrapt<2,>=1.10 in /home/barry/.local/lib/python3.10/site-packages (from deprecated->PyGithub->iqss-gh-reporting==0.5) (1.15.0)
Requirement already satisfied: pycparser in /home/barry/.local/lib/python3.10/site-packages (from cffi>=1.4.1->pynacl>=1.4.0->PyGithub->iqss-gh-reporting==0.5) (2.21)
Building wheels for collected packages: iqss-gh-reporting
Building wheel for iqss-gh-reporting (setup.py) ... done
Created wheel for iqss-gh-reporting: filename=iqss_gh_reporting-0.5-py3-none-any.whl size=33671 sha256=528ff2d22dcf48fe24a4882ad374617ed49799c15914fb7cd9822f2fb1887ee1
Stored in directory: /tmp/pip-ephem-wheel-cache-xgbl9agw/wheels/60/48/4e/67cf42315ddb16f7c572094bf1015d4b40f5e098bd02a712fe
Successfully built iqss-gh-reporting
Installing collected packages: iqss-gh-reporting
Attempting uninstall: iqss-gh-reporting
Found existing installation: iqss-gh-reporting 0.5
Uninstalling iqss-gh-reporting-0.5:
Successfully uninstalled iqss-gh-reporting-0.5
Successfully installed iqss-gh-reporting-0.5
~/PycharmProjects/iqss_gh_reporting/build_test

<info>
file: ./build_and_deploy_local.sh
pwd: /home/barry/PycharmProjects/iqss_gh_reporting/build_test
</info>

<msg>

Build and install complete.
The build will put these files and their associated libraries in your path.
create_iq_snapshot_init
create_iq_snapshot
__
Next Steps:
() Check that the build actually completed succesfully by reviewing the output.
() Test out the create_iq_snapshot_init build correctly using

create_iq_snapshot_init --help

() Follow the rest of the instructions in the readme
</msg>
++ press <enter> to continue ++

~/PycharmProjects/iqss_gh_reporting/build_test/example

<info>
file: ./build_and_run_example.sh
pwd: /home/barry/PycharmProjects/iqss_gh_reporting/build_test/example
</info>

<msg>
Will now run create_iq_snapshot_init
</msg>
++ press <enter> to continue ++


Yaml file path: /home/barry/PycharmProjects/iqss_gh_reporting/build_test/example/input_file.yaml
YAML data is valid!
------------------------------
Defaults currently mapped to Command Line input:
Any changes you just made will be written back to the yaml file
you can run this file repeatedly to update the defaults


collection_flag:
h: 'str: valid values: start | snapshot | end. api=required. file=Ignored.'
v: snapshot
data_collected_time:
h: 'str: When working with file input,use this.-special_char] ok:''_'' no
trailing /. api=ignored. file=required.'
v: ''
organization_name:
h: 'str: e.g: IQSS. Always required.'
v: IQSS
output_base_dir:
h: 'str: /mnt/hgfs/iq_reporting_collab/run/out;no[ ,.-special_char] ok:''_''.
No trailing /. api=ignored. file=Optional'
v: .
output_file_base_name:
h: 'str: e.g. sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig  .api=ignored.
file=not required.'
v: ''
project_name:
h: 'str: e.g: IQSS/dataverse. Always required.'
v: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34)
sprint_name:
h: 'str: e.g. sprint_2023_04_26;no[ ,.-special_char] ok:''_''; api=required.file=required.'
v: example_collection_sprint
src_dir_name:
h: 'str: e.g: ~/iqss_gh_reporting/run/in no[ ,.-special_char] ok:''_'' no
trailing /. api=ignored. file=required.'
v: ''
src_file_name:
h: 'str: e.g: sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig.tsv
.api=ignored. file=required.'
v: sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig.tsv
src_type:
h: 'str: valid values: api | file. Always required.'
v: api
workflow_name:
h: very short description or code.no[ ,.-special_char] ok:'_' Optional.
v: '000'


<info>
file: ./build_and_run_example.sh
pwd: /home/barry/PycharmProjects/iqss_gh_reporting/build_test/example
</info>

<msg>
Will now run create_iq_snapshot
</msg>
++ press <enter> to continue ++

Running /home/barry/.local/bin/create_iq_snapshot as the main program
YAML data is valid!
input arguments:

collection_flag:
h: 'str: valid values: start | snapshot | end. api=required. file=Ignored.'
v: snapshot
data_collected_time:
h: 'str: When working with file input,use this.-special_char] ok:''_'' no trailing
/. api=ignored. file=required.'
v: ''
organization_name:
h: 'str: e.g: IQSS. Always required.'
v: IQSS
output_base_dir:
h: 'str: /mnt/hgfs/iq_reporting_collab/run/out;no[ ,.-special_char] ok:''_''. No
trailing /. api=ignored. file=Optional'
v: .
output_file_base_name:
h: 'str: e.g. sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig  .api=ignored.
file=not required.'
v: ''
project_name:
h: 'str: e.g: IQSS/dataverse. Always required.'
v: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34)
sprint_name:
h: 'str: e.g. sprint_2023_04_26;no[ ,.-special_char] ok:''_''; api=required.file=required.'
v: example_collection_sprint
src_dir_name:
h: 'str: e.g: ~/iqss_gh_reporting/run/in no[ ,.-special_char] ok:''_'' no trailing
/. api=ignored. file=required.'
v: ''
src_file_name:
h: 'str: e.g: sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig.tsv .api=ignored.
file=required.'
v: sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig.tsv
src_type:
h: 'str: valid values: api | file. Always required.'
v: api
workflow_name:
h: very short description or code.no[ ,.-special_char] ok:'_' Optional.
v: '000'

output_file_base_name 4api: example_collection_sprint-snapshot-000-api-2024_01_07_135415
directory exists or was created now: example_collection_sprint
projects: looking to match IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34) with IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34)
Pandas version:2.0.2
start: 0, 0 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column ▶ SPRINT READY
end: 1, 2 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column ▶ SPRINT READY
start: 1, 2 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column This Sprint 🏃♀️ 🏃
end: 6, 7 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column This Sprint 🏃♀️ 🏃
start: 6, 7 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column IQSS Team - In Progress  💻
end: 8, 9 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column IQSS Team - In Progress  💻
start: 8, 9 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column Ready for Review ⏩
end: 12, 13 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column Ready for Review ⏩
start: 12, 13 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column In Review 🔎
end: 16, 17 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column In Review 🔎
start: 16, 17 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column Ready for QA ⏩
end: 16, 17 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column Ready for QA ⏩
start: 16, 17 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column QA ✅
end: 16, 17 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column QA ✅
start: 16, 17 cards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34), Column Done 🚀
>>>>>> 48, 50 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,PullRequest ,10159,dataverse ,Fix Datasets API getVersionFiles endpoint content type filtering (JPA Criteria)
>>>>>> 98, 100 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,PullRequest ,10049,dataverse ,specify the extension case for XLSX files TabularIngest parameter
>>>>>> 148, 150 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,PullRequest ,9900,dataverse ,Extend DataFile API payload and new endpoints for Files (getHasBeenDeleted) and Access (userFileAccessRequested)
>>>>>> 198, 200 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,PullRequest ,9873,dataverse ,disable loading of metadata blocks in API tests, more sleep
>>>>>> 248, 250 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,PullRequest ,151,dataverse-frontend ,135 - Files table UI [2/2] - Search this dataset Input
>>>>>> 298, 300 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,PullRequest ,121,dataverse-frontend ,Add configbaker to the containerized development environment
>>>>>> 348, 350 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,PullRequest ,8940,dataverse ,8822 incomplete datasets via api
>>>>>> 398, 400 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,PullRequest ,9511,dataverse ,modified getCurationLabels() to use try-with-resources
>>>>>> 448, 450 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,Issue ,213,dataverse.harvard.edu ,add NcML previewers (HDF5 and NetCDF) to demo and Harvard Dataverse
>>>>>> 498, 500 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,PullRequest ,9129,dataverse ,IQSS/9126- Fix workflow token access
>>>>>> 548, 550 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,PullRequest ,9131,dataverse ,merge develop to master for 5.12.1 release
>>>>>> 598, 600 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,PullRequest ,8880,dataverse ,optionally split Shibboleth affiliation and return first or last value
>>>>>> 648, 650 vcards processed: IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34): Done 🚀                         ,Issue ,174,dataverse.harvard.edu ,Upgrade production to 5.11