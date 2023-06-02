#!/bin/bash

rm ./input_file.yaml

create_iq_snapshot_init \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --sprint_name "sprint_2023_05_24" \
     --src_type "api"\
     --collection_flag "snapshot" \
     --data_collected_time "" \
     --src_dir_name "" \
     --src_file_name "" \
     --output_base_dir "/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example" \
     --output_file_base_name "" \
     --workflow_name "example" 


cat<<EOF
==========================================================================
You have set the run parameters.

Summary:
$(cat ./input_file.yaml | grep : | grep -v h:)

==========================================================================


To actually run the analysis or collection and analysis run

create_iq_snapshot

from this same directory.


EOF
