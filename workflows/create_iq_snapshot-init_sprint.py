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
    mydirs = { "in": "~/iqss_gh_reporting/run/in", "wrk": "~/iqss_gh_reporting/run/wrk", "out":"~/iqss_gh_reporting/run/out"}

    text = \
        "3 directories must exist:\n" \
        + "\n- " + mydirs["in"] \
        + "\n- " + mydirs["wrk"] \
        + "\n- " + mydirs["out"] \
        + "\n" \
        + "\n- " + "testing for their existence now." \
        + "\n- " + "if they do not exist they will be created."

    print(f"{text}")

    for d in mydirs.values():
        d = os.path.expanduser(d)
        if not os.path.exists(d):
            print(f"Creating directory: {d}")
            os.makedirs(d)
        if os.path.exists(d):
            print('Directories exist')
        else:
            print('Directories missing')

    yaml_file = os.path.expanduser(mydirs["in"] + '/' + 'input_file.yaml')
    if not os.path.exists(yaml_file):
        print(f"Creating file: {yaml_file}")
        default_yaml_contents = "" \
            + "\n" + "  any:" \
            + "\n" + "    sprint_name: 'April 12, 2023'" \
            + "\n" + "    collection_flag: 'start'" \
            + "\n" + "    # collection_flag: 'end'" \
            + "\n" + "    # collection_flag: 'other'" \
            + "\n" + "    dest_dir_name: '~/iqss_gh_reporting/run/out'" \
            + "\n" + "    collection_timestamp: None" \
            + "\n"  \
            + "\n" + "  api:" \
            + "\n" + "    organization_name: 'IQSS'" \
            + "\n" + "    project_name: 'IQSS/dataverse'" \
            + "\n"  \
            + "\n" + "  file:" \
            + "\n" + "    src_file_name: '2023_04_26-17_32_18-output.tsv'" \
            + "\n" + "    src_dir_name: '~/iqss_gh_reporting/run/wrk'"

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


    print(f"Current defaults set in:{yaml_file}")
    yaml_string = yaml.dump(data, default_flow_style=False)
    print(yaml_string)
    print("------------------------------")


    parser = argparse.ArgumentParser(
        prog='create_iq_snapshot-init_sprint.py',
        description='run this at the beginning of the sprint to set the defaults for the sprint',
        epilog='<>')
    parser.add_argument('--dest_dir_name', dest='dest_dir_name', default=data['any']['dest_dir_name'], type=str, help='XXX')
    parser.add_argument('--sprint_name', dest='sprint_name', default=data['any']['sprint_name'], type=str, help='XXX')
    parser.add_argument('--collection_flag', dest='collection_flag', default=data['any']['collection_flag'], type=str, help='XXX')
    parser.add_argument('--collection_timestamp', dest='collection_timestamp', default=data['any']['collection_timestamp'], type=str, help='XXX')
    parser.add_argument('--organization_name', dest='organization_name', default=data['api']['organization_name'], type=str, help='XXX')
    parser.add_argument('--project_name', dest='project_name', default=data['api']['project_name'], type=str, help='XXX')
    parser.add_argument('--src_file_name', dest='src_file_name', default=data['file']['src_file_name'], type=str, help='XXX')
    parser.add_argument('--src_dir_name', dest='src_dir_name', default=data['file']['src_dir_name'], type=str, help='XXX')
    args = parser.parse_args()

    print("Defaults currently mapped to Command Line input:")
    args_dict = vars(args)
    yaml_string = yaml.dump(args_dict, default_flow_style=False)
    print(yaml_string)

    print("you can run this file repeatedly to update the defaults")
    long_text = '''
    The relationship between the arguments:
    
    When you run the any of the other scripts in the workflow, they will use the defaults set here.
    Those defaults can be over  ridden by passing in command line arguments.
    
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
    print(long_text)

    data['any']['dest_dir_name'] = args.dest_dir_name
    data['any']['sprint_name'] = args.sprint_name
    data['any']['collection_flag'] = args.collection_flag
    data['any']['collection_timestamp'] = args.collection_timestamp
    data['api']['organization_name'] = args.organization_name
    data['api']['project_name'] = args.project_name
    data['file']['src_file_name'] = args.src_file_name
    data['file']['src_dir_name'] = args.src_dir_name
    yaml_str = yaml.dump(data, default_flow_style=False)
    with open(yaml_file, 'w') as f:
        f.write(yaml_str)


if __name__ == "__main__":
    main()