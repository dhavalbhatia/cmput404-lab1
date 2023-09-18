import requests

URL = "https://github.com/dhavalbhatia/cmput404-lab1/blob/main/print_requests.py"

request = requests.get(URL)
print(request.text)
