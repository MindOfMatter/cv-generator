import os
import subprocess
import json

# Constants
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SCRIPT_TO_RUN = os.path.join(BASE_PATH, '_DOCX_generator.py')
COMPANIES_FOLDER_PATH = os.path.join(BASE_PATH, 'JSON/JOB/COMPANIES')
RESULTS_FOLDER_PATH = os.path.join(BASE_PATH, 'RESULTS/JOB/')

# Language selection (either 'EN' or 'FR')
LANGUAGE = 'FR'  # Change this to 'EN' for English

# Constructing paths based on selected language
FORMAT_JSON_PATH = os.path.join(BASE_PATH, f'JSON/JOB/LANGUAGES/{LANGUAGE}/job_format.json')
MY_DATA_JSON_PATH = os.path.join(BASE_PATH, f'JSON/ME/LANGUAGES/{LANGUAGE}/my_data.json')

# Read the JSON file to extract the name
with open(MY_DATA_JSON_PATH, 'r', encoding='utf-8') as file:
    my_data = json.load(file)
    name = my_data['contact_info']['name']

company_folders = os.listdir(COMPANIES_FOLDER_PATH)

for company_folder_index, company_folder_name in enumerate(company_folders, start=1):
    output_folder_path = os.path.join(RESULTS_FOLDER_PATH, company_folder_name)
    
    # Choose the file name based on the language
    if LANGUAGE == 'FR':
        output_docx_name = f'lettre-de-presentation-{name} ({company_folder_name}).docx'
    else:  # Assuming 'EN' or any other language will use this format
        output_docx_name = f'cover-letter-{name} ({company_folder_name}).docx'
    
    output_docx_path = os.path.join(output_folder_path, output_docx_name)
    
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    job_json_path = os.path.join(COMPANIES_FOLDER_PATH, company_folder_name, 'job_data.json')
    
    # Pass the paths as arguments to the _DOCX_generator.py script
    subprocess.call(["python", SCRIPT_TO_RUN, "job=" + job_json_path, "me=" + MY_DATA_JSON_PATH, FORMAT_JSON_PATH, output_docx_path])
