import os
import subprocess
import platform
import sys
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
APPLICATIONS_TO_CLOSE = config['APPLICATIONS_TO_CLOSE']
LANGUAGE = config['LANGUAGE']

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
MY_DATA_JSON_PATH = os.path.join(BASE_PATH, f'JSON/ME/LANGUAGES/{LANGUAGE}/my_data.json')

# Get name
my_data = load_json_file(MY_DATA_JSON_PATH)
name = my_data['contact_info']['name']

SCRIPT_TO_RUN = os.path.join(BASE_PATH, '_DOCX_generator.py')
CV_SCRIPT_TO_RUN = os.path.join(BASE_PATH, 'CV_generator.py')
PDF_SCRIPT_TO_RUN = os.path.join(BASE_PATH, '_DOCXS_to_PDF_covertor.py')

COMPANIES_FOLDER_PATH = os.path.join(BASE_PATH, 'JSON/JOB/COMPANIES')
RESULTS_FOLDER_PATH = os.path.join(BASE_PATH, 'RESULTS/JOB/')
FORMAT_JSON_PATH = os.path.join(BASE_PATH, f'JSON/JOB/LANGUAGES/{LANGUAGE}/job_format.json')

CV_OUTPUT_DOCX_PATH = os.path.join(BASE_PATH, f'RESULTS/CV/CV_{name} [{LANGUAGE}].docx')

def close_applications():
    # Check if the operating system is Windows
    if platform.system() != "Windows":
        print("This script is designed to run on Windows.")
        sys.exit(1)

    for app in APPLICATIONS_TO_CLOSE:
        try:
            print(f"Attempting to close {app}...")
            subprocess.call(["taskkill", "/im", app, "/f"])
            print(f"{app} has been closed.")
        except Exception as e:
            print(f"An error occurred while closing {app}: {e}")


def main():
    # Close default applications
    close_applications()
    
    # Run CV and JOB generators
    subprocess.call(["python", CV_SCRIPT_TO_RUN])

    # Process each company folder
    company_folders = os.listdir(COMPANIES_FOLDER_PATH)

    for company_folder_index, company_folder_name in enumerate(company_folders, start=1):
        if company_folder_index > 1:
            # Close default applications
            close_applications()

        output_folder_path = os.path.join(RESULTS_FOLDER_PATH, company_folder_name)
        
        # Choose the file name based on the language
        if LANGUAGE == 'FR':
            output_docx_path = os.path.join(output_folder_path, f'lettre-de-presentation-{name} ({company_folder_name}) [{LANGUAGE}].docx')
        else:  # Assuming 'EN' or any other language will use this format
            output_docx_path = os.path.join(output_folder_path, f'cover-letter-{name} ({company_folder_name}) [{LANGUAGE}].docx')
        
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
        
        job_json_path = os.path.join(COMPANIES_FOLDER_PATH, company_folder_name, 'job_data.json')
        
        # Pass the paths as arguments to the _DOCX_generator.py script
        subprocess.call(["python", SCRIPT_TO_RUN, "job=" + job_json_path, "me=" + MY_DATA_JSON_PATH, FORMAT_JSON_PATH, output_docx_path])
    
        # Convert DOCX to PDF
        subprocess.call(["python", PDF_SCRIPT_TO_RUN, CV_OUTPUT_DOCX_PATH, output_docx_path])

        # Pause and wait for user input
        input("Press Enter to continue to the next company...")

if __name__ == "__main__":
    main()
