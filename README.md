# CV-Generator

## Overview
CV-Generator is a Python-based application designed to automate the creation of professional CVs and job applications. It includes modules for DOCX generation, PDF conversion, and JSON data integration, offering a complete solution for personalized resume and cover letter creation.

## Features
- **DOCX Creation**: Generates CVs in DOCX format using customizable templates.
- **PDF Conversion**: Converts DOCX files to PDF format for broader accessibility.
- **Data Merging**: Integrates personal and professional data from JSON sources into CV templates.

## Prerequisites
- Python 3.x
- LibreOffice (for DOCX to PDF conversion)

## Installation
1. Clone the repository:
```
git clone [repository URL]
```

2. Install required Python packages:
```
pip install -r requirements.txt
```

## JSON Setup
The application requires specific JSON files for data input:
- `my_data.json`: Contains global personal (sensitive) information.
- `cv_data.json`: Holds professional details and experiences.
- `cv_format.json`: Defines the format and structure of the CV.
- `job_data.json`: Contains job-specific details for cover letters.

Place these files in a directory structured as follows:
```
PROJECT_ROOT/
|-- JSON/
|   |-- ME/
|   |   `-- my_data.json
|   |-- CV/
|   |   |-- cv_data.json
|   |   `-- cv_format.json
|   `-- JOB/
|       |-- COMPANIES/
|       |   `-- [Company Name]/
|       |       |-- job_data.json
|       |       `-- job_format.json
`-- RESULTS/
    |-- CV/
    |   |-- CV_[my_data.name].docx
    |   `-- CV_[my_data.name].pdf
    `-- JOB/
        `-- [Company Name]/
            |-- letter_[my_data.name]_[Company Name].docx
            `-- letter_[my_data.name]_[Company Name].pdf
```

## Usage
Run `generate_all.py` to generate a CV with for each Company (from JSON provided values to RESULTS output):
```
python generate_all.py
```

## Contributing
Contributions to CV-Generator are welcome! Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments
- Thanks to all contributors who have helped to build this tool.
