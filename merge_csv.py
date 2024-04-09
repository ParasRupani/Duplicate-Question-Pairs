import pandas as pd
import glob

df_q1 = []
df_q2 = []

ignore_csv = 'data/merged_questions.csv'

for csv_file in glob.glob('data/*.csv'):
    if csv_file.endswith(ignore_csv): 
        continue
    
    #remove empty rows, shuffle
    df = pd.read_csv(csv_file).dropna().sample(frac=1).reset_index(drop=True)

    #Midpoint for splitting
    midpoint = len(df) // 2

    # Split into 2 dataframes, first half into q1, second half into q2 dataframes
    q1 = df.iloc[:midpoint, :]
    q2 = df.iloc[midpoint:, :]

    df_q1.append(q1)
    df_q2.append(q2)

# Concatenate all q1 and q2 DataFrames
merged_q1 = pd.concat(df_q1, ignore_index=True)
merged_q2 = pd.concat(df_q2, ignore_index=True)

merged_df = pd.DataFrame({
    'q1': merged_q1.iloc[:, 0], 
    'q2': merged_q2.iloc[:, 0]   
})

merged_df.to_csv('data/merged_dataset.csv', index=False)