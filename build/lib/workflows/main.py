import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='The first argument')
    parser.add_argument('arg2', help='The second argument')
    args = parser.parse_args()

    print(f'arg1: {args.arg1}')
    print(f'arg2: {args.arg2}')
