import os
import subprocess

# Constants
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SCRIPT_TO_RUN = os.path.join(BASE_PATH, '_DOCX_generator.py')
COMPANIES_FOLDER_PATH = os.path.join(BASE_PATH, 'JSON/JOB/COMPANIES')
RESULTS_FOLDER_PATH = os.path.join(BASE_PATH, 'RESULTS/JOB/')
FORMAT_JSON_PATH = os.path.join(BASE_PATH, 'JSON/JOB/job_format.json')

MY_DATA_JSON_PATH = os.path.join(BASE_PATH, 'JSON/ME/my_data.json')

company_folders = os.listdir(COMPANIES_FOLDER_PATH)

for company_folder_index, company_folder_name in enumerate(company_folders, start=1):
    output_folder_path = os.path.join(RESULTS_FOLDER_PATH, company_folder_name)
    output_docx_path = os.path.join(output_folder_path, f'lettre-de-presentation-mathieu-martineau ({company_folder_name}).docx')
    
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    job_json_path = os.path.join(COMPANIES_FOLDER_PATH, company_folder_name, 'job_data.json')
    
    # Pass the paths as arguments to the _DOCX_generator.py script
    subprocess.call(["python", SCRIPT_TO_RUN, "job=" + job_json_path, "me=" + MY_DATA_JSON_PATH, FORMAT_JSON_PATH, output_docx_path])
