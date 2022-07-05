#!/usr/bin/python

import os
import argparse


def read_files(d):
    '''
    Read all files in directory
    '''
    # Use dictionary to collect of statics 
    result_dict = {}
    q = 0
    for fn in os.listdir(d):
        with open(os.path.join(d, fn), 'r') as f:

            for str in f:
                str_list = str.split(",", 1)
                frame_id = int(str_list[0])

                if frame_id in result_dict:
                    # If frame_id is in dict - increase its statistics
                    result_dict[frame_id] += 1
                else:
                    # If frame_id isn't in dict - create a new key
                    result_dict[frame_id] = 1
        # Count of files
        q += 1
    return result_dict, q


def analyze(d, pc):
    '''
    Analyze frame_numbers in files
    '''
    s = read_files(d)
    r_dict, q = s
    r_list = []
    for key in r_dict:
        # Determine the percentage of each frame_number
        part = (r_dict[key] / q) * 100
        if part >= pc:
            # If a percentage of a frame_number is not less than P - 
            # append it to result list
            r_list.append(key)
    output(r_list)


def output(r_l):
    '''
    Write result list to a file
    '''
    r_l.sort()
    lenght = len(r_l)
    with open('output.txt', 'w') as f:
        for i in range(lenght):
            if i == lenght - 1:
                f.write(str(r_l[i]))
            else:
                f.write(str(r_l[i])+',')


def create_parser():
    '''
    Start bash parser
    '''
    parser = argparse.ArgumentParser()
    h1_mes = 'A directory to analyze files'
    h2_mes = 'A percentage'
    parser.add_argument('-d', help=h1_mes)
    parser.add_argument('-p', help=h2_mes)
    return parser


def driver():
    '''
    Initial with default or user options
    '''
    args = create_parser().parse_args()
    directory = 'test_algorithm'
    percentage = 50

    if args.d:
        directory = args.d
    if args.p:
        percentage = args.p

    analyze(directory, float(percentage))


if __name__ == '__main__':

    driver()
