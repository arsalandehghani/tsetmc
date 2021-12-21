#!/usr/bin/env python3

from bs4 import BeautifulSoup
import datetime
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
