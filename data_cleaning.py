# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:03:49 2020

@author: barad
"""

import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x:x.split('(')[0]) 
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_kd.apply(lambda x:x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x:x.split('-')[0])
df['max_salary'] = min_hr.apply(lambda x:x.split('-')[1])
df[['min_salary','max_salary']] = df[['min_salary','max_salary']].apply(pd.to_numeric)
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#company name only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis =1)

#state field
df['job_State'] = df['Location'].apply(lambda x:x.split(',')[1])
df['job_State'].value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis =1)
df['same_state'].value_counts()

#age of company

df['age'] = df['Founded'].apply(lambda x:x if x< 0 else 2020-x )

#parsing of job description
skills = ['python','rstudio','excel','tableau','spark','sql','aws']

for skill in skills:
  df[skill + '_yn']  = df['Job Description'].apply(lambda x: 1 if skill in x.lower() else 0)
    
df.python_yn.value_counts()

df.columns
df.drop(['Unnamed: 0'], axis =1, inplace = True )

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    