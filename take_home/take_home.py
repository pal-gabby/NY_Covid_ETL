# -*- coding: utf-8 -*-
"""

@author: Pallavi Arora
"""

import requests
import json
import sqlite3
from datetime import date, datetime
import logging

logger = logging.getLogger()

def get_data():
    url = "https://health.data.ny.gov/api/views/xdss-u53e/rows.json?accessType=DOWNLOAD" 
    response = requests.get(url)
    #print(response)
    data = response.text
    data_dict = json.loads(data)
    return data_dict

def process_data(data_dict):
    county_dict = {}
    column_list = {'test_date':-6,
                   'new_positive':-4,
                   'cum_numb_positive':-3,
                   'tot_num_test_perform':-2,
                   'cum_num_test_perform':-1}
    for row in data_dict["data"]:
        row_dict = {}
        for column,position in column_list.items():
            row_dict[column]= row[position]
        row_dict['load_date'] = str(date.today())
        if row[-5] not in county_dict:        
            county_dict[row[-5]] = [row_dict]
        else:
            county_dict[row[-5]].append(row_dict)
    return county_dict

def insert_into_db(county_dict):
    conn = sqlite3.connect(r'/mnt/c/Users/pallavi/Desktop/take_home/NY_county.db')
    #cursor = conn.cursor()
    for county,county_rows in county_dict.items():
        county = county.replace(' ','_').replace('.','')
        conn.execute('''CREATE TABLE IF NOT EXISTS %s
                 ( test_date date,
                      new_positive int,
                      cum_numb_positive int,
                      tot_num_test_perform int,
                      cum_num_test_perform int,
                      load_date string) '''%(county))
        print(str(datetime.now()) + " :\n")
        print("%s Table Created"%(county))
        for row in county_rows:
            conn.execute("""INSERT INTO """+str(county)+""" VALUES (?,?,?,?,?,?)""",[row['test_date'],
                         row['new_positive'],row['cum_numb_positive'],row['tot_num_test_perform'],
                         row['cum_num_test_perform'],row['load_date'] ])
        print("Records inserted to %s"%(county))
        
    conn.commit()
    conn.close()
        
if __name__=='__main__':
    data_dict =  get_data()
    county_dict = process_data(data_dict)
    insert_into_db(county_dict)
    
        

