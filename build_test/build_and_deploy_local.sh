
# ================================================================================================================
# The objective of this script is to build the current code and deploy it locally.
# MUST be run from the ./iqss_gh_reporting/scripts directory
# e.g /home/barry/PycharmProjects/iqss_gh_reporting/scripts
# where /home/barry/PycharmProjects/iqss_gh_reporting is the root of the project
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

# Section: Initialize Global Variable
DEVHOME='..'
SETUPPY='setup.py'

msg=$(cat <<EOF

The script is going to to build the sources and then deploy it with pip

This script MUST be run from the ./build_test directory in the project tree.
e.g ./PycharmProjects/iqss_gh_reporting/build_test
where ~/PycharmProjects/iqss_gh_reporting is the root of the project

e.g. We are looking for ${DEVHOME}/${SETUPPY}

EOF
)
echo_basic_info "$0" "$msg"

if [ ! -f "${DEVHOME}/${SETUPPY}" ]; then
  msg="Failed. Not found: ${DEVHOME}/${SETUPPY}."
  echo_basic_info "${0}" "$msg"
  exit 1
else
  msg="Successfully Verified existence of the build script: ${DEVHOME}/${SETUPPY}"
  echo_basic_info "${0}" "$msg"
fi

pushd ${DEVHOME} || exit 1
msg="Begin Building..."
echo_basic_info "${0}" "$msg"

bash -cl "python3 ./setup.py bdist_wheel"  || exit 1


msg="Begin Installing..."
echo_basic_info "${0}" "$msg"

pip3 install .  || exit 1
popd 

# Section: Set long variable to echo info back.
msg=$(cat <<EOF

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
EOF
)
echo_basic_info "${0}" "$msg"
