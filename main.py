import requests
import json
from datetime import datetime

def fetch_data():
    url = "https://your-api-url.com/data"
    response = requests.get(url)
    data = response.json()

    filename = f"data_{datetime.now().strftime('%Y_%m_%d')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print("Saved:", filename)

if __name__ == "__main__":
    fetch_data()
