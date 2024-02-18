import requests
import pandas as pd
import os

def download_tsv_from_google_sheet(sheet_url):
    # Modify the Google Sheet URL to export it as TSV
    tsv_url = sheet_url.replace('/edit#gid=', '/export?format=tsv&gid=')
    
    # Send a GET request to download the TSV file
    response = requests.get(tsv_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Read the TSV content into a pandas DataFrame
        from io import StringIO
        tsv_content = StringIO(response.text)
        df = pd.read_csv(tsv_content, sep='\t')
        return df
    else:
        print("Failed to download the TSV file.")
        return None

# Example usage (URL would need to be replaced with your actual Google Sheet URL)
catalog_url="https://docs.google.com/spreadsheets/d/181EDfwZNtHgHFOMaKNtgKssrYDX4tXTJ9POMzBsCRlI/edit#gid=0"
df_catalog = download_tsv_from_google_sheet(catalog_url)
print(df_catalog.sample(1))

# Get the current date in the format YYYYMMDD
today = pd.Timestamp.now().strftime("%Y%m%d")

filename = f"pl-asr-speech-datasets-catalog-{today}.tsv"
filepath = os.path.join("./snapshots/catalog", filename)

df_catalog.to_csv(filepath, sep='\t', index=False)
print(f"Saved the DataFrame to {filepath}")

# save also as the "latest" file
latest_filepath = os.path.join("./snapshots", "pl-asr-speech-datasets-catalog-latest.tsv")
df_catalog.to_csv(latest_filepath, sep='\t', index=False)
print(f"Saved the DataFrame to {latest_filepath}")


taxonomy_url="https://docs.google.com/spreadsheets/d/181EDfwZNtHgHFOMaKNtgKssrYDX4tXTJ9POMzBsCRlI/edit#gid=2015613057"
df_taxonomy = download_tsv_from_google_sheet(taxonomy_url)
print(df_taxonomy.sample(1))

# Get the current date in the format YYYYMMDD
today = pd.Timestamp.now().strftime("%Y%m%d")

filename = f"pl-asr-speech-datasets-taxonomy-{today}.tsv"
filepath = os.path.join("./snapshots/taxonomy", filename)

df_taxonomy.to_csv(filepath, sep='\t', index=False)
print(f"Saved the DataFrame to {filepath}")

# save also as the "latest" file
latest_filepath = os.path.join("./snapshots", "pl-asr-speech-datasets-taxonomy-latest.tsv")
df_taxonomy.to_csv(latest_filepath, sep='\t', index=False)
print(f"Saved the DataFrame to {latest_filepath}")
 