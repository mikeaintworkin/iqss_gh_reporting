#!/usr/bin/bash
#
#  any:
#         collection_flag: snapshot
#         collection_timestamp: 20230412-1632
#         dest_dir_name: ~/iqss_gh_reporting/run/out
#         sprint_name: April 26, 2023
# api:
#         organization_name: IQSS
#         project_name: IQSS/dataverse
# file:
#         src_dir_name: /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk
#         src_file_name: 2023_04_12-sprint-20230412-1632-02.csv
# 

#create_iq_snapshot_init_sprint.py --sprint_name "April 12, 2023" \
#                                  --collection_flag "start" \
##                                  --src_file_name "2023_04_12-sprint-20230412-1632-02.csv" \
#                                  --src_dir_name "~/DevCode/github-com-mreekie/iqss_gh_reporting/run/wrk" \
#                                  --collection_timestamp "20230412-1632"
#create_iq_snapshot_file.py

create_iq_snapshot_init \
     --collection_flag "end" \
     --collection_timestamp "" \
     --sprint_name "April 26, 2023" \
     --src_dir_name "" \
     --src_file_name "" \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --src_type "api"
     