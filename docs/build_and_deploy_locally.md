
```
perftest@ubuntu:~/DevCode/github-com-mreekie/iqss_gh_reporting/scripts$ ./build_and_deploy_local.sh 
============================

This assumes that you are running the from the ./scripts directory in the project tree.
That would make the directory above it the root of the project
The script is going to to build the sources and then deploy it with pip to your local environment.

press <enter> to continue
============================

~/DevCode/github-com-mreekie/iqss_gh_reporting ~/DevCode/github-com-mreekie/iqss_gh_reporting/scripts

Building the code here:
../


Building....

running bdist_wheel
running build
running build_py
running build_scripts
copying and adjusting workflows/create_iq_snapshot_init -> build/scripts-3.10
copying and adjusting workflows/create_iq_snapshot -> build/scripts-3.10
copying and adjusting workflows/process_labels -> build/scripts-3.10
/usr/lib/python3/dist-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
warnings.warn(
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64/wheel
creating build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/pdata.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/utils.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/__init__.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/fetch_from_repository.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/graphql_query_lib.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/transformer.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/sprint_metadata.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/process_labels_util.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
copying build/lib/iqss_gh_reporting/legacy.py -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting
creating build/bdist.linux-x86_64/wheel/z-scratch
copying build/lib/z-scratch/scratch-00.py -> build/bdist.linux-x86_64/wheel/z-scratch
copying build/lib/z-scratch/utils.py -> build/bdist.linux-x86_64/wheel/z-scratch
copying build/lib/z-scratch/__init__.py -> build/bdist.linux-x86_64/wheel/z-scratch
copying build/lib/z-scratch/dev-capture_pr_points_from_issues.py -> build/bdist.linux-x86_64/wheel/z-scratch
creating build/bdist.linux-x86_64/wheel/deprecated
creating build/bdist.linux-x86_64/wheel/deprecated/iqss_gh_reporting
copying build/lib/deprecated/iqss_gh_reporting/test_validate_project_data_input.py -> build/bdist.linux-x86_64/wheel/deprecated/iqss_gh_reporting
copying build/lib/deprecated/iqss_gh_reporting/main.py -> build/bdist.linux-x86_64/wheel/deprecated/iqss_gh_reporting
copying build/lib/deprecated/iqss_gh_reporting/__init__.py -> build/bdist.linux-x86_64/wheel/deprecated/iqss_gh_reporting
copying build/lib/deprecated/iqss_gh_reporting/create_iq_snapshot_api.py -> build/bdist.linux-x86_64/wheel/deprecated/iqss_gh_reporting
copying build/lib/deprecated/iqss_gh_reporting/create_iq_snapshot_file.py -> build/bdist.linux-x86_64/wheel/deprecated/iqss_gh_reporting
copying build/lib/deprecated/iqss_gh_reporting/deprecated.py -> build/bdist.linux-x86_64/wheel/deprecated/iqss_gh_reporting
copying build/lib/deprecated/iqss_gh_reporting/test_utils.py -> build/bdist.linux-x86_64/wheel/deprecated/iqss_gh_reporting
creating build/bdist.linux-x86_64/wheel/deprecated/scratch
copying build/lib/deprecated/scratch/scratch-00.py -> build/bdist.linux-x86_64/wheel/deprecated/scratch
copying build/lib/deprecated/scratch/class_line.py -> build/bdist.linux-x86_64/wheel/deprecated/scratch
copying build/lib/deprecated/scratch/ex1.py -> build/bdist.linux-x86_64/wheel/deprecated/scratch
copying build/lib/deprecated/scratch/__init__.py -> build/bdist.linux-x86_64/wheel/deprecated/scratch
copying build/lib/deprecated/scratch/secretNumber.py -> build/bdist.linux-x86_64/wheel/deprecated/scratch
copying build/lib/deprecated/scratch/ForMikev41.py -> build/bdist.linux-x86_64/wheel/deprecated/scratch
creating build/bdist.linux-x86_64/wheel/deprecated/process_flat_file
copying build/lib/deprecated/process_flat_file/__init__.py -> build/bdist.linux-x86_64/wheel/deprecated/process_flat_file
creating build/bdist.linux-x86_64/wheel/deprecated/process_flat_file/bin
copying build/lib/deprecated/process_flat_file/bin/__init__.py -> build/bdist.linux-x86_64/wheel/deprecated/process_flat_file/bin
copying build/lib/deprecated/process_flat_file/bin/process_flat_file.py -> build/bdist.linux-x86_64/wheel/deprecated/process_flat_file/bin
running install_egg_info
running egg_info
writing iqss_gh_reporting.egg-info/PKG-INFO
writing dependency_links to iqss_gh_reporting.egg-info/dependency_links.txt
writing requirements to iqss_gh_reporting.egg-info/requires.txt
writing top-level names to iqss_gh_reporting.egg-info/top_level.txt
reading manifest file 'iqss_gh_reporting.egg-info/SOURCES.txt'
adding license file 'LICENSE.txt'
writing manifest file 'iqss_gh_reporting.egg-info/SOURCES.txt'
Copying iqss_gh_reporting.egg-info to build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.1.egg-info
running install_scripts
creating build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.1.data
creating build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.1.data/scripts
copying build/scripts-3.10/create_iq_snapshot_init -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.1.data/scripts
copying build/scripts-3.10/create_iq_snapshot -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.1.data/scripts
copying build/scripts-3.10/process_labels -> build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.1.data/scripts
changing mode of build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.1.data/scripts/create_iq_snapshot_init to 775
changing mode of build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.1.data/scripts/create_iq_snapshot to 775
changing mode of build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.1.data/scripts/process_labels to 775
adding license file "LICENSE.txt" (matched pattern "LICEN[CS]E*")
creating build/bdist.linux-x86_64/wheel/iqss_gh_reporting-0.1.dist-info/WHEEL
creating 'dist/iqss_gh_reporting-0.1-py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
adding 'deprecated/iqss_gh_reporting/__init__.py'
adding 'deprecated/iqss_gh_reporting/create_iq_snapshot_api.py'
adding 'deprecated/iqss_gh_reporting/create_iq_snapshot_file.py'
adding 'deprecated/iqss_gh_reporting/deprecated.py'
adding 'deprecated/iqss_gh_reporting/main.py'
adding 'deprecated/iqss_gh_reporting/test_utils.py'
adding 'deprecated/iqss_gh_reporting/test_validate_project_data_input.py'
adding 'deprecated/process_flat_file/__init__.py'
adding 'deprecated/process_flat_file/bin/__init__.py'
adding 'deprecated/process_flat_file/bin/process_flat_file.py'
adding 'deprecated/scratch/ForMikev41.py'
adding 'deprecated/scratch/__init__.py'
adding 'deprecated/scratch/class_line.py'
adding 'deprecated/scratch/ex1.py'
adding 'deprecated/scratch/scratch-00.py'
adding 'deprecated/scratch/secretNumber.py'
adding 'iqss_gh_reporting/__init__.py'
adding 'iqss_gh_reporting/fetch_from_repository.py'
adding 'iqss_gh_reporting/graphql_query_lib.py'
adding 'iqss_gh_reporting/legacy.py'
adding 'iqss_gh_reporting/pdata.py'
adding 'iqss_gh_reporting/process_labels_util.py'
adding 'iqss_gh_reporting/sprint_metadata.py'
adding 'iqss_gh_reporting/transformer.py'
adding 'iqss_gh_reporting/utils.py'
adding 'iqss_gh_reporting-0.1.data/scripts/create_iq_snapshot'
adding 'iqss_gh_reporting-0.1.data/scripts/create_iq_snapshot_init'
adding 'iqss_gh_reporting-0.1.data/scripts/process_labels'
adding 'z-scratch/__init__.py'
adding 'z-scratch/dev-capture_pr_points_from_issues.py'
adding 'z-scratch/scratch-00.py'
adding 'z-scratch/utils.py'
adding 'iqss_gh_reporting-0.1.dist-info/LICENSE.txt'
adding 'iqss_gh_reporting-0.1.dist-info/METADATA'
adding 'iqss_gh_reporting-0.1.dist-info/WHEEL'
adding 'iqss_gh_reporting-0.1.dist-info/top_level.txt'
adding 'iqss_gh_reporting-0.1.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel

Installing....

Defaulting to user installation because normal site-packages is not writeable
Processing /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting
Preparing metadata (setup.py) ... done
Requirement already satisfied: PyGithub in /home/perftest/.local/lib/python3.10/site-packages (from iqss-gh-reporting==0.1) (1.58.2)
Requirement already satisfied: gql in /usr/local/lib/python3.10/dist-packages (from iqss-gh-reporting==0.1) (3.4.0)
Requirement already satisfied: graphql-py in /home/perftest/.local/lib/python3.10/site-packages (from iqss-gh-reporting==0.1) (0.8.1)
Requirement already satisfied: pandas in /home/perftest/.local/lib/python3.10/site-packages (from iqss-gh-reporting==0.1) (1.5.3)
Requirement already satisfied: pathvalidate in /usr/local/lib/python3.10/dist-packages (from iqss-gh-reporting==0.1) (2.5.2)
Requirement already satisfied: pyyaml in /usr/lib/python3/dist-packages (from iqss-gh-reporting==0.1) (5.4.1)
Requirement already satisfied: yarl<2.0,>=1.6 in /usr/local/lib/python3.10/dist-packages (from gql->iqss-gh-reporting==0.1) (1.8.2)
Requirement already satisfied: graphql-core<3.3,>=3.2 in /usr/local/lib/python3.10/dist-packages (from gql->iqss-gh-reporting==0.1) (3.2.3)
Requirement already satisfied: backoff<3.0,>=1.11.1 in /usr/local/lib/python3.10/dist-packages (from gql->iqss-gh-reporting==0.1) (2.2.1)
Requirement already satisfied: ply>=3.6 in /home/perftest/.local/lib/python3.10/site-packages (from graphql-py->iqss-gh-reporting==0.1) (3.11)
Requirement already satisfied: python-dateutil>=2.8.1 in /home/perftest/.local/lib/python3.10/site-packages (from pandas->iqss-gh-reporting==0.1) (2.8.2)
Requirement already satisfied: numpy>=1.21.0 in /home/perftest/.local/lib/python3.10/site-packages (from pandas->iqss-gh-reporting==0.1) (1.24.2)
Requirement already satisfied: pytz>=2020.1 in /usr/lib/python3/dist-packages (from pandas->iqss-gh-reporting==0.1) (2022.1)
Requirement already satisfied: requests>=2.14.0 in /home/perftest/.local/lib/python3.10/site-packages (from PyGithub->iqss-gh-reporting==0.1) (2.29.0)
Requirement already satisfied: deprecated in /usr/local/lib/python3.10/dist-packages (from PyGithub->iqss-gh-reporting==0.1) (1.2.13)
Requirement already satisfied: pynacl>=1.4.0 in /usr/lib/python3/dist-packages (from PyGithub->iqss-gh-reporting==0.1) (1.5.0)
Requirement already satisfied: pyjwt[crypto]>=2.4.0 in /usr/local/lib/python3.10/dist-packages (from PyGithub->iqss-gh-reporting==0.1) (2.6.0)
Requirement already satisfied: cryptography>=3.4.0 in /usr/lib/python3/dist-packages (from pyjwt[crypto]>=2.4.0->PyGithub->iqss-gh-reporting==0.1) (3.4.8)
Requirement already satisfied: cffi>=1.4.1 in /usr/local/lib/python3.10/dist-packages (from pynacl>=1.4.0->PyGithub->iqss-gh-reporting==0.1) (1.15.1)
Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.8.1->pandas->iqss-gh-reporting==0.1) (1.16.0)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.14.0->PyGithub->iqss-gh-reporting==0.1) (1.26.13)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests>=2.14.0->PyGithub->iqss-gh-reporting==0.1) (2020.6.20)
Requirement already satisfied: idna<4,>=2.5 in /usr/lib/python3/dist-packages (from requests>=2.14.0->PyGithub->iqss-gh-reporting==0.1) (3.3)
Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.14.0->PyGithub->iqss-gh-reporting==0.1) (3.1.0)
Requirement already satisfied: multidict>=4.0 in /usr/local/lib/python3.10/dist-packages (from yarl<2.0,>=1.6->gql->iqss-gh-reporting==0.1) (6.0.4)
Requirement already satisfied: wrapt<2,>=1.10 in /usr/local/lib/python3.10/dist-packages (from deprecated->PyGithub->iqss-gh-reporting==0.1) (1.15.0)
Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi>=1.4.1->pynacl>=1.4.0->PyGithub->iqss-gh-reporting==0.1) (2.21)
Building wheels for collected packages: iqss-gh-reporting
Building wheel for iqss-gh-reporting (setup.py) ... done
Created wheel for iqss-gh-reporting: filename=iqss_gh_reporting-0.1-py3-none-any.whl size=45251 sha256=2e4b8e81f9d3999bb6219e0aa688748219ad13098305d32d678a3ace5d733e15
Stored in directory: /tmp/pip-ephem-wheel-cache-k1n235il/wheels/4a/7f/b3/d210cd71c693cf10bf317fb27629da0b685a8fd066e16b68bf
Successfully built iqss-gh-reporting
Installing collected packages: iqss-gh-reporting
Attempting uninstall: iqss-gh-reporting
Found existing installation: iqss-gh-reporting 0.1
Uninstalling iqss-gh-reporting-0.1:
Successfully uninstalled iqss-gh-reporting-0.1
Successfully installed iqss-gh-reporting-0.1
~/DevCode/github-com-mreekie/iqss_gh_reporting/scripts

============================
pwd: /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts

Build and install complete.
The build will put these files and their associated libraries in your path.
create_iq_snapshot_init
create_iq_snapshot


Next Steps:
() Check that the build actually completed succesfully by reviewing the output.
() Test out the create_iq_snapshot_init build correctly using

create_iq_snapshot_init --help

() Follow the rest of the instructions in the readme

============================

perftest@ubuntu:~/DevCode/github-com-mreekie/iqss_gh_reporting/scripts$
```