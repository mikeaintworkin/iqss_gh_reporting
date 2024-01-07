#
# ================================================================================================================
# Bash Script:
# Description:
# - This script runs an example query against the legacy dataverse project.
# - It was created to document the code that accesses the legacy api before I move on to using only the graphql API
# - See  https://github.com/thisaintwork/iqss_gh_reporting/issues/59
# Objective:
#
# Arguments:
# Output:
#   stdout - The script is very chatty on purpose. It tells you where you are and what is coming next in several places
#
#   return - N/A
#
# Example:
#   cd ~/PycharmProjects/iqss_gh_reporting/build_test/example
#
#
#   ~/PycharmProjects/  is the root for my dev projects
#   ./iqss_gh_reporting is the root of this project
#
#
# Pre-requisites:
# * Directory variables do not have a trailing slash
# ================================================================================================================


# -----------------------------------------------------------------------------------------------------------------
# Function:
# Description: Provides basic information on the context for what is happening in the script
# Arguments:
#   $1 (input) - The name of the current executing bash file
#   $2 (input) - The name of the next thing the script is going to do (e.g. calling bash file XXX.SH)
# Output:
#   stdout - the input and the present working directory.
#
#   return - N/A
# Example:
#   echo_basic_info "${THIS_FILE}" "setting directories and timestamp for this run"
#
echo_basic_info() {
cat<<EOF

<info>
file: $1
pwd: $(pwd)
</info>

<msg>
$2
</msg>
++ press <enter> to continue ++
EOF
read line
}


# ================================================================================================================
# Section: MAIN
# Description: This section acts as the main routine for this script. The details are found at the header


# Section: initialize global variables
BUILD_SCRIPT="build_and_deploy_local.sh"

# Section: Set input varaibles and call echo_basic_info
SCRIPT_DIR="$(pwd)/.."
THIS_FILE=$0
msg=$(cat <<EOF

  Section: build the project to create new commands

  ${THIS_FILE} assumes that the directory it is running in is one level below in the directory heirarchy
  from ${BUILD_SCRIPT}

  e.g. pwd=./iqss_gh_reporting/build_test/build_test_scripts
  e.g. pwd=./iqss_gh_reporting/build_test/example


  ${BUILD_SCRIPT} will be (must be) run from the build_test directory

EOF
)
echo_basic_info "$0" "$msg"

# Section: build the project to create new commands

if [ ! -f "${SCRIPT_DIR}/${BUILD_SCRIPT}" ]; then
  msg="Failed. Not found: ${SCRIPT_DIR}/${BUILD_SCRIPT}"
  echo_basic_info "${0}" "$msg"
  exit 1
else
  msg="Successfully Verified existence of the build script: ${SCRIPT_DIR}/${BUILD_SCRIPT}"
  echo_basic_info "${0}" "$msg"
fi


#Section: run build and deploy script
pushd "${SCRIPT_DIR}" || exit 1
bash ./build_and_deploy_local.sh
popd

msg="Will now run create_iq_snapshot_init"
echo_basic_info "${0}" "$msg"


create_iq_snapshot_init --project_name 'IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34)' \
--collection_flag snapshot \
--organization_name IQSS \
--output_base_dir . \
--project_name 'IQSS/dataverse (TO BE RETIRED / DELETED in favor of project 34)' \
--sprint_name example_collection_sprint \
--src_type api \
--workflow_name '000'

msg="Will now run create_iq_snapshot"
echo_basic_info "${0}" "$msg"

create_iq_snapshot
