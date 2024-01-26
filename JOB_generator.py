import os
import subprocess
import json

# Constants
# Constant for the setup configuration file path
SETUP_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'JSON/setup.json')

def load_json_file(file_path):
    """Load JSON file from the given path."""
    with open(file_path, 'r', encoding='utf-8') as file:
        print(f"Loading JSON from {file_path}")
        return json.load(file)

# Load configuration from setup.json
config = load_json_file(SETUP_CONFIG_PATH)

# Use the configuration values
LANGUAGE = config['LANGUAGE']

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SCRIPT_TO_RUN = os.path.join(BASE_PATH, '_DOCX_generator.py')
COMPANIES_FOLDER_PATH = os.path.join(BASE_PATH, 'JSON/JOB/COMPANIES')
RESULTS_FOLDER_PATH = os.path.join(BASE_PATH, 'RESULTS/JOB/')

# Constructing paths based on selected language
FORMAT_JSON_PATH = os.path.join(BASE_PATH, f'JSON/JOB/LANGUAGES/{LANGUAGE}/job_format.json')
MY_DATA_JSON_PATH = os.path.join(BASE_PATH, f'JSON/ME/LANGUAGES/{LANGUAGE}/my_data.json')

# Get name
my_data = load_json_file(MY_DATA_JSON_PATH)
name = my_data['contact_info']['name']

company_folders = os.listdir(COMPANIES_FOLDER_PATH)

for company_folder_index, company_folder_name in enumerate(company_folders, start=1):
    output_folder_path = os.path.join(RESULTS_FOLDER_PATH, company_folder_name)
    
    # Choose the file name based on the language
    if LANGUAGE == 'FR':
        output_docx_name = f'lettre-de-presentation-{name} ({company_folder_name}) [{LANGUAGE}].docx'
    else:  # Assuming 'EN' or any other language will use this format
        output_docx_name = f'cover-letter-{name} ({company_folder_name}) [{LANGUAGE}].docx'
    
    output_docx_path = os.path.join(output_folder_path, output_docx_name)
    
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    job_json_path = os.path.join(COMPANIES_FOLDER_PATH, company_folder_name, 'job_data.json')
    
    # Pass the paths as arguments to the _DOCX_generator.py script
    subprocess.call(["python", SCRIPT_TO_RUN, "job=" + job_json_path, "me=" + MY_DATA_JSON_PATH, FORMAT_JSON_PATH, output_docx_path])
