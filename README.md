# Jira API Test Automation

## Overview
This project provides an automated test suite for interacting with the Jira REST API, demonstrating core CRUD (Create, Read, Update, Delete) operations on Jira issues.

## Prerequisites
- Python 3.8+
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/mobink/JIRAAPIAutomation.git
cd jira-api-test-automation
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Configuration
1. Replace the following credentials in `jira_api_test.py`:
   - `email`: Your Atlassian account email
   - `api_token`: Your Jira API token
   - `base_url`: Your Jira instance URL

### Generate an API Token
1. Log in to your Atlassian account
2. Go to Account Settings > Security
3. Create an API token

## Running the Tests
```bash
python jira_api_test.py
```

## Frameworks and Tools
- **Language**: Python 3.8+
- **HTTP Library**: `requests`
- **Logging**: Python's built-in `logging` module
- **Reporting**: JSON-based test report generation

## Test Coverage
The test script covers the following Jira API operations:
- Issue Creation
- Issue Retrieval
- Issue Update
- Issue Deletion

### Test Report
After execution, a `test_report.json` and `jira_api_test.log` will be generated, providing detailed test results and logs.

## Security Considerations
⚠️ **Important**: 
- Never commit sensitive credentials to version control
- Use environment variables or secure credential management
- The current script disables SSL verification (not recommended for production)

## Potential Improvements
- Add more comprehensive error handling
- Implement retry mechanisms
- Create more granular test scenarios
- Add support for different issue types

## License
[Specify your license here]

## Contact
[Your contact information]
