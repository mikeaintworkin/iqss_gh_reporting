#!/usr/bin/bash

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

SPRINTNAME="sprint_2023_05_10"
create_iq_snapshot_init \
     --collection_flag "start" \
     --collection_timestamp "" \
     --sprint_name ${SPRINTNAME} \
     --src_dir_name "" \
     --src_file_name "" \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --src_type "api" \
     --output_base_dir "/home/perftest/iqss_gh_reporting/run/out" \
     --workflow_name "r01"
     

cat<<EOF

-----
kickoff the work 
The yaml file that was created in create_iq_snapshot_init will be the input for this step
The yaml file is in the cwd

EOF

create_iq_snapshot
     
cat<<EOF

-----
 Mikes and Ceilyn's code is glued together here.
 create_iq_snapshot creates the ./runlog.sh file.
 in that file is text like the example below.

 example data
 DEST_DIR_NAME=/home/perftest/iqss_gh_reporting/run/out/snapshots/2023_04_30-20_05_58/                       
 DEST_FILE_SIZED=2023_04_30-20_05_58-April262023-snapshot-create_iq_snapshot_api-api-20230430200558-sized.tsv

EOF


# Mikes and Ceilyn's code is glued together here.
# create_iq_snapshot creates the ./runlog.sh file.
# in that file is text like the example below.
#
# example data
# DEST_DIR_NAME=/home/perftest/iqss_gh_reporting/run/out/snapshots/2023_04_30-20_05_58/                       
# DEST_FILE_SIZED=2023_04_30-20_05_58-April262023-snapshot-create_iq_snapshot_api-api-20230430200558-sized.tsv

if [ ! -e "./runlog.sh" ]; then
  echo "./runlog.sh  must exist"
  exit 1
fi
. ./runlog.sh  


DIRNAME="${DEST_DIR_NAME}"
INFILE="${DEST_FILE_SIZED}"
INFILECORE=$(echo "${INFILE}" | cut -d'-' -f1-7)
INFILECORE=$(echo "${INFILECORE}" | xargs)
 
OUTFILE="${INFILECORE}-matrix_summary .tsv"
MATRIXFILE="${INFILECORE}-matrix.tsv"
 
cat<<EOF

-----
Now we process the labels

debug: data:
DIRNAME    ${DIRNAME}
INFILE     ${INFILE}
INFILECORE ${INFILECORE}
OUTFILE    ${OUTFILE}
MATRIXFILE ${MATRIXFILE}


EOF

rm ./runlog.sh
cp "${DIRNAME}/${INFILE}" "${DIRNAME}/input.tsv"
 
process_labels --input "${DIRNAME}/input.tsv" --output "${DIRNAME}/outputput.tsv" --matrix "${DIRNAME}/matrix.tsv"

rm "${DIRNAME}/input.tsv"
mv "${DIRNAME}/outputput.tsv" "${DIRNAME}/${OUTFILE}"
mv "${DIRNAME}/matrix.tsv" "${DIRNAME}/${MATRIXFILE}"  


cat<<EOF

-----
Finally, tar up the all of the existing results

debug: data:
DIRNAME    ${DIRNAME}
INFILE     ${INFILE}
INFILECORE ${INFILECORE}
OUTFILE    ${OUTFILE}
MATRIXFILE ${MATRIXFILE}

debug:
tar --transform "s|.*/${SPRINTNAME}|./${SPRINTNAME}|" -cvf ${DIRNAME}/${SPRINTNAME}.tar ${DEST_DIR_NAME}  

Creating the tar file in verbose mode.
And then finally printing out what is in it.
EOF
   
tar --transform "s|.*/${SPRINTNAME}|./${SPRINTNAME}|" -cvf ${DIRNAME}/${SPRINTNAME}.tar ${DEST_DIR_NAME}  
tar -tvf ${DIRNAME}/${SPRINTNAME}.tar 