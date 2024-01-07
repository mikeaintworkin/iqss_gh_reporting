#!/usr/bin/bash -x
# ================================================================================================================
# The objective of this frame is to work through the following steps outside of the development environment.
# - read in a graphql file to find a pr and return its information
# - prepare the python that does the querying and returns the results to be a library
# ================================================================================================================

pushd "/home/barry/PycharmProjects/iqss_gh_reporting/scripts"
./build_and_deploy_local.sh
popd


source /home/barry/PycharmProjects/iqss_gh_reporting/venv/bin/activate
SCRIPT_DIR="/home/barry/PycharmProjects/iqss_gh_reporting/scripts"
WRK_DIR_RT="/home/barry/Documents/github_reporting/framework_02"
DATESTAMP=$(date +"%Y%m%d_%H%M%S")
TESTNUM=0
cat<<EOF

--------------------------------
Directories:
SCRIPT_DIR: "${SCRIPT_DIR}"
WRK_DIR_RT: "${WRK_DIR_RT}"
INDIR: "${WRK_DIR_RT}/in"
WRKDIR: "${WRK_DIR_RT}/wrk"
OUTDIR: "${WRK_DIR_RT}/out"

-------------------------------
input file:
${WRK_DIR_RT}/in/${WRK_FILE}

EOF


mkdir -p ${WRK_DIR_RT}/in || exit 1
mkdir -p ${WRK_DIR_RT}/wrk || exit 1
mkdir -p ${WRK_DIR_RT}/out || exit 1

rm ${WRK_DIR_RT}/out/*.json || exit 1


cat<<EOF
--------------------------------
Directories Contents:

$(find "${WRK_DIR_RT}" -type f)

-----
kickoff the Test

================================
EOF

########################################################################################################################
# If false means this does not run
TESTNUM=$(( TESTNUM + 1 ))
if true; then
cat<<EOF
--------------------------------
${TESTNUM}

test: PR exists and has a single issue associated with it.
example PR: #9597 "9369 Shib groups (and other custom groups), as subgroups of an explicit group"
--------------------------------
EOF
query_key="query_get_one_pr"
python3 framework_02.py --query_key ${query_key} --loginOrg "IQSS" --repo "dataverse" --output_dir "${WRK_DIR_RT}/out" --output_file_name "test_${TESTNUM}-${query_key}-${DATESTAMP}" \
    --number 9597
fi


########################################################################################################################
# If false means this does not run
TESTNUM=$(( TESTNUM + 1 ))
if false; then
cat<<EOF
--------------------------------
${TESTNUM}

test: PR does not exist
PR: 9999
--------------------------------
EOF

query_key="query_get_one_pr"
python3 framework_02.py --query_key ${query_key} --loginOrg "IQSS" --repo "dataverse" --output_dir "${WRK_DIR_RT}/out" --output_file_name "test_${TESTNUM}-${query_key}-${DATESTAMP}" \
    --number 9999
fi

########################################################################################################################
# If false means this does not run
TESTNUM=$(( TESTNUM + 1 ))
if false; then
cat<<EOF
--------------------------------
${TESTNUM}

PR exists and has a 2 issues associated with it.
PR: #9402 "Iqss/9150 handle fundreg reqs for ext cvv"
--------------------------------
EOF

query_key="query_get_one_pr"
python3 framework_02.py --query_key ${query_key} --loginOrg "IQSS" --repo "dataverse" --output_dir "${WRK_DIR_RT}/out" --output_file_name "test_${TESTNUM}-${query_key}-${DATESTAMP}" \
    --number 9402
fi

########################################################################################################################
# If false means this does not run
TESTNUM=$(( TESTNUM + 1 ))
if false; then
cat<<EOF
--------------------------------
${TESTNUM}

test: PR exists but there are no associated issues
PR:#9632 "External Exporters bug fix"
--------------------------------
EOF

query_key="query_get_one_pr"
python3 framework_02.py --query_key ${query_key} --loginOrg "IQSS" --repo "dataverse" --output_dir "${WRK_DIR_RT}/out" --output_file_name "test_${TESTNUM}-${query_key}-${DATESTAMP}" \
    --number 9632
fi

########################################################################################################################
# If false means this does not run
TESTNUM=$(( TESTNUM + 1 ))
if false; then
cat<<EOF
--------------------------------
${TESTNUM}
test: The graphql is malformed.
Otherwise identical to PR exists but there are no associated issues
example PR: External Exporters bug fix #9632
I'm going to cause the graphql to be malformed for this.
See: def query_get_one_pr_malformed() in graphql_query_lib
--------------------------------
EOF

query_key="query_get_one_pr_malformed"
python3 framework_02.py --query_key ${query_key} --loginOrg "IQSS" --repo "dataverse" --output_dir "${WRK_DIR_RT}/out" --output_file_name "test_${TESTNUM}-${query_key}-${DATESTAMP}" \
    --number 9632
fi
