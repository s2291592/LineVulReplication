import pandas as pd

# Read the MBU vulnerabilities list from the file
input_path = r'/exports/eddie/scratch/s2291592/LineVulReplication/MBU_work/mbu_vulnerabilities.txt'

with open(input_path, 'r') as file:
    mbu_vulnerabilities = [line.strip() for line in file]


# Read the train.csv file
df = pd.read_csv(r'/exports/eddie/scratch/s2291592/LineVul/data/big-vul_dataset/train.csv')

# Create a dictionary to store merged functions
merged_funcs = {}

# Iterate over the DataFrame to process MBU vulnerabilities
for index, row in df.iterrows():
    cve_id = row['CVE ID']
    if cve_id in mbu_vulnerabilities:
        if cve_id not in merged_funcs:
            merged_funcs[cve_id] = row['processed_func']
        else:
            merged_funcs[cve_id] += ' ' + row['processed_func']
        df.at[index, 'processed_func'] = merged_funcs[cve_id]

# Keep only the first occurrence of each CVE ID
df = df.drop_duplicates(subset=['CVE ID'], keep='first')

# Output the result
df.to_csv(r'/exports/eddie/scratch/s2291592/LineVul/data/big-vul_dataset/merged_train.csv', index=False)
print("Processing complete, the result has been saved to merged_train.csv")

