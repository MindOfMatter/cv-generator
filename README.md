# CV-Generator

## Overview
CV-Generator is a Python-based application designed to automate the creation of professional CVs and job applications. It includes modules for DOCX generation, PDF conversion, and JSON data integration, offering a complete solution for personalized resume and cover letter creation. The application supports both English (EN) and French (FR) versions, allowing for multilingual document generation.

## Why CV-Generator is Useful

The CV-Generator streamlines the process of creating personalized and professional CVs and job applications, offering several key benefits:

- **Time Efficiency**: Automates the repetitive task of formatting and structuring CVs and cover letters, saving valuable time for job seekers.
- **Consistency and Accuracy**: Ensures consistent formatting and layout across different applications, reducing the likelihood of errors and discrepancies in personal and professional information.
- **Customization and Flexibility**: Offers the ability to easily tailor CVs and cover letters for specific job applications or industries by simply updating JSON data files.
- **Multilingual Capabilities**: With support for both English and French, the CV-Generator caters to a diverse user base, facilitating bilingual document creation.
- **Scalability**: Ideal for generating multiple CVs and cover letters efficiently, particularly beneficial for freelancers, consultants, and job seekers targeting multiple roles or companies.
- **Professional Presentation**: By utilizing customizable templates, the tool aids in producing clean, professionally formatted documents that make a strong first impression.
- **Ease of Use**: Designed to be user-friendly, it requires minimal technical expertise, making it accessible to a wide range of users.

In summary, CV-Generator is an invaluable tool for anyone looking to enhance their job application process, offering a blend of efficiency, professionalism, and customization.

## Features
- **DOCX Creation**: Generates CVs in DOCX format using customizable templates.
- **PDF Conversion**: Converts DOCX files to PDF format for broader accessibility.
- **Data Merging**: Integrates personal, professional, and job-specific data from JSON sources into CV templates.
- **Multilingual Support**: Offers template and data management for both English and French languages.

## Prerequisites
- Python 3.x
- LibreOffice (for DOCX to PDF conversion)

## Configuration Setup
The application uses a `setup.json` file in the JSON directory for easy configuration of common settings:
- `LIBRE_OFFICE_PATH`: Specifies the path to the LibreOffice executable, used for PDF conversion.
- `LANGUAGE`: Determines the language (either 'EN' or 'FR') for document generation.

This approach prevents the need for hardcoding these values within the script, offering flexibility and ease of updates.

Here is the structure of the `setup.json` file:
```
{
 "LIBRE_OFFICE_PATH": "path_to_your_libreoffice_executable",
 "APPLICATIONS_TO_CLOSE": ["PDFXEdit.exe", "swriter.exe", "soffice.bin"],
 "LANGUAGE": "EN"  // Or "FR"
}
```

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
+---JSON
|   setup.json
|   +---CV
|   |   \---LANGUAGES
|   |       +---EN
|   |       |       cv_data.json
|   |       |       cv_format.json
|   |       |
|   |       \---FR
|   |               cv_data.json
|   |               cv_format.json
|   |
|   +---JOB
|   |   +---COMPANIES
|   |   |   \---_EXAMPLE_TEMPLATE_compagnyx
|   |   |           job_data.json
|   |   |
|   |   \---LANGUAGES
|   |       +---EN
|   |       |       job_format.json
|   |       |
|   |       \---FR
|   |               job_format.json
|   |
|   \---ME
|       \---LANGUAGES
|           +---EN
|           |       my_data.json
|           |
|           \---FR
|                   my_data.json
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
This project is licensed under the GPL-3.0 license - see the `LICENSE` file for details.

## Acknowledgments
- Thanks to all possible contributors who have helped to build this tool.
