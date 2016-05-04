#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Extracting features for predictive model

"""

import pandas as pd
import numpy as np
from pandas.io.sql import frame_query
from db.models import db_connect


def load_table(table_name):
    engine = db_connect()
    conn = engine.raw_connection()
    data = frame_query("SELECT * from reviews",conn)
    return data

if __name__ == '__main__':
    table = load_table("review")
    print(table.head())

