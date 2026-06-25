# Requires requests
# Install with: pip install requests

import requests

url = "https://www.google.com"

response = requests.get(url)

print("URL:", url)
print("HTTP Status Code:", response.status_code)