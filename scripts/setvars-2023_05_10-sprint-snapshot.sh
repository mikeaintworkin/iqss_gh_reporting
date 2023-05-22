#!/usr/bin/bash -x

rm ./input_file.yaml

create_iq_snapshot_init \
     --collection_flag "snapshot" \
     --collection_timestamp "" \
     --sprint_name "2023_05_03_sprint" \
     --src_dir_name "" \
     --src_file_name "" \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --src_type "api"\
     --workflow_name "000" \
     --output_base_dir "/mnt/hgfs/iq_reporting_collab/run/out"


cat<<EOF

You have set the run parameters.
To actually run the analysis or collection and analysis run:

create_iq_snapshot


EOF
