#!/usr/bin/python3
import requests
import json
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def job():
        
    base_url = 'https://api.stackexchange.com/2.2/questions?site=stackoverflow'
    response = requests.get(base_url, headers={'Accept-Charset': 'utf-8'})
    data = response.json()

    base_url2 = 'https://api.stackexchange.com/2.2/users?site=stackoverflow'
    response2 = requests.get(base_url2, headers={'Accept-Charset': 'utf-8'})
    data2 = response2.json()

    # print(json.dumps(data, indent=2))
    # print(json.dumps(data2, indent=2))

    df = pd.DataFrame(data["items"])
    df2 = pd.DataFrame(data2["items"])

    # print(df)
    # print(df2)

    # print(df.head())
    # print(df2.head())
    
    merged_df = df.join(df2, lsuffix='_A', rsuffix='_B')
    # print(merged_df)
    merged_df.to_csv('records.csv', index=False)

    print("Report updated!")

scheduler = BackgroundScheduler()
start_time = datetime.now().replace(hour=6, minute=0, second=0, microsecond=0)
scheduler.add_job(job, 'interval', days=1, start_date=start_time, timezone='UTC')
scheduler.start()
