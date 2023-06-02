#!/usr/bin/bash

# ================================================================================================================
# The objective of this script is to build the current code and deploy it locally.
#
# ================================================================================================================

DEVHOME="../"


echo<<EOF
============================

This assumes that you are running the from the ./scripts directory in the project tree.
That would make the directory above it the root of the project
The script is going to to build the sources and then deploy it with pip to your local environment.

============================
EOF

pushd ${DEVHOME} || exit 1

echo<<EOF

Building the code here:
${DEVHOME}

EOF


bash -cl "/usr/bin/python3.10 ./setup.py bdist_wheel"  || exit 1
pip install .  || exit 1
popd 

echo<<EOF
============================
Build complete.
pwd: $(pwd)
============================

EOF
