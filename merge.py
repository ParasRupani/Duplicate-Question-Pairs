import os
import pandas as pd

# Path to the folder containing files to be merged
folder_path = "./data"

# List to store DataFrames from individual files
dfs = []

for file_name in os.listdir(folder_path):
    # Check for CSV files
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        dfs.append(pd.read_csv(file_path))

# Merge all DataFrames in the list into a single DataFrame
merged_df = pd.concat(dfs)

merged_df.to_csv('./data/merged_questions.csv', index=False)