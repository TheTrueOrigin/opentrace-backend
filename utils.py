import requests
import os

def download_latest_database():
    api_url = f'https://api.github.com/repos/thetrueorigin/opentrace-database/releases/latest'
    response = requests.get(api_url)
    download_url = response.json()["assets"][0]["browser_download_url"]
    download_response = requests.get(download_url)
    with open(os.path.join(os.path.dirname(__file__), "database.db"), "wb") as file:
        file.write(download_response.content)