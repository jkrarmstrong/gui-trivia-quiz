import requests

# Params for API request
parameters = {
    "amount": 10,
    "type": "boolean",
}

# Make GET request, check if successful, parse JSON response and extract key from data
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
