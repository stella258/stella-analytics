# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:54:16 2021

@author: 91705
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('C:/Users/91705/Desktop/Py Work/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('C:/Users/91705/Desktop/Py Work/pooja.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('C:/Users/91705/Desktop/Py Work/User_Data.xlsx')

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('C:/Users/91705/Desktop/Py Work/pooja.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)
