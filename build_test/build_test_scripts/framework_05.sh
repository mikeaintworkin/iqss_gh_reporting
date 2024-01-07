#
# ================================================================================================================
# Bash Script:
# Description:
# - This script was used to get me back into the context of the existing code after being away for awhile.
# - See  https://github.com/thisaintwork/iqss_gh_reporting/issues/59
# Objective:
# - This
# - tracked via: Figure out why Ceilyn scripts are not working
# see also #57.  This is the first of the framework scripts that moves the venv call out of the build and deploy script
#
# Arguments:
#  -w contains the working directory. This directory will be the root for the data collection.
#     the director should not contain a trailing "/"
#   Example of executing this script:
#  pwd: /home/barry/Documents/github_reporting
#  cmd: /home/barry/PycharmProjects/iqss_gh_reporting/scripts/scaffolding/framework_05.sh \
#      -s "/home/barry/PycharmProjects/iqss_gh_reporting/scripts" \
#      -v "/home/barry/PycharmProjects/iqss_gh_reporting/venv/bin/activate"
# Output:
#   stdout - The script is very chatty on purpose. It tells you where you are and what is coming next in several places
#
#   return - N/A
#
# Example:
#   cd ~/PycharmProjects/iqss_gh_reporting/build_test/build_test_script
#    ./framework_05.sh
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
SCRIPT_DIR="$(pwd)/../"
THIS_FILE=$0
msg=$(cat <<EOF

  Section: build the project to create new commands

  ${THIS_FILE} assumes that the directory it is running in is one level below in the directory heirarchy
  from ${BUILD_SCRIPT}

  e.g. pwd=./iqss_gh_reporting/build_test/build_test_scripts

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
popd || exit 1


