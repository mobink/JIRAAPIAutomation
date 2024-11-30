import base64
import json
import logging

import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set up logging
logging.basicConfig(filename='jira_api_test.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class JiraAPIClient:

    def __init__(self, email, api_token, base_url):
        self.base_url = base_url
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Basic {base64.b64encode(f'{email}:{api_token}'.encode()).decode()}"
        }
        self.session = requests.Session()
        self.session.verify = False

    def create_issue(self, project_key, summary, description):
        endpoint = f"{self.base_url}/rest/api/2/issue"
        payload = {
            "fields": {
                "project": {"key": project_key},
                "summary": summary,
                "description": description,
                "issuetype": {"name": "Task"}
            }
        }
        response = self.session.post(endpoint, json=payload, headers=self.headers)
        if response.status_code != 201:
            logging.error(f"Failed to create issue: {response.text}")
        return response.json()

    def get_issue(self, issue_key):
        endpoint = f"{self.base_url}/rest/api/2/issue/{issue_key}"
        response = self.session.get(endpoint, headers=self.headers)
        if response.status_code != 200:
            logging.error(f"Failed to get issue: {response.text}")
        return response.json()

    def update_issue(self, issue_key, summary=None, description=None):
        endpoint = f"{self.base_url}/rest/api/2/issue/{issue_key}"
        payload = {"fields": {}}

        if summary:
            payload["fields"]["summary"] = summary
        if description:
            payload["fields"]["description"] = description

        response = self.session.put(endpoint, json=payload, headers=self.headers)
        if response.status_code != 204:
            logging.error(f"Failed to update issue: {response.text}")
        return response.status_code == 204

    def delete_issue(self, issue_key):
        endpoint = f"{self.base_url}/rest/api/2/issue/{issue_key}"
        response = self.session.delete(endpoint, headers=self.headers)
        if response.status_code != 204:
            logging.error(f"Failed to delete issue: {response.text}")
        return response.status_code == 204


def jira_api_test():
    # Credentials
    email = "mobinvurse@gmail.com"
    api_token = "ATATT3xFfGF0vGISs0m-dcZDtUkVEHOjQSHZt9xP1gJ2FkqrSpc_-yBEdBrDN3Yd0p1Hqd5yiAFmomy0djnA-KuUYHQ_as5Mdli-yp4KejR0Qf-PTJ0eJoSKQ4lMu4EsqSUr9LcLz_Gayg1enuCxjb3Ia1B6l0-NjJH2J3GWbzvrZQh-zPno8qY=7E4B0420"
    base_url = "https://exinity-test.atlassian.net"

    # Initialize Jira API Client
    jira_client = JiraAPIClient(email, api_token, base_url)

    test_report = {
        "test_cases": []
    }

    try:
        # Create Issue
        new_issue = jira_client.create_issue(
            project_key="TST",
            summary="Test Issue from REST API",
            description="Created using Jira REST API direct endpoints"
        )
        issue_key = new_issue.get('key')
        test_report["test_cases"].append({"name": "Create Issue", "result": "Pass"})
        logging.info(f"Created Issue: {issue_key}")

        # Get Issue Details
        issue_details = jira_client.get_issue(issue_key)
        test_report["test_cases"].append({"name": "Get Issue", "result": "Pass"})
        logging.info(f"Issue Details: {issue_details['fields']['summary']}")

        # Update Issue
        update_result = jira_client.update_issue(
            issue_key,
            summary="Updated Test Issue",
            description="Updated description via REST API"
        )
        test_report["test_cases"].append({"name": "Update Issue", "result": "Pass" if update_result else "Fail"})
        logging.info(f"Issue Update Success: {update_result}")

        # Delete Issue
        delete_result = jira_client.delete_issue(issue_key)
        test_report["test_cases"].append({"name": "Delete Issue", "result": "Pass" if delete_result else "Fail"})
        logging.info(f"Issue Deletion Success: {delete_result}")

    except Exception as e:
        logging.error(f"Error: {e}")
        test_report["test_cases"].append({"name": "Exception Handling", "result": "Fail", "error": str(e)})

    # Generate Test Report
    with open('test_report.json', 'w') as report_file:
        json.dump(test_report, report_file, indent=4)
    logging.info("Test report generated.")


if __name__ == "__main__":
    jira_api_test()
