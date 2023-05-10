#!/usr/bin/bash
set -o errexit

# ###########################################################
# Initialize the environment and global variables.
# -----------------------------------------------------------
. ./environment.sh

# ###########################################################
# LOCAL VARIABLE CUSTOMIZATION
# -----------------------------------------------------------

# override the RUNDIR here
#RUNDIR=.


cat<<EOF

# ###########################################################
# Announcement
# -----------------------------------------------------------
# https://cli.github.com/manual/index
# Begin: $0
EOF

# ###########################################################
# Declare input variables
# from the command line
# -----------------------------------------------------------
REPOSLIST=${1}
LABELSLIST=${2}

COUNT=0
while read -r LABELLINE || [ -n "$LABELLINE" ]
do
  echo "--- LABELLINE: ${LABELLINE}"

  LBLNAME=$(echo "${LABELLINE}" | cut -f1)
  LBLDESC=$(echo "${LABELLINE}" | cut -f2)
  LBLCLR=$(echo "${LABELLINE}" | cut -f3)

  while read -r REPOLINE || [ -n "$REPOLINE" ]
  do
    echo "--- --- REPOLINE: ${REPOLINE}"
       #echo ${REPOLINE}
      # gh label create 'Feature: Search/Browse' -c 'c7def8' --force --repo 'IQSS/dataverse-pm'
      CMDNOW="gh label create ${LBLNAME} -d ${LBLDESC} -c ${LBLCLR} --force --repo ${REPOLINE}"
      echo ${CMDNOW}
      eval ${CMDNOW}
      EVAL_RETURN=$?
      [ ${EVAL_RETURN} != "0" ] && EVAL_RETURN="ERROR"
      sleep 2
  done < ${RELINPUTDIR}/${REPOSLIST}.txt
  COUNT=$((COUNT+1))
done < ${RELINPUTDIR}/${LABELSLIST}.txt

cat<<EOF
# End: $0
#---------------------------
EOF
