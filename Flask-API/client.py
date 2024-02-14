import requests
import json

# Define the input data
input_data = {
    'bs1': 'e2:55:b8:29:4d:ef',
    'inten1': 45,
    'bs2': 'f6:55:b8:29:4d:ef',
    'inten2': 45,
    'bs3': 'e6:55:b8:29:4d:ef',
    'inten3': 46,
    'dest':'C4'
}

# Make an HTTP POST request to the API server
url = 'http://127.0.0.1:5000/process_input'  # Replace 'your_api_server_address' with your actual API server address
response = requests.post(url, json=input_data)

# Print the response
print(response.json())
