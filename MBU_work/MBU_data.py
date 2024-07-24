import pandas as pd
import os


train_df = pd.read_csv(r"/exports/eddie/scratch/s2291592/LineVul/data/big-vul_dataset/train.csv")


with open(r'/exports/eddie/scratch/s2291592/LineVulReplication//MBU_work/mbu_vulnerabilities.txt', 'r') as file:
    mbu_cve_ids = set(file.read().splitlines())

processed_data = []


output_dir = r'/exports/eddie/scratch/s2291592/CVE_Merged_Files'
os.makedirs(output_dir, exist_ok=True)


processed_mbu_cves = set()


for cve_id, group in train_df.groupby('CVE ID'):
    if cve_id in mbu_cve_ids:
        if cve_id not in processed_mbu_cves:
            
            merged_funcs = '\n'.join(group['processed_func'])  
            
            first_row = group.iloc[0].to_dict()
            first_row['processed_func'] = merged_funcs
            processed_data.append(first_row)
            
            
            cve_file_path = os.path.join(output_dir, f'{cve_id}-merged-functions.txt')
            
            with open(cve_file_path, 'w') as f:
                f.write(merged_funcs)
            
            
            processed_mbu_cves.add(cve_id)
    else:
        
        for _, row in group.iterrows():
            processed_data.append(row.to_dict())


processed_df = pd.DataFrame(processed_data)


processed_df.to_csv(r'/exports/eddie/scratch/s2291592/LineVul/data/big-vul_dataset/merged_train.csv', index=False)

print("Finish, now can cd /exports/eddie/scratch/s2291592/LineVul/data/big-vul_dataset")
