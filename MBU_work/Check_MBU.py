import os

def is_mbu_vulnerability(conclusion_file_path):
    if not os.path.exists(conclusion_file_path):
        return True
    with open(conclusion_file_path, 'r') as file:
        content = file.read().strip()
        return content == "MBU vulnerability"

def find_mbu_vulnerabilities(base_path):
    mbu_vulnerabilities = []
    non_mbu_vulnerabilities = []
    
    for detector_name in os.listdir(base_path):
        detector_path = os.path.join(base_path, detector_name)
        if not os.path.isdir(detector_path):
            continue
        
        for project_name in os.listdir(detector_path):
            project_path = os.path.join(detector_path, project_name)
            if not os.path.isdir(project_path):
                continue
            
            for commit_or_cve_id in os.listdir(project_path):
                commit_or_cve_path = os.path.join(project_path, commit_or_cve_id)
                if not os.path.isdir(commit_or_cve_path):
                    continue
                
                conclusion_file_path = os.path.join(commit_or_cve_path, 'conclusion')
                if is_mbu_vulnerability(conclusion_file_path):
                    mbu_vulnerabilities.append(commit_or_cve_id)
                else:
                    non_mbu_vulnerabilities.append(commit_or_cve_id)
    
    return mbu_vulnerabilities, non_mbu_vulnerabilities

# Usage example:
base_path = '/Users/ricardoline/Desktop/CodeChangesAnalysis/experiments/all_else'
mbu_vulnerabilities, non_mbu_vulnerabilities = find_mbu_vulnerabilities(base_path)

# print("MBU Vulnerabilities:")
# print(mbu_vulnerabilities)

# print("Non-MBU Vulnerabilities:")
# print(non_mbu_vulnerabilities)


output_path = '/Users/ricardoline/Desktop/what_code/MBU_work/mbu_vulnerabilities.txt'

with open(output_path, 'w') as file:
    for item in mbu_vulnerabilities:
        file.write(f"{item}\n")