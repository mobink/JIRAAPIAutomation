# CI/CD Pipeline Setup for Jira API Test Automation

## GitHub Secrets Configuration

To set up the CI/CD pipeline, you'll need to configure the following secrets in your GitHub repository:

1. `JIRA_EMAIL`: Your Atlassian account email
2. `JIRA_API_TOKEN`: Your Jira API token
3. `JIRA_BASE_URL`: Your Jira instance URL
4. `SLACK_WEBHOOK` (Optional): Slack webhook for notifications

### Steps to Add Secrets

1. Navigate to your GitHub repository
2. Go to Settings > Secrets and variables > Actions
3. Click "New repository secret"
4. Add each secret with its corresponding value

## Pipeline Triggers

The GitHub Actions workflow is configured to:
- Run on pushes to `main` and `develop` branches
- Trigger on pull requests
- Execute daily scheduled tests

## Test Execution

The pipeline will:
- Set up a Python environment
- Install dependencies
- Run Jira API tests
- Upload test reports as artifacts
- Send Slack notifications on test failures

## Recommended Additional Setup

1. Create a `.gitignore` file:
```
# Python
__pycache__/
*.py[cod]
venv/

# Test Artifacts
*.log
*.json

# Environment Files
.env
```

2. Implement environment variable fallback in your script for local testing:
```python
# At the top of your script
from dotenv import load_dotenv
load_dotenv()  # This will load variables from a .env file if present
```

## Monitoring and Troubleshooting

- Check the Actions tab in your GitHub repository for detailed test logs
- Review uploaded artifacts for comprehensive test reports
- Slack notifications provide quick failure alerts
