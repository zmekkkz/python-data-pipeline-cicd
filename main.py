import pandas as pd
import requests

def extract() -> list:
    req = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
    data_json = req.json()
    data = data_json['data']
    return data

def transform(data) -> pd.DataFrame:
    df = pd.DataFrame(data)
    return df

def load(data):
    data.to_csv('population_data_test.csv', index=False)
    print("Data loaded into population_data.csv")
def main():
    print("Starting data pipeline...")
    data = extract()
    data = transform(data)
    load(data)
    print("Pipeline finished.")

if __name__ == "__main__":
    main()
