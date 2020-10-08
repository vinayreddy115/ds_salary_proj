# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:09:17 2020

@author: barad
"""

import glassdoor_scraper as gs 
import pandas as pd 


path = "D:/Professional Stuff/Projects/ds_salary_proj/chromedriver_win32/chromedriver"
df = gs.get_jobs('data scientist',1000, False, path, 15)

df1 = gs.get_jobs('data scientist',10000, False, path, 15)
df.to_csv('glassdoor_jobs.csv', index = False)
df1.to_csv('glassdoor_jobs1.csv', index = False)
