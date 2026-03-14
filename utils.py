import requests
import os

def download_latest_database():
    download_url = "https://github.com/thetrueorigin/opentrace-database/releases/latest/download/database.db"
    download_response = requests.get(download_url)
    with open(os.path.join(os.path.dirname(__file__), "database.db"), "wb") as file:
        file.write(download_response.content)
