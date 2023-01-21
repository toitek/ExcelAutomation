import requests
import json
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
import matplotlib.pyplot as plt
import seaborn as sns

    
base_url1 = 'https://api.stackexchange.com/2.2/questions'
base_url2 = 'https://api.stackexchange.com/2.2/answers'

params1 = {'site':'stackoverflow','sort':'votes','tagged':'python'}
params2 = {'site':'stackoverflow','sort':'votes','tagged':'python'}

response1 = requests.get(base_url1, headers={'Accept-Charset': 'utf-8'},params=params1)
response2 = requests.get(base_url2, headers={'Accept-Charset': 'utf-8'},params=params2)
data1 = response1.json()
data2 = response2.json()


print(json.dumps(data1, indent=2))
print(json.dumps(data2, indent=2))

df1 = pd.DataFrame(data1["items"])
df2 = pd.DataFrame(data2["items"])

# print(df)
# print(df2)

# data cleaning 
df1 =df1[['question_id', 'title', 'creation_date']]
df2 =df2[['question_id', 'answer_id', 'creation_date']]

    
# merged_df = df1.join(df2, lsuffix='_A', rsuffix='_B')
# print(merged_df)
# merged_df.to_csv('records.csv', index=False)

# print("Report updated!")
