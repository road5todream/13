import argparse


def parse():
    parser = argparse.ArgumentParser(description=' two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser.parse_args()
