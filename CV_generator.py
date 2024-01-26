import os
import subprocess

# Constants
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SCRIPT_TO_RUN = os.path.join(BASE_PATH, '_DOCX_generator.py')

MY_DATA_JSON_PATH = os.path.join(BASE_PATH, 'JSON/ME/my_data.json')
CV_DATA_JSON_PATH = os.path.join(BASE_PATH, 'JSON/CV/cv_data.json')
FORMAT_JSON_PATH = os.path.join(BASE_PATH, 'JSON/CV/cv_format.json')
OUTPUT_DOCX_PATH = os.path.join(BASE_PATH, 'RESULTS/CV/CV_Mathieu_Martineau.docx')

# Call the script with the new arguments
subprocess.call(["python", SCRIPT_TO_RUN, "cv=" + CV_DATA_JSON_PATH, "me=" + MY_DATA_JSON_PATH, FORMAT_JSON_PATH, OUTPUT_DOCX_PATH])