

## Yaml file contents explained

| Field | src_type=file | src_type=api | Explanation. |
| --- | --- | --- | --- |
| organization_name | **required** | **required** | str: e.g: 'IQSS'. Always required because even when processing from a file, the processing may include attempting to lookup an issue to retrieve additional information.  Avoid the use of any special characters other than '_'. In particular do not use '-' or '.' or ',' |
| project_name | **required** | **required** | str: e.g: IQSS/dataverse. Always required. |
| sprint_name | **required** | **required** | str: e.g. sprint_2023_04_26. Please follow the example convention. 'sprint_YYYY_MM_DD'. This is an important piece of input. It is the means by which the process identifies the sprint during which the data was collected. It is used when processing from the api or from a file. when processing a file, this can be extracted as the first thing in the input file name. |
| src_type | **required** | **required** | valid values: 'api' or 'file'. Always required. indicates to the tool whether you are working on a previously collected set of data. |
| collection_flag | ignored | **required** | str: valid values: 'start' or  'snapshot' or  'end' This flag is just an indicator of the intent when collecting the data via the api. It is used to form the output file name. |
| data_collected_time | **required** | ignored | str: this is required when you are processing previous data. It populates the column in the output data that indicates when the data was originally recorded. use only numbers and underscores. e.g. date '+%Y_%m_%d_%H%M%S'. e.g. 2023_06_02_145217. when src_type=file, this can be extracted as the second to last '-' delimited item in the input file name. |
| src_dir_name | **required** | ignored | str: This is only used when processing data from a file e.g. /mnt/hgfs/iq_reporting_collab/run/out When  processing a file this provides the tool with the source directory of the data. Note that when processing from a file, the input file and output file typically reside in the same directory. This emables the data from a particular run to stay together.  Do not use relative paths. Do not include a trailing slash. Avoid the use of any special characters other  than '_'. In particular do not use '-' or '.' or ',' |
| src_file_name | **required** | ignored | str: e.g: sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig.tsv |
| output_base_dir | optional | ignored | str: This is not typically set. e.g. /mnt/hgfs/iq_reporting_collab/run/out  When  processing a file this provides the option to direct the output to a  particular  directory. Typically the output file is purposely put in the same  directory as  the input file so that all of the data from a particular run  stays together.  Do not use relative paths. Do not include a trailing slash. Avoid the use of any special  characters other  than '_'. In particular do not use '-' or '.' or ',' |
| output_file_base_name | optional | ignored | str: This is not typically set. e.g. sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig.  When processing a file this provides the option to create a file basename for the results. If it is not set, the base output file name will be the input file name without it's extension. Avoid the use of any special characters other than '_'. In particular do not use '-' or '.' or ',' |
| workflow_name | optional | optional | an optional short description or code. Avoid the use of any special characters other than '_'. In particular do not  use '-' or '.' or ',' |


## Sample shell script that configures the input.yaml file:

sprint_2023_05_24-api-example.sh
```
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
``` 


## Sample input.yaml file contents

This yaml file was the result of running the example script above: sprint_2023_05_24-api-example.sh

```
collection_flag:
    h: 'str: valid values: start | snapshot | end. api=required. file=Ignored.'
    v: snapshot
data_collected_time:
    h: 'str: When working with file input,use this.-special_char] ok:''_'' no
        trailing /. api=ignored. file=required.'
    v: ''
organization_name:
    h: 'str: e.g: IQSS. Always required.'
    v: IQSS
output_base_dir:
    h: 'str: /mnt/hgfs/iq_reporting_collab/run/out;no[ ,.-special_char] ok:''_''.
        No trailing /. api=ignored. file=Optional'
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
    h: 'str: e.g: ~/iqss_gh_reporting/run/in no[ ,.-special_char] ok:''_'' no
        trailing /. api=ignored. file=required.'
    v: ''
src_file_name:
    h: 'str: e.g: sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig.tsv
        .api=ignored. file=required.'
    v: ''
src_type:
    h: 'str: valid values: api | file. Always required.'
    v: api
workflow_name:
    h: very short description or code.no[ ,.-special_char] ok:'_' Optional.
    v: example
```
