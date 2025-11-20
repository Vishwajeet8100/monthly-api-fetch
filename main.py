import requests
import json
from datetime import datetime

def fetch_trial_data():
    # Public test API (returns a random dog image)
    url = "https://dog.ceo/api/breeds/image/random"

    response = requests.get(url)
    data = response.json()

    # Create a file name with timestamp
    filename = f"trial_data_{datetime.now().strftime('%Y_%m_%d_%H_%M')}.json"

    # Save response in JSON file
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print("Saved:", filename)


if __name__ == "__main__":
    fetch_trial_data()
