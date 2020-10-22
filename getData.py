# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:52:44 2020

@author: schkorf1
"""


import requests
import pandas as pd

# https://projects.fivethirtyeight.com/polls/president-general/
url = 'https://projects.fivethirtyeight.com/polls-page/president_polls.csv'
r = requests.get(url, allow_redirects=True)

fileName='president_polls.csv'

#open(fileName, 'wb').write(r.content)
with open(fileName, 'wb') as f:
    f.write(r.content)


myData=pd.read_csv(fileName)


# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

# Get all the possible parties
