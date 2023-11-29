#!/usr/bin/bash
# ================================================================================================================
# The objective of this frame:
# - reproduce the test run that Ceilyn can't run on her newly installed macbook
# - tracked via: Figure out why Ceilyn scripts are not working
# - https://github.com/thisaintwork/iqss_gh_reporting/issues/56
# ================================================================================================================
cat<<EOF
< info >
executing: $0
pwd:  $(pwd)
  < find . -type f >
$(find . -type f)
  </find . -type f >

  < Example of executing this script:>
  pwd: /home/barry/Documents/github_reporting
  cmd: /home/barry/PycharmProjects/iqss_gh_reporting/scripts/scaffolding/framework_04.sh
  </Example of executing this script:>

next: launching the build and deploy script
-------------------------------
</info >

press <enter> to continue
============================
EOF
read line

pushd "/home/barry/PycharmProjects/iqss_gh_reporting/scripts"
./build_and_deploy_local.sh
popd

cat<<EOF
< info >
--------------------------------
executing: $0
pwd:  $(pwd)
  < find . -type f >
  $(find . -type f)
  </find . -type f >  $(pwd)
Next: invoking local environment & setting directories for this run
-------------------------------
</info >
press <enter> to continue
============================
EOF
read line


# Invoke the local environment
# TODO: this is hardcoded to barry's environment. It should not be.
source /home/barry/PycharmProjects/iqss_gh_reporting/venv/bin/activate


# TODO: this is hardcoded to barry's environment. It should not be.
SCRIPT_DIR="/home/barry/PycharmProjects/iqss_gh_reporting/scripts"
# TODO: this is hardcoded to barry's environment. It should not be.
WRK_DIR_RT="/home/barry/Documents/github_reporting/framework_05"
DATESTAMP=$(date +"%Y%m%d_%H%M%S")
TESTNUM=0
cat<<EOF
< info >
--------------------------------
executing: $0
pwd:  $(pwd)
  < find . -type f >
  $(find . -type f)
  </find . -type f >  $(pwd)
Next: invoking local environment & setting directories for this run

  < dir info >
    Time Stamp: ${DATESTAMP}
    Directories:
    SCRIPT_DIR: "${SCRIPT_DIR}"
    WRK_DIR_RT: "${WRK_DIR_RT}"
    INDIR: "${WRK_DIR_RT}/in"
    WRKDIR: "${WRK_DIR_RT}/wrk"
    OUTDIR: "${WRK_DIR_RT}/out"

    input file:
    ${WRK_DIR_RT}/in/${WRK_FILE}

    Note: This test is using the API so WRK_FILE will not be defined.

  </dir info >

-------------------------------
</info >
press <enter> to continue
============================
EOF
read line


mkdir -p ${WRK_DIR_RT}/in || exit 1
mkdir -p ${WRK_DIR_RT}/wrk || exit 1
mkdir -p ${WRK_DIR_RT}/out || exit 1

# This command should not exit if it fail
rm ${WRK_DIR_RT}/out/*.json


cat<<EOF
< info >
--------------------------------
executing: $0
pwd:  $(pwd)
  < find . -type f >
  $(find . -type f)
  </find . -type f >  $(pwd)

  < ${WRK_DIR_RT} Directories Contents: >
  $(find "${WRK_DIR_RT}" -type f)
  </${WRK_DIR_RT} Directories Contents: >

-----
Next: kickoff the Test

</info >
press <enter> to continue
============================
EOF
read line

########################################################################################################################
TESTNUM=$(( TESTNUM + 1 ))
# This is a simplistic on/off switch.
# If false means this does not run
if true; then

# Remove any existing input file
# This should not exit if it fails
rm ./input_file.yaml

cat<<EOF
< info >
--------------------------------
executing: $0
pwd:  $(pwd)
  < find . -type f >
  $(find . -type f)
  </find . -type f >  $(pwd)


Next: Execute Test number ${TESTNUM}

Test: Run the example api query from ./scripts/example/sprint_2023_05_24/bin/sprint_2023_05_24-api-example.sh

--------------------------------
</info >

press <enter> to continue
============================
EOF
read line

#     --collection_flag "" \
#     --data_collected_time "" \
#    --output_file_base_name "" \
#    --src_dir_name "" \
#     --src_file_name "" \


create_iq_snapshot_init \
     --organization_name "IQSS" \
     --output_base_dir  ${WRK_DIR_RT}/out/ \
     --project_name "IQSS/dataverse" \
     --sprint_name "snaps_collection" \
     --src_type "api" \
     --workflow_name "000"


cat<<EOF
==========================================================================
You have set the run parameters.

Summary:
$(cat ./input_file.yaml | grep : | grep -v h:)

==========================================================================


To actually run the analysis or collection and analysis run

create_iq_snapshot

from this same directory.


press <enter> to continue
============================
EOF
read line


fi
