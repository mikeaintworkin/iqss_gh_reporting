
```
perftest@ubuntu:~/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/sample/sprint_2023_05_24/bin$ ./sprint_2023_05_24-file-example.sh 
YAML data is valid!
------------------------------
Defaults currently mapped to Command Line input:
Any changes you just made will be written back to the yaml file
you can run this file repeatedly to update the defaults


collection_flag:
h: 'str: valid values: start | snapshot | end. api=required. file=Ignored.'
v: ''
data_collected_time:
h: 'str: When working with file input,use this.-special_char] ok:''_'' no
trailing /. api=ignored. file=required.'
v: '2023_06_02_172814'
organization_name:
h: 'str: e.g: IQSS. Always required.'
v: IQSS
output_base_dir:
h: 'str: /mnt/hgfs/iq_reporting_collab/run/out;no[ ,.-special_char] ok:''_''.
No trailing /. api=ignored. file=Optional'
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
h: 'str: e.g: ~/iqss_gh_reporting/run/in no[ ,.-special_char] ok:''_'' no
trailing /. api=ignored. file=required.'
v: /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24
src_file_name:
h: 'str: e.g: sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig.tsv
.api=ignored. file=required.'
v: sprint_2023_05_24-snapshot-example-api-2023_06_02_172814-sized.tsv
src_type:
h: 'str: valid values: api | file. Always required.'
v: file
workflow_name:
h: very short description or code.no[ ,.-special_char] ok:'_' Optional.
v: example

==========================================================================
You have set the run parameters.

Summary:
collection_flag:
v: ''
data_collected_time:
v: '2023_06_02_172814'
organization_name:
v: IQSS
output_base_dir:
v: ''
output_file_base_name:
v: ''
project_name:
v: IQSS/dataverse
sprint_name:
v: sprint_2023_05_24
src_dir_name:
v: /home/perftest/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/example/sprint_2023_05_24
src_file_name:
v: sprint_2023_05_24-snapshot-example-api-2023_06_02_172814-sized.tsv
src_type:
v: file
workflow_name:
v: example

==========================================================================


To actually run the analysis or collection and analysis run

create_iq_snapshot

from this same directory.


perftest@ubuntu:~/DevCode/github-com-mreekie/iqss_gh_reporting/scripts/sample/sprint_2023_05_24/bin$
```