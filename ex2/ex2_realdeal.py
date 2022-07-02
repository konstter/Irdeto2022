#!/usr/bin/env python3

import os
import argparse


def read_files(d):
    result_dict = {}
    q = 0
    for fn in os.listdir(d):
        with open(os.path.join(d, fn), 'r') as f:

            for str in f:
                str_list = str.split(",", 1)
                frame_id = int(str_list[0])

                if frame_id in result_dict:
                    result_dict[frame_id] += 1
                else:
                    result_dict[frame_id] = 1
        q += 1
    return result_dict, q


def analyze(d, pc):
    s = read_files(d)
    r_dict, q = s
    r_list = []
    for key in r_dict:
        part = (r_dict[key] / q) * 100
        if part >= pc:
            r_list.append(key)
    output(r_list)


def output(r_l):
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
