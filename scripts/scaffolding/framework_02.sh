#!/usr/bin/bash -x

SCRIPT_DIR="/home/barry/PycharmProjects/iqss_gh_reporting/scripts"
WRK_DIR_RT="/home/barry/Documents/github_reporting/framework_02"
INDIR="${WRK_DIR_RT}/in"
WRKDIR="${WRK_DIR_RT}/wrk"
OUTDIR="${WRK_DIR_RT}/out"

cat<<EOF

--------------------------------
Directories:
SCRIPT_DIR: "${SCRIPT_DIR}"
WRK_DIR_RT: "${WRK_DIR_RT}"
INDIR: "${INDIR}"
WRKDIR: "${WRKDIR}"
OUTDIR: "${OUTDIR}"

-------------------------------
input file:
${INDIR}/${WRK_FILE}

EOF


mkdir -p ${INDIR} || exit 1
mkdir -p ${WRKDIR} || exit 1
mkdir -p ${OUTDIR} || exit 1

# avoid a potention rm /*
rm "${WRK_DIR_RT}/wrk/input.tsv"
rm "${WRK_DIR_RT}/out/*"
cp "${INDIR}/${WRK_FILE}" "${WRKDIR}/input.tsv"

cat<<EOF


--------------------------------
Directories Contents:

$(find "${WRK_DIR_RT}" -type f)

--------------------------------

EOF


cp "${WRK_DIR_RT}/in/${WRK_FILE}" "${WRK_DIR_RT}/wrk/input.tsv"


SPRINTNAME="framework_02"

create_iq_snapshot_init \
     --collection_flag "snapshot" \
     --sprint_name "testing" \
     --src_dir_name "${WRKDIR}" \
     --src_file_name "input.tsv" \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --src_type "file" \
     --output_base_dir "${OUTDIR}" \
     --workflow_name "framework_02"
     

cat<<EOF

-----
kickoff the Test

================================

EOF

${SCRIPT_DIR}/test_frame_02.py \
    --qry
    --org
    --repo
