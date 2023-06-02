# Introduction

This is our first MVP.  There is no deployment process. To use the software, you can follow these instructions.

## Summary

- Check out the latest code.
- Build and deploy it locally.
   - report any problems as an issue [here](https://github.com/thisaintwork/iqss_gh_reporting/issues/new). 
- create a base directory where you will collect the output from the data collection.
  - Underneath that directory create: ./bin
  - copy example shell script into the bin directory.
- edit and run the example shell script.
 
## Detailed Instructions

### Build and deploy it locally.

After the code is checked out, cd to ./scripts. In that directory run the script [build_and_deploy_local.sh](scripts/build_and_deploy_local.sh). 

The results of running the build and deploy script will look [like this](docs%2Fbuild_and_deploy_locally.md).

Once the code is built and deployed, you can run the tool from the command line or from a shell script.

This is where to find the scripts directory in the code base:

| Directory                                                | Description                                                                 |
|----------------------------------------------------------|-----------------------------------------------------------------------------|
| /home/user1/DevCode/iqss_gh_reporting (specific example) | The base directory: BASECODEDIR of the project. This is the root of the project |
| BASECODEDIR/scripts                                          | The bash scripts related to the project                                     |
| BASECODEDIR/scripts/build_and_deploy_local.sh                | Run this script to build and deploy the code locally                        |
| BASECODEDIR/scripts/example                                  | This is the example BASEDATADIR                                          |
| BASEDATADIR/sprint_2023_05_24                            | The sprint directory for this example                                       |


### Create a base directory for your data collection

The base data collection directory: BASEDATADIR will be the top of the directory tree where the data is collected.

Underneath BASEDATADIR, create the sprint_name directory: SPRINTNAME
BASEDATADIR/SPRINTNAME
e.g.: BASEDATADIR/sprint_2023_05_24 
- All results of the data collection tagged with this sprint name will be deposited in this directory.
- It is **important** that the name of this directory match [the sprint_name in the setup](./docs/example_yaml_file_configuration.md).
- If they don't match the tool will create a new directory with the sprint_name and deposit the results there. This can lead to confusion.

Finally underneath the sprint directory, create the ./bin directory:

BASEDATADIR/SPRINTNAME/bin.

e.g.: BASEDATADIR/sprint_2023_05_24/bin
- The ./bin directory is where you will store the shell scripts that you use to run the tool for this particular sprint

### edit and run the example shell scripts

To explain how to get started running the tool there is an example environment setup in the repo.
- It includes an example shell script that you can use to setup the yaml file that runs the tool.
- It includes an example shell script that you can use to run the tool.

# The example

**To get started you can use the example included in the repo.**

For this example we are going to pretend that we created this BASEDATADIR:

| Directory                          | Description                           |
|------------------------------------|---------------------------------------|
| BASECODEDIR/scripts/example        | our example BASEDATADIR               |
| BASEDATADIR/sprint_2023_05_24      | The sprint directory for this example |
| BASEDATADIR/sprint_2023_05_24/bin  | The bin directory for this example    |

**BASEDATADIR/sprint_2023_05_24**

| File Name                                                                                                          | Description                                                                             |
|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| sprint_2023_05_24-snapshot-example-api-2023_06_02_172814-sized.tsv                                                 | The original data collected from the API                                                |
| sprint_2023_05_24-snapshot-example-api-2023_06_02_172814-matrix.tsv                                                | The original data collected from the API with the addition of the label data            |
| sprint_2023_05_24-snapshot-example-api-2023_06_02_172814-snapshot_summary.tsv                                      | A original data collectedd from the API as a single row of data representing the sprint |
| sprint_2023_05_24_snapshot_example_api_2023_06_02_172814_sized-example-file-2023_06_02_172814-sized.tsv            | The original data re-processed.                                                         |
| sprint_2023_05_24_snapshot_example_api_2023_06_02_172814_sized-example-file-2023_06_02_172814-matrix.tsv           | The original data re-processed.                                                                                        |
| sprint_2023_05_24_snapshot_example_api_2023_06_02_172814_sized-example-file-2023_06_02_172814-snapshot_summary.tsv | The original data re-processed.                                                                                        |

**BASEDATADIR/sprint_2023_05_24/bin**

| File Name                                                                                                      | Description                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [sprint_2023_05_24-api-example.sh](./scripts/example/sprint_2023_05_24/bin/sprint_2023_05_24-api-example.sh)   | Example script to create the yaml file to collect data from the api  |
| [sprint_2023_05_24-file-example.sh](./scripts/example/sprint_2023_05_24/bin/sprint_2023_05_24-file-example.sh) | Example script to create the yaml file to reprocess an existing file |
| [input_file.yaml](./docs/example_yaml_file_configuration.md)                                                                                     | Example yaml file created by the above scripts                            |

Notes on using the setup shell scripts.
- the BASEDATADIR here corresponds to the _output_base_dir_ command line variable. Note that it ends in  "example". This is because the tool will create a subdirectory matching the command line variable _sprint_name_  if it doesn't already exist.
- Be careful when editing to include the ending '\' on all the lines in the command except the last. Not doing this will result in the file only partially modifying the parameters.

Modify the bash path if required. This example was written on ubuntu. 
 