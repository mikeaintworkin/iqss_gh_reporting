#!/usr/bin/bash
# exec 3>&1 4>&2
# trap 'exec 2>&4 1>&3' 0 1 2 3
# exec 1>log.out 2>&1

# ================================================================================================================
# The objective of this frame:
# - reproduce the test run that Ceilyn can't run on her newly installed macbook
# - tracked via: Figure out why Ceilyn scripts are not working
# - https://github.com/thisaintwork/iqss_gh_reporting/issues/56
# see also #57.  This is the first of the framework scripts that moves the venv call out of the builld and deploy script
#
#   Example of executing this script:
#  pwd: /home/barry/Documents/github_reporting
#  cmd: /home/barry/PycharmProjects/iqss_gh_reporting/scripts/scaffolding/framework_04.sh \
#      -s "/home/barry/PycharmProjects/iqss_gh_reporting/scripts" \
#      -v "/home/barry/PycharmProjects/iqss_gh_reporting/venv/bin/activate"
# ================================================================================================================

function print_help_message(){
cat<<EOF
  Usage: $(basename $0), with args
    [-v command to invoke virtual environment]
     example arg: \"/home/barry/PycharmProjects/iqss_gh_reporting/venv/bin/activate\"

    \"[-s scripts directory in checked out project]\"
    This is a required arg
    example arg: \"/home/barry/PycharmProjects/iqss_gh_reporting/scripts\"

    \"[-w working directory]\"
    This is a required arg
    example arg: \"/home/barry/PycharmProjects/iqss_gh_reporting/scripts\"

  Notes:
  () enclose all strings in quotes. In particular, enclose directory names in double quotes.
    e.g. "my directory" instead of my\ directory
  () include only fully qualified directory names.
    e.g. do not use the tilde \"~\" shortcut
EOF

}


function get_cli_options() {
  echo "processing command line"
  OPTIND=1
  while getopts 's:w:v:h' opt; do
  echo "processing command line option: $opt"
  case "$opt" in
    w)
      echo "Processing option 'w' with '${OPTARG}' argument"
      echo "Setting WRK_DIR_RT: ${OPTARG}"
      WRK_DIR_RT="${OPTARG}"
      ;;
    s)
      echo "Processing option 's' with '${OPTARG}' argument"
      echo "Setting SCRIPT_DIR: ${OPTARG}"
      SCRIPT_DIR="${OPTARG}"
      ;;
    v)
      echo "Processing option 'v' with '${OPTARG}' argument"
      echo "Activating virtual environment: ${OPTARG}"
      . "${OPTARG}"
      RTN="$?"
      [[ "$RTN" != "0" ]] && echo "Error when attemtpting to active the environment"
      if [[ "$(env |grep VIRTUAL_ENV | wc -l)" = "0" ]]; then
        echo "There is no virtual environment active"
      else
        echo "Virtual environment active"
        env |grep VIRTUAL_ENV
      fi
      ;;
    :)
      echo -e "option requires an argument.\nUsage: $(basename $0) [-v arg][-s arg]"
      echo " use -h for help"
      exit 1
      ;;
    h)
      print_help_message
      exit 0
      ;;
    ?)
      echo -e "Invalid command option.\nUsage: $(basename $0) [-v arg]"
      exit 1
      ;;
  esac
  done
  shift $(($OPTIND -1))
  THIS_FILE="$0"
}

echo_basic_info() {
cat<<EOF
-
--
executing file: $1
pwd:  $(pwd)
venv: <>$(env |grep VIRTUAL_ENV)</>
--
---
find . -type f (first 5 entries)
$(find . -type f | tail -5)
---
--
Next step: $2
--
++ press <enter> to continue ++
--
-
EOF
  read line
}

get_cli_options "$@"
echo ">> ${SCRIPT_DIR}"
echo ">> ${SCRIPT_DIR}/build_and_deploy_local.sh"
ls "${SCRIPT_DIR}/build_and_deploy_local.sh"

if [ ! -f "${SCRIPT_DIR}/build_and_deploy_local.sh" ]; then
  echo "${SCRIPT_DIR}/build_and_deploy_local.sh does not exist"
  echo "Missing -s CLI option or -s CLI option is not correct"
  echo " use -h for help on the CLI"
  exit 1
fi
if [ -z "${WRK_DIR_RT}" ]; then
  echo "WRK_DIR_RT was not defined"
  echo "Missing -w CLI option."
  echo " use -h for help on the CLI"
  exit 1
fi


echo_basic_info "${THIS_FILE}" "build_and_deploy_local.sh"

#run this script from the scripts directory
echo "pushd to ${SCRIPT_DIR}"
pushd "${SCRIPT_DIR}" || exit 1
./build_and_deploy_local.sh
echo "popd"
popd || exit 1


echo_basic_info "${THIS_FILE}" "setting directories and timestamp for this run"

DATESTAMP="$(date +"%Y%m%d_%H%M%S")"
mkdir -p "${WRK_DIR_RT}/in "|| exit 1
mkdir -p "${WRK_DIR_RT}/wrk" || exit 1
mkdir -p "${WRK_DIR_RT}/out" || exit 1

cat<<EOF
-
--
Time Stamp: "${DATESTAMP}"
--
---
Directories:
SCRIPT_DIR: "${SCRIPT_DIR}"
WRK_DIR_RT: "${WRK_DIR_RT}"
INDIR: "${WRK_DIR_RT}/in"
WRKDIR: "${WRK_DIR_RT}/wrk"
OUTDIR: "${WRK_DIR_RT}/out"
---
--
-
EOF

echo_basic_info "${THIS_FILE}" "create_iq_snapshot_init"

# #####################################################################################################################
# Test: Run the example api query from ./scripts/example/sprint_2023_05_24/bin/sprint_2023_05_24-api-example.sh
# #####################################################################################################################
# Remove any existing input file
# This should not exit if it fails
rm ./input_file.yaml


#     --collection_flag "" \
#     --data_collected_time "" \
#    --output_file_base_name "" \
#    --src_dir_name "" \
#     --src_file_name "" \


create_iq_snapshot_init \
     --organization_name "IQSS" \
     --output_base_dir  "${WRK_DIR_RT}/out/" \
     --project_name "IQSS/dataverse" \
     --sprint_name "snaps_collection" \
     --src_type "api" \
     --workflow_name "000"


#   $(cat ./input_file.yaml | grep : | grep -v h:)
# cat<<EOF
# ==========================================================================
# You have configured the parameters for this data analysis or  collection.
# To actually run the analysis or collection and analysis:
#   - remain in this directory.
#   - execute create_iq_snapshot
#
#   press <enter> to continue
#   ============================
# EOF
echo_basic_info "${THIS_FILE}" "create_iq_snapshot"

create_iq_snapshot
