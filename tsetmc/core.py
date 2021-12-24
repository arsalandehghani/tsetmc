#!/usr/bin/env python3

from bs4 import BeautifulSoup
import datetime
import numpy as np
import os
import pandas as pd
import requests
import re

def read_tsetmc_groups_dictionary():
    url = 'http://www.tsetmc.com/Loader.aspx?ParTree=111C1213'
    page = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    table_rows = soup.find_all('tr')
    regexPattern = "<td>(\d+)\s+?</td>\s+?<td>(.*?)</td>"
    dicGroups = {}
    x = re.search(regexPattern, str(table_rows[1]), re.U)
    for tr in table_rows:
        x = re.search(regexPattern, str(tr), re.U)
        if x:
            code = x.group(1)
            desc = x.group(2)
            dicGroups[code] = desc
    return dicGroups

def convert_dictionary_to_DataFrame(dic, keyColumnName='k', valueColumnName='v'):
    new_data_frame = pd.DataFrame(list(dic.items()), columns=[keyColumnName, valueColumnName])
    return new_data_frame

def read_tsetmc_groups_DataFrame1():
    dicGroups = read_tsetmc_groups_dictionary()
    dataFrameGroups = convert_dictionary_to_DataFrame(dicGroups, keyColumnName='groupKey', valueColumnName='groupName')
    return dataFrameGroups


def read_tsetmc_groups_DataFrame():
    url = 'http://www.tsetmc.com/Loader.aspx?ParTree=111C1213'
    page = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    table_rows = soup.find_all('tr')
    regexPattern = "<td>(\d+)\s+?</td>\s+?<td>(.*?)</td>"
    arrGroups = np.array()
    columns=['groupKey', 'groupName']
    x = re.search(regexPattern, str(table_rows[1]), re.U)
    for tr in table_rows:
        x = re.search(regexPattern, str(tr), re.U)
        if x:
            code = x.group(1)
            desc = x.group(2)
            arrGroups.add([code, desc])
    group_DataFrame = pd.DataFrame(arrGroups, columns)
    return group_DataFrame

def read_tsetmc_groups_DataFrame_pd():
    url = 'http://www.tsetmc.com/Loader.aspx?ParTree=111C1213'
    page = requests.get(url, allow_redirects=True)
    tables = pd.read_html(page.content, encoding="UTF-8")
    if len(tables)>0:
        return tables[0]
    else:
        return None
