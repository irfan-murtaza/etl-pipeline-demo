from etl import extract, transform, load

if __name__ == "__main__":
    raw_data = extract.from_csv("data/sample_data.csv")
    cleaned_data = transform.clean_data(raw_data)
    load.to_postgres(cleaned_data)
