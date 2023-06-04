#!/usr/bin/bash -x

SCRIPT_DIR="/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts"
WRK_DIR_RT="/home/perftest/iqss_gh_reporting/test/test_frame_02"
INDIR="${WRK_DIR_RT}/in"
WRK_FILE=""

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

EOF

${SCRIPT_DIR}/test_frame_02.py \
    --qry
    --org
    --repo
