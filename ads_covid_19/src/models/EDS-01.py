import pandas as pd
import subprocess
import os
import requests
from bs4 import BeautifulSoup
import json
import plotly.express as px
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

raw_data_path="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

# reading the data file, source: Our World in Data
raw_df = pd.read_csv(raw_data_path, sep=',')

'''Show the complete data frame'''
raw_df

# Unique command is used to make a list of all the countries available in the data set
raw_df['location'].unique()

df_AFR=raw_df[raw_df['location']=='Africa']
df_AFR=df_AFR.reset_index(drop=True)
df_AFR.columns

fig=px.line(df_AFR, x="date", y= "total_cases",color='location', title= "Graph representing the total case in AFRICA")
fig.show()

dataset_US=raw_df['location']=='United States'
dataset_India=raw_df['location']=='India'
dataset_Germany=raw_df['location']=='Germany'
processed_data= dataset_US | dataset_India | dataset_Germany

df_list=raw_df[processed_data]
df_list
df_list.columns

df_list['total_infection_mean']=df_list['total_cases']/df_list['population']
# Absolute COVID Cases over a Population Size
Rel_Cases=px.line(df_list, x= "date", y= "total_infection_mean",color='location', title= "Relative Cases over time of Covid Infectors")
Rel_Cases.show()

# Vaccination Rate over Time
Vacc_Rate=px.line(df_list, x="date", y="total_vaccination_mean",color='location', title="The Vaccination Rate")
Vacc_Rate.show()