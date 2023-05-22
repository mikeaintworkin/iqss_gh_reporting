#!/usr/bin/bash

rm ./input_file.yaml

create_iq_snapshot_init \
     --collection_flag "snapshot" \
     --sprint_name "sprint_2023_05_03" \
     --src_dir_name "" \
     --src_file_name "" \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --src_type "api"\
     --workflow_name "000" \
     --output_base_dir "/mnt/hgfs/iq_reporting_collab/"


cat<<EOF

You have set the run parameters.
To actually run the analysis or collection and analysis run

create_iq_snapshot

from this same directory.

EOF
