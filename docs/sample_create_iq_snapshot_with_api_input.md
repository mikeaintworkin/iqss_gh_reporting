
```
perftest@ubuntu:~/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/sample/sprint_2023_05_24/bin$ create_iq_snapshot
Running /home/perftest/.local/bin/create_iq_snapshot as the main program
YAML data is valid!
input arguments:
​
collection_flag:
h: 'str: valid values: start | snapshot | end. api=required. file=Ignored.'
v: snapshot
data_collected_time:
h: 'str: When working with file input,use this.-special_char] ok:''_'' no trailing
/. api=ignored. file=required.'
v: ''
organization_name:
h: 'str: e.g: IQSS. Always required.'
v: IQSS
output_base_dir:
h: 'str: /mnt/hgfs/iq_reporting_collab/run/out;no[ ,.-special_char] ok:''_''. No
trailing /. api=ignored. file=Optional'
v: /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example
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
v: ''
src_file_name:
h: 'str: e.g: sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig.tsv .api=ignored.
file=required.'
v: ''
src_type:
h: 'str: valid values: api | file. Always required.'
v: api
workflow_name:
h: very short description or code.no[ ,.-special_char] ok:'_' Optional.
v: example
​
output_file_base_name 4api: sprint_2023_05_24-snapshot-example-api-2023_06_02_171412
directory exists or was created now: /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24
projects: looking to match IQSS/dataverse with IQSS/dataverse
start: 0 cards processed: IQSS/dataverse, Column ▶ SPRINT READY
end: 17 cards processed: IQSS/dataverse, Column ▶ SPRINT READY
start: 17 cards processed: IQSS/dataverse, Column This Sprint 🏃♀️ 🏃
end: 19 cards processed: IQSS/dataverse, Column This Sprint 🏃♀️ 🏃
start: 19 cards processed: IQSS/dataverse, Column IQSS Team - In Progress  💻
end: 24 cards processed: IQSS/dataverse, Column IQSS Team - In Progress  💻
start: 24 cards processed: IQSS/dataverse, Column Ready for Review ⏩
end: 32 cards processed: IQSS/dataverse, Column Ready for Review ⏩
start: 32 cards processed: IQSS/dataverse, Column In Review 🔎
end: 35 cards processed: IQSS/dataverse, Column In Review 🔎
start: 35 cards processed: IQSS/dataverse, Column Ready for QA ⏩
end: 36 cards processed: IQSS/dataverse, Column Ready for QA ⏩
start: 36 cards processed: IQSS/dataverse, Column QA ✅
end: 40 cards processed: IQSS/dataverse, Column QA ✅
start: 40 cards processed: IQSS/dataverse, Column Done 🚀
>>>>>> 50 # cards IQSS/dataverse: Done 🚀             ,PullRequest ,9175,dataverse ,DANS - Exporters in external jars
>>>>>> 100 # cards IQSS/dataverse: Done 🚀             ,PullRequest ,9528,dataverse ,update oauth2-oidc-sdk
>>>>>> 150 # cards IQSS/dataverse: Done 🚀             ,PullRequest ,9437,dataverse ,update link in harvestserver.rst
>>>>>> 200 # cards IQSS/dataverse: Done 🚀             ,Issue ,24,dataverse-pm ,Spike: Inventory and prioritize all existing Harvesting related issues
>>>>>> 250 # cards IQSS/dataverse: Done 🚀             ,Issue ,9110,dataverse ,NetCDF/HDF5/geospatial discovery
>>>>>> 300 # cards IQSS/dataverse: Done 🚀             ,PullRequest ,8906,dataverse ,8859 update api error msg
>>>>>> 350 # cards IQSS/dataverse: Done 🚀             ,PullRequest ,8747,dataverse ,Gdcc/8746 single version semantics for archiving
>>>>>> 400 # cards IQSS/dataverse: Done 🚀             ,PullRequest ,8682,dataverse ,SWORD: if custom terms disabled, report error #8580
>>>>>> 450 # cards IQSS/dataverse: Done 🚀             ,PullRequest ,8586,dataverse ,7565 simplify ajax bootstrap
>>>>>> 500 # cards IQSS/dataverse: Done 🚀             ,Issue ,8388,dataverse ,As someone approving pull requests, I want automation to move them in to QA like before
>>>>>> 550 # cards IQSS/dataverse: Done 🚀             ,PullRequest ,8304,dataverse ,adding API Token to Aux Files docs
end: 591 cards processed: IQSS/dataverse, Column Done 🚀
required list entries: ['Project', 'Column', 'Type', 'Number', 'Labels', 'Repo', 'State']
submitted list entries: Index(['Project', 'Column', 'Card', 'CardURL', 'Type', 'Number', 'Labels',
'Repo', 'State', 'CreatedAt', 'UpdatedAt', 'ClosedAt', 'ClosedBy',
'Title'],
dtype='object')
All desired entries are present.
Saving result to file.
/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24/sprint_2023_05_24-snapshot-example-api-2023_06_02_171412-sized.tsv
required list entries: ['Project', 'Column', 'Type', 'Number', 'Labels', 'Repo', 'State']
submitted list entries: Index(['Project', 'Column', 'Card', 'CardURL', 'Type', 'Number', 'Labels',
'Repo', 'State', 'CreatedAt', 'UpdatedAt', 'ClosedAt', 'ClosedBy',
'Title', 'Size'],
dtype='object')
All desired entries are present.
Saving results to file.
/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24/sprint_2023_05_24-snapshot-example-api-2023_06_02_171412-matrix.tsv
/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24/sprint_2023_05_24-snapshot-example-api-2023_06_02_171412-matrix.tsv
Values: ['This Sprint 🏃\u200d♀️ 🏃', 'IQSS Team - In Progress  💻', 'Ready for Review ⏩', 'In Review 🔎']
Values: ['This Sprint 🏃\u200d♀️ 🏃', 'IQSS Team - In Progress  💻', 'Ready for Review ⏩', 'In Review 🔎']
Saving results to file.
/home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24/sprint_2023_05_24-snapshot-example-api-2023_06_02_171412-snapshot_summary.tsv
perftest@ubuntu:~/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/sample/sprint_2023_05_24/bin$
```