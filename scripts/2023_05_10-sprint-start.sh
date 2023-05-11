#!/usr/bin/bash -x 

# collection_flag: 'str: valid values: start | snapshot | end'
# collection_timestamp: 'str: gen automaticaly for ''api'', require for  ''file'
# organization_name: 'str: e.g: IQSS'
# output_base_dir: base directory for output files. e.g. ~/iqss_gh_reporting/run/out
# project_name: 'str: e.g: IQSS/dataverse'
# sprint_name: 'str: A string that represents the sprint name. e.g. April 12, 2023'
# src_dir_name: 'str: e.g: ~/iqss_gh_reporting/run/in'
# src_file_name: 'str: e.g: 2023_04_26-17_32_18-output.tsv'
# src_type: 'str: valid values: api | file'
# workflow_name: very short description or code

# setup the work
create_iq_snapshot_init \
     --collection_flag "start" \
     --collection_timestamp "" \
     --sprint_name "sprint_2023_05_10" \
     --src_dir_name "" \
     --src_file_name "" \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --src_type "api" \
     --output_base_dir "/home/perftest/iqss_gh_reporting/run/out" \
     --workflow_name "r01"
     
# kickoff the work     
create_iq_snapshot
     
# usage: process_labels.py [-h] --input INPUT --output OUTPUT [--matrix MATRIX]
# process_labels.py: error: the following arguments are required: --input, --output
#
#DIRNAME="/home/perftest/iqss_gh_reporting/run/out/May 10, 2023/"
#DIRNAME=$(realpath "$DIRNAME")
#INFILE=2023_05_10-21_03_50-May102023-start-r01-api-20230510210350-sized.tsv

# runlog might contain for example:  
# This file is output from create_iq_snapshot
# DEST_DIR_NAME=/home/perftest/iqss_gh_reporting/run/out/snapshots/2023_04_30-20_05_58/                       
# DEST_FILE_SIZED=2023_04_30-20_05_58-April262023-snapshot-create_iq_snapshot_api-api-20230430200558-sized.tsv
. ./runlog.sh  


DIRNAME="${DEST_DIR_NAME}"
INFILE="${DEST_FILE_SIZED}"
INFILECORE=$(echo "${INFILE}" | cut -d'-' -f1-7)
INFILECORE=$(echo "${INFILECORE}" | xargs)
 
 
OUTFILE="${INFILECORE}-matrix_summary .tsv"
MATRIXFILE="${INFILECORE}-matrix.tsv"
 
cat<<EOF
DIRNAME    ${DIRNAME}
INFILE     ${INFILE}
INFILECORE ${INFILECORE}
OUTFILE    ${OUTFILE}
MATRIXFILE ${MATRIXFILE}

cp ${DIRNAME}/${INFILE} ${DIRNAME}/input.tsv
process_labels --input "${DIRNAME}/input.tsv" --output "${DIRNAME}/outputput.tsv" --matrix "${DIRNAME}/matrix.tsv"
rm ${DIRNAME}/input.tsv"
mv ${DIRNAME}/outputput.tsv" "${DIRNAME}/${OUTFILE}"
mv ${DIRNAME}/matrix.tsv" "${DIRNAME}/${MATRIXFILE}"     

EOF

rm ./runlog.sh
cp "${DIRNAME}/${INFILE}" "${DIRNAME}/input.tsv"
 
process_labels --input "${DIRNAME}/input.tsv" --output "${DIRNAME}/outputput.tsv" --matrix "${DIRNAME}/matrix.tsv"

rm "${DIRNAME}/input.tsv"
mv "${DIRNAME}/outputput.tsv" "${DIRNAME}/${OUTFILE}"
mv "${DIRNAME}/matrix.tsv" "${DIRNAME}/${MATRIXFILE}"     
     