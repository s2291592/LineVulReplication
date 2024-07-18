import pandas as pd

# Read the MBU vulnerabilities list from the file
input_path = '/Users/ricardoline/Desktop/what_code/MBU_work/mbu_vulnerabilities.txt'

with open(input_path, 'r') as file:
    mbu_vulnerabilities = [line.strip() for line in file]

# Load the original data
df = pd.read_csv('path/to/train.csv')

# Separate MBU and non-MBU vulnerabilities data
mbu_data = df[df['CVE ID'].isin(mbu_vulnerabilities)]
non_mbu_data = df[~df['CVE ID'].isin(mbu_vulnerabilities)]

# Merge functions for MBU vulnerabilities (random order)
mbu_data_random_order = mbu_data.groupby('CVE ID')['processed_func'].apply(lambda x: ' '.join(x)).reset_index()
mbu_data_random_order['target'] = 1  # Set the target label

# Pseudocode, in practice, use Joern commands or API
def generate_callgraph_order(mbu_data):
    # Use Joern to generate call graphs
    # Parse call graphs to get function call order
    # Merge functions based on call order
    mbu_data_callgraph_order = mbu_data.groupby('CVE ID')['processed_func'].apply(lambda x: ' '.join(sorted(x))).reset_index()  # Example, sort based on call graph
    mbu_data_callgraph_order['target'] = 1
    return mbu_data_callgraph_order

mbu_data_callgraph_order = generate_callgraph_order(mbu_data)

# Combine MBU and non-MBU data
train_data_random_order = pd.concat([mbu_data_random_order, non_mbu_data])
train_data_callgraph_order = pd.concat([mbu_data_callgraph_order, non_mbu_data])

# Save the generated datasets
train_data_random_order.to_csv('path/to/train_random_order.csv', index=False)
train_data_callgraph_order.to_csv('path/to/train_callgraph_order.csv', index=False)
