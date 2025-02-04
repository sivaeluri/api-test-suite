API Test Automation

Project Overview

This project automates API testing using Python, pytest, and requests. It includes test cases for GET and POST requests, with an option to generate an HTML test report.

Prerequisites

Ensure you have the following installed:

Python 3.x (Download)

Pip (comes with Python installation)

Install required Python packages:

pip install pytest requests openpyxl pytest-html

Test Cases

The test cases are documented in TestCases.xlsx. It includes:

GET request to fetch user details

POST request to create a user

Running the Tests

Navigate to the project folder and run:

pytest -v

Generating a Test Report

To generate an HTML report, run:

pytest --html=report.html --self-contained-html

The report will be generated as report.html. Open it in a browser to view the results.

Uploading to GitHub

To upload your test suite to GitHub, follow these steps:

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main

Replace <your-repo-url> with your actual GitHub repository URL.

Folder Structure

api-test-suite/
│-- test_api.py       # Python script containing API tests
│-- TestCases.xlsx    # Excel file with test cases
│-- report.html       # Generated test report
│-- README.md         # Project documentation

Conclusion

This project provides an automated approach to API testing using Python. You can expand it further by adding more API test cases or integrating it with CI/CD pipelines.
