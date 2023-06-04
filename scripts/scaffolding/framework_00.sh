#!/usr/bin/bash -x

WRK_DIR_RT="/home/perftest/iqss_gh_reporting/test/test_frame_00"
create_iq_snapshot_init \
     --collection_flag "snapshot" \
     --sprint_name issue_num_29 \
     --src_dir_name "" \
     --src_file_name "" \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --src_type "api" \
     --output_base_dir "${WRK_DIR_RT}/out" \
     --workflow_name "frame_00"
     

cat<<EOF

-----
kickoff the Test
The yaml file that was created in create_iq_snapshot_init will be the input for this step
The yaml file is in the cwd

EOF

# ./test_frame_00.py
     

