#!/usr/bin/bash
# ================================================================================================================
# The objective of this frame:
# - read in a graphql file to find a pr and return its information
# - prepare the python that does the querying and returns the results to be a library
# ================================================================================================================
cat<<EOF
< info >
executing: $0
pwd:  $(pwd)

Example of executing this script:
pwd: /home/barry/Documents/github_reporting
cmd: /home/barry/PycharmProjects/iqss_gh_reporting/scripts/scaffolding/framework_04.sh


next: launching the build and deploy script
-------------------------------
</ info >

EOF

pushd "/home/barry/PycharmProjects/iqss_gh_reporting/scripts"
./build_and_deploy_local.sh
popd

cat<<EOF
< info >
--------------------------------
executing: $0
pwd:  $(pwd)
Next: invoking local environment & setting directories for this run
-------------------------------
</ info >
EOF

# TODO: this is hardcoded to barry's environment. It should not be.
source /home/barry/PycharmProjects/iqss_gh_reporting/venv/bin/activate
# TODO: this is hardcoded to barry's environment. It should not be.
SCRIPT_DIR="/home/barry/PycharmProjects/iqss_gh_reporting/scripts"
# TODO: this is hardcoded to barry's environment. It should not be.
WRK_DIR_RT="/home/barry/Documents/github_reporting/framework_04"
DATESTAMP=$(date +"%Y%m%d_%H%M%S")
TESTNUM=0
cat<<EOF
< info >
--------------------------------
executing: $0
pwd:  $(pwd)
Next: invoking local environment & setting directories for this run
Time Stamp: ${DATESTAMP}
Directories:
SCRIPT_DIR: "${SCRIPT_DIR}"
WRK_DIR_RT: "${WRK_DIR_RT}"
INDIR: "${WRK_DIR_RT}/in"
WRKDIR: "${WRK_DIR_RT}/wrk"
OUTDIR: "${WRK_DIR_RT}/out"

input file:
${WRK_DIR_RT}/in/${WRK_FILE}

Note: if this is a test using the API WRK_FILE will not be defined.

-------------------------------
</ info >
EOF


mkdir -p ${WRK_DIR_RT}/in || exit 1
mkdir -p ${WRK_DIR_RT}/wrk || exit 1
mkdir -p ${WRK_DIR_RT}/out || exit 1

# This command should not exit if it fail
rm ${WRK_DIR_RT}/out/*.json > 2&>1


cat<<EOF
< info >
--------------------------------
executing: $0
pwd:  $(pwd)

Directories Contents:

$(find "${WRK_DIR_RT}" -type f)

-----
Next: kickoff the Test

================================
================================
</ info >
EOF

########################################################################################################################
TESTNUM=$(( TESTNUM + 1 ))
# This is a simplistic on/off switch.
# If false means this does not run
if true; then

cat<<EOF
< info >
--------------------------------
executing: $0
pwd:  $(pwd)
Next: Execute Test number ${TESTNUM}

Test: return the results of a query for a single PR (see: query_key)

--------------------------------
</ info >

EOF

pushd ${SCRIPT_DIR}/scaffolding

query_key="query_get_one_pr"
python3 framework_04.py --query_key ${query_key} --loginOrg "IQSS" --repo "dataverse" --output_dir "${WRK_DIR_RT}/out" --output_file_name "test_${TESTNUM}-${query_key}-${DATESTAMP}" \
    --number 9597
popd
fi
