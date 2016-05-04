#!/usr/bin/python

import json
import yaml
import pandas as pd
import numpy as np
import ujson


"""
JSON files are loaded in and parsed with utf-8 with yaml
"""

json_files =[
        "datasets/yelp_academic_dataset_tip.json",
        "datasets/yelp_academic_dataset_business.json",
        "datasets/yelp_academic_dataset_checkin.json",
        "datasets/yelp_academic_dataset_user.json",
        "datasets/yelp_academic_dataset_review.json"
        ]

csv_files = [
        "datasets/AllViolations.csv",
        "datasets/restaurant_ids_to_yelp_ids.csv"
        ]

def load_csv_document(f_name):
    document  = pd.read_csv(f_name)
    return document
def load_json_document(f_name):
    document = []
    file = open(f_name,'r')
    for line in file.readlines():
        line = line.split("\n")[0]
        line = yaml.safe_load(line)
        document.append(line)

    return document

def show(f_name):
    print f_name
    print load_json_document(f_name)[0].keys()

show(json_files[0])


