import requests
import pandas as pd

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