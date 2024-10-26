import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Cat Fact:", data['fact'])
else:
    print("Error:", response.status_code)
