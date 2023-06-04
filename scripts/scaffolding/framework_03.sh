#!/usr/bin/bash -x
  # ================================================================================================================
  # The objective of this frame is to work through the following steps:
  # - do a full file run
  # - do a full api run
  #
  # ================================================================================================================
DEVHOME=/home/perftest/DevCode/github-com-mreekie/builds
RUNHOME=/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts

echo "\$1 is $1"
if [ "$1" = "dev" ]; then
	DEVHOME=/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting
  RUNHOME=/home/perftest/iqss_gh_reporting/test
fi

pushd ${DEVHOME} || exit 1
pwd
bash -cl "/usr/bin/python3.10 ./setup.py bdist_wheel"  || exit 1
pip install .

pwd
echo "buld complete. return to continue"
read line



cd ${RUNHOME}  || exit 1
rm ./input_file.yaml 
create_iq_snapshot_init \
     --collection_flag "" \
     --sprint_name "sprint_2023_05_24" \
     --src_dir_name "/mnt/hgfs/iq_reporting_collab/sprint_2023_05_10" \
     --src_file_name "sprint_2023_05_10-snapshot-api-2023_05_24_085539-sized.tsv" \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --src_type "file"\
     --workflow_name "test" \
     --output_base_dir "/home/perftest/iqss_gh_reporting/test/print_2023_05_24" \
     --output_file_base_name ""\
     --data_collected_time "2023_05_24_085539"


create_iq_snapshot


echo "return to continue"
read line

#cd ${RUNHOME}  || exit 1
#rm ./input_file.yaml 
#pwd
#create_iq_snapshot_init \
#     --collection_flag "snapshot" \
#     --sprint_name "sprint_2023_05_24" \
#     --src_dir_name "" \
#     --src_file_name "" \
#     --organization_name "IQSS" \
#     --project_name "IQSS/dataverse" \
#     --src_type "api"\
#     --workflow_name "" \
#     --output_base_dir "/home/perftest/iqss_gh_reporting/test" \
#     --output_file_base_name ""
#create_iq_snapshot
#popd
#pwd