#!/usr/bin/env python
# -*- coding=utf-8 -*-


import os
import sys
import json
import nltk


index1 = './Project1_data/DBdoc.json'
index2 = './Project1_data/queries-v2.txt'


def get_data(path):
    # open DBdoc.json file
    data = []
    with open(index1, 'rb') as f:
        raw_data = json.load(f)
        # data is a list consisting many dicts, len=45668, type=list, a dic consists two key-vale pairs
        for i in range(len(raw_data)):
            data.append([raw_data[i]['abstract'], raw_data[i]['entity']])
    return data


def get_query(path):
    # open queries-v2.txt file
    query = []
    with open(index2, 'rb') as f:
        # read all data into ram
        lines = f.readlines()
        # split each line
        for line in lines:
            # split str by "tab"
            list = line.split('\t')
            # delete '\n'
            list[1] = list[1].strip('\n')
            # query is a 2-d array, such as ['INEX_LD-20120111','vietnam war movie']
            query.append(list)
    f.close()
    return query


def main():
    data = get_data(index1)

    query = get_query(index2)
    # print query


if __name__ == '__main__':
    main()
