#!/usr/bin/bash -x

# collection_flag: 'str: valid values: start | snapshot | end'
# organization_name: 'str: e.g: IQSS'
# output_base_dir: base directory for output files. e.g. ~/iqss_gh_reporting/run/out
# project_name: 'str: e.g: IQSS/dataverse'
# sprint_name: 'str: A string that represents the sprint name. e.g. April 12, 2023'
# src_dir_name: 'str: e.g: ~/iqss_gh_reporting/run/in'
# src_file_name: 'str: e.g: 2023_04_26-17_32_18-output.tsv'
# src_type: 'str: valid values: api | file'
# workflow_name: very short description or code

# setup the work    

# set this variable because the value is needed more than once.
# I know  SPRINTNAME is the final piece of the destination directory where the
#  processing in create_iq_snapshot puts the result.
# I will use that knowledge when I create the tar file so that I can have a 
#  small and neat relative path
# 
cat<<EOF

-----
First setup the yaml file

EOF
SCRIPT_DIR="/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts"
WRK_DIR_RT="/home/perftest/iqss_gh_reporting/test/test_frame_01"
WRK_FILE="2023_04_26-11_21_13--April 12 2023-end-mn-snapshot_sprint_from_file-file-20230429001318-sized.tsv"

rm "${WRK_DIR_RT}/wrk/input.tsv"
rm "${WRK_DIR_RT}/out/*"
ls -la "${WRK_DIR_RT}/in/${WRK_FILE}" 

cp "${WRK_DIR_RT}/in/${WRK_FILE}" "${WRK_DIR_RT}/wrk/input.tsv"




SPRINTNAME="sprint_2023_05_10"

create_iq_snapshot_init \
     --collection_flag "snapshot" \
     --sprint_name ${SPRINTNAME} \
     --src_dir_name "${WRK_DIR_RT}/wrk" \
     --src_file_name "input.tsv" \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --src_type "file" \
     --output_base_dir "${WRK_DIR_RT}/out" \
     --workflow_name "frame_01"
     

cat<<EOF

-----
kickoff the Test
The yaml file that was created in create_iq_snapshot_init will be the input for this step
The yaml file is in the cwd

EOF

${SCRIPT_DIR}/test_frame_01.py
     

