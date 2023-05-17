#!/usr/bin/bash -x

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
     --collection_flag "snapshot" \
     --collection_timestamp "" \
     --sprint_name "20230503sprint" \
     --src_dir_name "" \
     --src_file_name "" \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --src_type "api"
     --workflow_name "tst"

# iqss_gh_reporting
# usage: process_labels.py [-h] --input INPUT --output OUTPUT [--matrix MATRIX]
# process_labels.py: error: the following arguments are required: --input, --output
# perftest@ubuntu:~/DevCode/github-com-mreekie/iqss_gh_reporting$
DIRNAME=/home/perftest/iqss_gh_reporting/run/out/April_26_2023_sprint-end
INFILE=2023_05_10-14_37_49-April262023-end-create_iq_snapshot-api-20230510143749-sized.tsv
INFILECORE=$(echo "${INFILE}" | cut -d'-' -f1-7)


OUTFILE="${INFILECORE}-matrix_summary .tsv"
MATRIXFILE="${INFILECORE}-matrix.tsv"

cat<<EOF
${DIRNAME}
${INFILE}
${INFILECORE}
${OUTFILE}
${MATRIXFILE}
cp ${DIRNAME}/${INFILE} ${DIRNAME}/input.tsv

EOF

cp "${DIRNAME}/${INFILE}" "${DIRNAME}/input.tsv"

process_labels --input "${DIRNAME}/input.tsv" --output "${DIRNAME}/outputput.tsv" --matrix "${DIRNAME}/matrix.tsv"

cp  "${DIRNAME}/outputput.tsv" "${DIRNAME}/${OUTFILE}"
cp "${DIRNAME}/matrix.tsv" "${DIRNAME}/${MATRIXFILE}"
