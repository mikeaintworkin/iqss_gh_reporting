# Directory Structure
This example is based on Mike's setup.

I'm working on an ubuntu VM on my windows machine.
There is a shared folder between the two machines.
This same folder is shared via microsoft one drive on the windows machine.
/mnt/hgfs/iq_reporting_collab
C:\Users\user1\OneDrive - Harvard University\iq_reporting_collab

The ubuntu directory structure under the shared folder still needs some cleanup as of this writing.
However this is the standard that I'll be using going forward.

| directory       | example                   | description                                                                                                                                  |
|-----------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|     
| ./SPRINT_NAME  | ./sprint_2023_05_03       | created by the tool based on the YAML file entry for the sprint name. <br/>All runs are deposited here                                       |
| ./SPRINT_NAME/bin  | ./sprint_2023_05_03/bin   | manually created. The setup scripts live here. e.g. setvars-sprint_2023_05_10-snapshot-api.sh<br/>The yaml file is generated and lives here. |
| ./SPRINT_NAME/start   | ./sprint_2023_05_03/start | manually created. The first data collected is manually selected and moved from ../ to here                                                   |
| ./SPRINT_NAME/start   | ./sprint_2023_05_03/end   | manually created. The last  data collected is manually selected and moved from ../ to here                                                   |



# File Names
Example generated output directory base for src_type = api

| dest_dir_name                 | /sprint_name       |
|-------------------------------|--------------------|
| /mnt/hgfs/iq_reporting_collab | /sprint_2023_05_03 |

Example generated output file base name for src_type = api

| sprint_name       | -collection_flag | -workflow_name | -src_type  | -(timestamp)         |
|-------------------|------------------|----------------|------------|----------------------|
| sprint_2023_05_03 | -snapshot        | -000           | -api       | -(automatically_set) |


Example generated output directory base for src_type = file

In the case where the output_base_dir is not defined, the output_base_dir is input directory.
This is good practice as you will want the output files to be in the same directory as the source files. The workflow name and timestamp will be used to delineate between objectives.

| dest_dir_name (same as input directory)         |
|-------------------------------------------------|
| /mnt/hgfs/iq_reporting_collab/sprint_2023_05_03 | 


Example generated output file base name for src_typ = file 

| output_file_base_name                                        | -workflow_name  | -src_type    | -(timestamp)         | 
|--------------------------------------------------------------|-----------------|--------------|----------------------|
| sprint_2023_05_03-snapshot-2023_05_22-07_34_32-api-000-sized | -re_run_00      | -file        | -(automatically_set) |


## Sample script for configurations

Before running this, setup a directory structure like this:

A standard place to run from. 
Once this is chosen, always launch and run from this directory.
This directory is where the input.yaml file will be created.

e.g.

``` 
mkdir -p /home/user/iqss_gh_reporting/
cd /home/user/iqss_gh_reporting/
```

A standard place to store your data
e.g.
```/mnt/hgfs/iq_reporting_collab/```

### example API - setvars-sprint_2023_05_10-snapshot-api.sh
```
#!/usr/bin/bash

rm ./input_file.yaml

create_iq_snapshot_init \
     --collection_flag "snapshot" \
     --sprint_name "sprint_2023_05_10" \
     --src_dir_name "" \
     --src_file_name "" \
     --organization_name "IQSS" \
     --project_name "IQSS/dataverse" \
     --src_type "api"\
     --workflow_name "tst" \
     --output_base_dir "/mnt/hgfs/iq_reporting_collab/" \
     --output_file_base_name ""


cat<<EOF

You have set the run parameters.
To actually run the analysis or collection and analysis run

create_iq_snapshot

from this same directory.

EOF
```

### Example - FILE - setvars-sprint_2023_05_10-snapshot-file.sh
The file runs are tricky in that you are naming a specific input file.
The input file is a snapshot file that was created by a previous run.


```
#!/usr/bin/bash

rm ./input_file.yaml

create_iq_snapshot_init \
     --collection_flag "" \
     --sprint_name "" \
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
```


## Sample input.yaml

```
collection_flag:
        h: 'str: valid values: start | snapshot | end. api=required. file=Ignored.'
        v: snapshot
organization_name:
        h: 'str: e.g: IQSS. Always required.'
        v: IQSS
output_base_dir:
        h: 'str: /mnt/hgfs/iq_reporting_collab/run/out;no[ ,.-special_char] ok:''_''.
                No trailing /. api=ignored. file=Optional'
        v: /mnt/hgfs/iq_reporting_collab/run/out
output_file_base_name:
        h: 'str: e.g. sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig  .api=ignored.
                file=not required.'
        v: sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig
project_name:
        h: 'str: e.g: IQSS/dataverse. Always required.'
        v: IQSS/dataverse
sprint_name:
        h: 'str: e.g. sprint_2023_04_26;no[ ,.-special_char] ok:''_''; api=required.file=Ignored.'
        v: sprint2023_05_03
src_dir_name:
        h: 'str: e.g: ~/iqss_gh_reporting/run/in no[ ,.-special_char] ok:''_'' no
                trailing /. api=ignored. file=required.'
        v: ''
src_file_name:
        h: 'str: e.g: sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig.tsv
                .api=ignored. file=required.'
        v: sprint_2023_05_03-snapshot-2023_05_22_11_00-api-000-orig.tsv
src_type:
        h: 'str: valid values: api | file. Always required.'
        v: api
workflow_name:
        h: very short description or code.no[ ,.-special_char] ok:'_' Optional.
        v: '000'

```
