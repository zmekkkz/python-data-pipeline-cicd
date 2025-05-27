import time

def extract():
    print("Extracting data...")
    return [1, 2, 3, 4, 5]

def transform(data):
    print("Transforming data...")
    return [x * 2 for x in data]

def load(data):
    print("Loading data...")
    print("Loaded data:", data)

def main():
    print("Starting data pipeline...")
    data = extract()
    data = transform(data)
    load(data)
    print("Pipeline finished.")

if __name__ == "__main__":
    main()
