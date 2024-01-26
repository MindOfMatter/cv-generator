import os
import subprocess
import json

# Constants
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SCRIPT_TO_RUN = os.path.join(BASE_PATH, '_DOCX_generator.py')

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

# Constructing paths based on selected language
MY_DATA_JSON_PATH = os.path.join(BASE_PATH, f'JSON/ME/LANGUAGES/{LANGUAGE}/my_data.json')
CV_DATA_JSON_PATH = os.path.join(BASE_PATH, f'JSON/CV/LANGUAGES/{LANGUAGE}/cv_data.json')
FORMAT_JSON_PATH = os.path.join(BASE_PATH, f'JSON/CV/LANGUAGES/{LANGUAGE}/cv_format.json')

# Get name
my_data = load_json_file(SETUP_CONFIG_PATH)
name = my_data['contact_info']['name']

OUTPUT_DOCX_PATH = os.path.join(BASE_PATH, f'RESULTS/CV/CV_{name}_{LANGUAGE}.docx')

# Call the script with the new arguments
subprocess.call(["python", SCRIPT_TO_RUN, "cv=" + CV_DATA_JSON_PATH, "me=" + MY_DATA_JSON_PATH, FORMAT_JSON_PATH, OUTPUT_DOCX_PATH])
