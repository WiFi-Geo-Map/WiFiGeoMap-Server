import requests
import json

# Define the input data
input_data = {
    'intensity': 65,
    'bssid': '38:17:c3:b7:2e:21'
}

# Make an HTTP POST request to the API server
url = 'http://127.0.0.1:5000/process_input'  # Replace 'your_api_server_address' with your actual API server address
response = requests.post(url, json=input_data)

# Print the response
print(response.json())
