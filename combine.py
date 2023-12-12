import pandas as pd

# Read the CSV files
file1 = pd.read_csv('langchain_rules.csv')
file2 = pd.read_csv('new_langchain_rules.csv')

# Concatenate the two DataFrames vertically
combined_data = pd.concat([file1, file2], ignore_index=True)

# Write the combined data to a new CSV file
combined_data.to_csv('combined_langchain.csv', index=False)

print("CSV files combined successfully.")
