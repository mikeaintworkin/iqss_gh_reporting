
```
perftest@ubuntu:~/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/sample/sprint_2023_05_24/bin$ create_iq_snapshot
Running /home/perftest/.local/bin/create_iq_snapshot as the main program
YAML data is valid!
input arguments:
​
collection_flag:
h: 'str: valid values: start | snapshot | end. api=required. file=Ignored.'
v: ''
data_collected_time:
h: 'str: When working with file input,use this.-special_char] ok:''_'' no trailing
/. api=ignored. file=required.'
v: '2023_06_02_172814'
organization_name:
h: 'str: e.g: IQSS. Always required.'
v: IQSS
output_base_dir:
h: 'str: /mnt/hgfs/iq_reporting_collab/run/out;no[ ,.-special_char] ok:''_''. No
trailing /. api=ignored. file=Optional'
v: ''
output_file_base_name:
h: 'str: e.g. sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig  .api=ignored.
file=not required.'
v: ''
project_name:
h: 'str: e.g: IQSS/dataverse. Always required.'
v: IQSS/dataverse
sprint_name:
h: 'str: e.g. sprint_2023_04_26;no[ ,.-special_char] ok:''_''; api=required.file=required.'
v: sprint_2023_05_24
src_dir_name:
h: 'str: e.g: ~/iqss_gh_reporting/run/in no[ ,.-special_char] ok:''_'' no trailing
/. api=ignored. file=required.'
v: /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24
src_file_name:
h: 'str: e.g: sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig.tsv .api=ignored.
file=required.'
v: sprint_2023_05_24-snapshot-example-api-2023_06_02_172814-sized.tsv
src_type:
h: 'str: valid values: api | file. Always required.'
v: file
workflow_name:
h: very short description or code.no[ ,.-special_char] ok:'_' Optional.
v: example
​
directory exists or was created now: /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24
Reading in data from a file.
input file directory: /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24, input file name: sprint_2023_05_24-snapshot-example-api-2023_06_02_172814-sized.tsv
input_file: /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24/sprint_2023_05_24-snapshot-example-api-2023_06_02_172814-sized.tsv
required list entries: ['Project', 'Column', 'Type', 'Number', 'Labels', 'Repo', 'State']
submitted list entries: Index(['Project', 'Column', 'Card', 'CardURL', 'Type', 'Number', 'Labels',
'Repo', 'State', 'CreatedAt', 'UpdatedAt', 'ClosedAt', 'ClosedBy',
'Title', 'Size'],
dtype='object')
All desired entries are present.
Saving result to file.
/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24/sprint_2023_05_24_snapshot_example_api_2023_06_02_172814_sized-example-file-2023_06_02_172814-sized.tsv
required list entries: ['Project', 'Column', 'Type', 'Number', 'Labels', 'Repo', 'State']
submitted list entries: Index(['Project', 'Column', 'Card', 'CardURL', 'Type', 'Number', 'Labels',
'Repo', 'State', 'CreatedAt', 'UpdatedAt', 'ClosedAt', 'ClosedBy',
'Title', 'Size'],
dtype='object')
All desired entries are present.
Saving results to file.
/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24/sprint_2023_05_24_snapshot_example_api_2023_06_02_172814_sized-example-file-2023_06_02_172814-matrix.tsv
/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24/sprint_2023_05_24_snapshot_example_api_2023_06_02_172814_sized-example-file-2023_06_02_172814-matrix.tsv
Values: ['This Sprint 🏃\u200d♀️ 🏃', 'IQSS Team - In Progress  💻', 'Ready for Review ⏩', 'In Review 🔎']
Values: ['This Sprint 🏃\u200d♀️ 🏃', 'IQSS Team - In Progress  💻', 'Ready for Review ⏩', 'In Review 🔎']
Saving results to file.
/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24/sprint_2023_05_24_snapshot_example_api_2023_06_02_172814_sized-example-file-2023_06_02_172814-snapshot_summary.tsv
perftest@ubuntu:~/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/sample/sprint_2023_05_24/bin$
​
```