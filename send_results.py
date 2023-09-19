import sys
import requests

def send_results(run_id, username, password, log_file_path):
    with open(log_file_path, 'r') as f:
        test_results = f.read()

    # Prepare the TestRail API endpoint and payload
    url = f"https://swe401pro.io.com/api/v2/add_results_for_cases/{run_id}"
    payload = {
        "results": test_results
    }

    # Send the API request
    response = requests.post(url, auth=(username, password), json=payload)
    response.raise_for_status()

if __name__ == "__main__":
    run_id = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    log_file_path = sys.argv[4]

    send_results(run_id, username, password, log_file_path)