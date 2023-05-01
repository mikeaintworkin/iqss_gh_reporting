#!python
import argparse
import os
import re
from datetime import datetime
import yaml

from iqss_gh_reporting import legacy_project_cards as pdio
from iqss_gh_reporting import pdata as ghpdata
from iqss_gh_reporting import utils as utils
from iqss_gh_reporting import transformer as transformer


def main():
    mydirs = {"in": "~/iqss_gh_reporting/run/in", "wrk": "~/iqss_gh_reporting/run/wrk", "out": "~/iqss_gh_reporting/run/out"}

    text = \
        "3 directories must exist:\n" \
        + "\n- " + mydirs["in"] \
        + "\n- " + mydirs["wrk"] \
        + "\n- " + mydirs["out"] \
        + "\n" \
        + "\n- " + "if they do not exist they will be created."

    print(f"{text}")

    for d in mydirs.values():
        d = os.path.expanduser(d)
        if not os.path.exists(d):
            # print(f"Creating directory: {d}")
            os.makedirs(d)
        if os.path.exists(d):
            print('.')
            # print('Directories exist')
        else:
            print('Directories missing')

    yaml_file = os.path.expanduser(mydirs["in"] + '/' + 'input_file.yaml')
    if not os.path.exists(yaml_file):
        print(f"Creating file: {yaml_file}")
        default_yaml_contents = \
            '''
            any:
              sprint_name: 'April 12, 2023' 
              collection_flag: 'start' 
              # collection_flag: 'end'
              # collection_flag: 'other'
              dest_dir_name: '~/iqss_gh_reporting/run/out'
              collection_timestamp: None 
    
            api:
              organization_name: 'IQSS'
              project_name: 'IQSS/dataverse'
    
            file: 
              src_file_name: '2023_04_26-17_32_18-output.tsv'
              src_dir_name: '~/iqss_gh_reporting/run/wrk'
            '''
        # print(default_yaml_contents)

        # Validate the YAML string
        try:
            data = yaml.safe_load(default_yaml_contents)
        except yaml.YAMLError as e:
            print(f"YAML syntax error: {e}")
        else:
            print("YAML data is valid!")

        print(default_yaml_contents)

        with open(yaml_file, 'w') as f:
            f.write(default_yaml_contents)

    with open(yaml_file) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    print("------------------------------")
    print(f"Current defaults set in {yaml_file}:")
    yaml_string = yaml.dump(data, default_flow_style=False)
    print(yaml_string)

    long_text = '''
       The relationship between the arguments:\n

       When you run the any of the other scripts in the workflow, they will use the defaults set here.\n
       Those defaults can be over  ridden by passing in command line arguments.\n

       The required argument is the variable: src_type
       This is hardcoded in the workflow.

       When src_type set to 'file' the workflow will read the data from a file and these arguments are used:
        --src_file_name
        --src_dir_name
        --dest_dir_name
        --sprint_name
        --collection_flag
        --collection_timestamp

       When src_type set to 'api' the workflow will read the data from a file and these arguments are used:
       --organization_name
       --project_name
       --dest_dir_name
       --sprint_name
       --collection_flag
       --collection_timestamp
    '''

    parser = argparse.ArgumentParser(
        prog='create_iq_snapshot_init_sprint.py',
        description='run this at the beginning of the sprint to set the defaults for the sprint',
        epilog=long_text)
    # don't allow the dest-dir_name to be set from the command line
    # parser.add_argument('--dest_dir_name', dest='dest_dir_name', default=os.path.expanduser(data['any']['dest_dir_name']), type=str, help='XXX')
    parser.add_argument('--sprint_name', dest='sprint_name', default=data['any']['sprint_name'], type=str, help='XXX')
    parser.add_argument('--collection_flag', dest='collection_flag', default=data['any']['collection_flag'], type=str, help='XXX')
    parser.add_argument('--collection_timestamp', dest='collection_timestamp', default=data['any']['collection_timestamp'], type=str, help='XXX')
    parser.add_argument('--organization_name', dest='organization_name', default=data['api']['organization_name'], type=str, help='XXX')
    parser.add_argument('--project_name', dest='project_name', default=data['api']['project_name'], type=str, help='XXX')
    parser.add_argument('--src_file_name', dest='src_file_name', default=os.path.expanduser(data['file']['src_file_name']), type=str, help='XXX')
    parser.add_argument('--src_dir_name', dest='src_dir_name', default=os.path.expanduser(data['file']['src_dir_name']), type=str, help='XXX')
    args = parser.parse_args()

    print("------------------------------")
    print("Defaults currently mapped to Command Line input:")
    print("Any changes you just made will be written back to the yaml file")
    print("you can run this file repeatedly to update the defaults\n\n")
    args_dict = vars(args)
    yaml_string = yaml.dump(args_dict, default_flow_style=False)
    print(yaml_string)

    data['any']['sprint_name'] = args.sprint_name
    data['any']['collection_flag'] = args.collection_flag
    data['any']['collection_timestamp'] = args.collection_timestamp
    data['api']['organization_name'] = args.organization_name
    data['api']['project_name'] = args.project_name
    data['file']['src_file_name'] = args.src_file_name
    data['file']['src_dir_name'] = args.src_dir_name
    yaml_str = yaml.dump(data, default_flow_style=False, indent=8)
    with open(yaml_file, 'w') as f:
        f.write(yaml_str)


if __name__ == "__main__":
    main()