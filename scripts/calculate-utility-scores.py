import pandas as pd
from utils import download_tsv_from_google_sheet

def score_datasets_with_updated_criteria(df):
    # Filter datasets based on the updated criteria
    filtered_df = df[
        (df['Access type'] == 'free') &
        (df['Access link'] != 'no info') &
        (df['Available online'] == 'yes') &
        (df['License'].str.contains('CC') & ~df['License'].str.contains('ND')) &
        (~df['License'].str.contains('public domain', case=False)) &  # Assuming we want to include public domain explicitly
        (df['Price - non-commercial usage'].str.lower() == 'free') &
        (df['Price - commercial usage'].str.lower() == 'free')&
        (df['Transcription coverage'] == "100")
    ]
    
    # Assign a score of 1 to all datasets that meet the criteria, as the filtering has already been applied
    filtered_df['Score'] = 1
    
    return filtered_df[['Dataset ID', 'Access type', 'Access link', 'License', 'Price - non-commercial usage', 'Price - commercial usage', 'Transcription coverage', 'Score']]

catalog_url="https://docs.google.com/spreadsheets/d/181EDfwZNtHgHFOMaKNtgKssrYDX4tXTJ9POMzBsCRlI/edit#gid=0"
df_catalog = download_tsv_from_google_sheet(catalog_url)
print(df_catalog.sample(10))

taxonomy_url="https://docs.google.com/spreadsheets/d/181EDfwZNtHgHFOMaKNtgKssrYDX4tXTJ9POMzBsCRlI/edit#gid=2015613057"
df_taxonomy = download_tsv_from_google_sheet(taxonomy_url)

# Apply the updated scoring function to the dataframe
scored_datasets_with_updated_criteria = score_datasets_with_updated_criteria(df_catalog)

# Display the resulting list of dataset IDs that meet the updated criteria
print(scored_datasets_with_updated_criteria[['Dataset ID', 'Score']])
