import requests
import csv
from datetime import datetime
import os

# API endpoint
url = "https://bsky-users.theo.io/api/stats"

# File to store historical data
output_file = "bsky_users_history.csv"

# Function to fetch data from the API
def fetch_data():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["last_timestamp"], data["last_user_count"]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None

# Append data to the CSV file
def append_to_file(timestamp, user_count):
    try:
        # Check if file exists
        file_exists = os.path.isfile(output_file)
        with open(output_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            # Write header if file doesn't exist
            if not file_exists:
                writer.writerow(["timestamp", "users"])
            writer.writerow([timestamp, user_count])
        print(f"Appended: {timestamp}, {user_count}")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Main function
def main():
    # Fetch data
    timestamp, user_count = fetch_data()
    if timestamp is not None and user_count is not None:
        # Convert Unix timestamp to a readable format
        readable_timestamp = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        # Append to file
        append_to_file(readable_timestamp, user_count)

if __name__ == "__main__":
    main()
