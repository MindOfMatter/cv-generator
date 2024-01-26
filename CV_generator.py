import os
import subprocess
import json

# Constants
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SCRIPT_TO_RUN = os.path.join(BASE_PATH, '_DOCX_generator.py')

# Language selection (either 'EN' or 'FR')
LANGUAGE = 'FR'  # Change this to 'EN' for English

# Constructing paths based on selected language
MY_DATA_JSON_PATH = os.path.join(BASE_PATH, f'JSON/ME/LANGUAGES/{LANGUAGE}/my_data.json')
CV_DATA_JSON_PATH = os.path.join(BASE_PATH, f'JSON/CV/LANGUAGES/{LANGUAGE}/cv_data.json')
FORMAT_JSON_PATH = os.path.join(BASE_PATH, f'JSON/CV/LANGUAGES/{LANGUAGE}/cv_format.json')

# Read the JSON file to extract the name
with open(MY_DATA_JSON_PATH, 'r', encoding='utf-8') as file:
    my_data = json.load(file)
    name = my_data['contact_info']['name']

OUTPUT_DOCX_PATH = os.path.join(BASE_PATH, f'RESULTS/CV/CV_{name}_{LANGUAGE}.docx')

# Call the script with the new arguments
subprocess.call(["python", SCRIPT_TO_RUN, "cv=" + CV_DATA_JSON_PATH, "me=" + MY_DATA_JSON_PATH, FORMAT_JSON_PATH, OUTPUT_DOCX_PATH])
