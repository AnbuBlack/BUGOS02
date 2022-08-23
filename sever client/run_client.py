import requests

user = "Lalo"

print("request")
response = requests.get(f"http://127.0.0.1:5000/visit/{user}")
print (response.text)

pid = 10
response = requests.get(f"http://127.0.0.1:5000/product/{pid}")
print (response.text)