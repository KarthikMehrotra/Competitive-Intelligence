import pandas as pd

# Specify the paths to your CSV files
csv_file1_path = r"alphavantage\apple\extracted_data_entity_verbs_march_apple_.csv"
csv_file2_path = r"alphavantage\apple\extracted_data_entity_verbs_april_apple_.csv"
csv_file3_path = r"alphavantage\apple\extracted_data_entity_verbs_may_apple_.csv"

# Read the CSV files into DataFrames
df1 = pd.read_csv(csv_file1_path)
df2 = pd.read_csv(csv_file2_path)
df3 = pd.read_csv(csv_file3_path)

# Merge the DataFrames
merged_df = pd.concat([df1, df2, df3], ignore_index=True)

# Save the merged DataFrame to a new CSV file
output_csv_file_path = r"alphavantage\apple\apple_merged_entity_verbs.csv"
merged_df.to_csv(output_csv_file_path, index=False)

print("Merged data saved to CSV file:", output_csv_file_path)
