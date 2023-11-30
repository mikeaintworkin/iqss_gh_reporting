#!/usr/bin/bash

# ================================================================================================================
# The objective of this script is to build the current code and deploy it locally.
# MUST be run from the ./iqss_gh_reporting/scripts directory
# e.g /home/barry/PycharmProjects/iqss_gh_reporting/scripts
# where /home/barry/PycharmProjects/iqss_gh_reporting is the root of the project
# ================================================================================================================

DEVHOME="../"


cat<<EOF
============================
Current file: $0
pwd: $(pwd)
venv: <>$(env |grep VIRTUAL_ENV)</>

The script is going to to build the sources and then deploy it with pip

MUST be run from the ./scripts directory in the project tree.
e.g /home/barry/PycharmProjects/iqss_gh_reporting/scripts
where /home/barry/PycharmProjects/iqss_gh_reporting is the root of the project

press <enter> to continue
============================
EOF

read line

pushd ${DEVHOME} || exit 1

cat<<EOF

Building the code here:
${DEVHOME}

EOF




cat<<EOF

Building....

EOF

bash -cl "/usr/bin/python3.10 ./setup.py bdist_wheel"  || exit 1

cat<<EOF

Installing....

EOF

pip install .  || exit 1
popd 


cat<<EOF

============================
current file: $0
pwd: $(pwd)
venv: <>$(env |grep VIRTUAL_ENV)</>


Build and install complete.
The build will put these files and their associated libraries in your path. 
create_iq_snapshot_init
create_iq_snapshot


Next Steps:
() Check that the build actually completed succesfully by reviewing the output.
() Test out the create_iq_snapshot_init build correctly using 

create_iq_snapshot_init --help

() Follow the rest of the instructions in the readme

press <enter> to continue
============================
EOF
read line
