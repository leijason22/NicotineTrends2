#CDC API
import requests
import pandas as pd

def fetch_cdc_data():
    url = "https://data.cdc.gov/resource/escb-scz6.json"
    response = requests.get(url)

    data = response.json()
    df_cdc = pd.DataFrame(data)

    df_cdc.to_csv('../data/cdc_data.csv', index=False)

fetch_cdc_data()