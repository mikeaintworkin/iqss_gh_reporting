#!/usr/bin/bash

rm ./input_file.yaml

create_iq_snapshot_init \
     --collection_flag "snapshot" \
     --sprint_name "sprint_2023_05_10" \
     --src_dir_name "/mnt/hgfs/iq_reporting_collab/sprint_2023_05_10" \
     --src_file_name "sprint_2023_05_10-snapshot-api-000-20230522204509-orig.tsv" \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --src_type "file"\
     --workflow_name "tst" \
     --output_base_dir "" \
     --output_file_base_name ""


cat<<EOF

You have set the run parameters.
To actually run the analysis or collection and analysis run

create_iq_snapshot

from this same directory.

EOF
