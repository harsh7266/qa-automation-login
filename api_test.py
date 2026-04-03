import requests

url = "https://reqres.in/api/login"

headers = {
    "x-api-key": "pub_5e244c21f879e64cb900c919b6e0bdf21fa48571a0a435d169a7ec51ddd993d7",
    "Content-Type": "application/json"
}

data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.text)