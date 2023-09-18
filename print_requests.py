import requests

URL = "https://raw.githubusercontent.com/dhavalbhatia/cmput404-lab1/main/print_requests.py"

request = requests.get(URL)
print(request.text)
