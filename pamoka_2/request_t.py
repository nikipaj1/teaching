import requests


# r = requests.get("http://python.org/blabla")
# if r.status_code not in range(400, 600):
#     print("Pavyko prisijungti! Dirbame toliau...")
# else:
#     print(f"Kažkas ne taip.. Kodas {r.status_code}")
# # Kažkas ne taip.. Kodas 404

# r = requests.get("http://python.org/")
# print(r.headers)


# r = requests.get("https://www.python.org/search/", params={"q": "pep"})

"""
GET

    [ AS ] --GET--> [SERVERUS] -|
        |                       |
        |------------------------

POST [ AS ] --GET--> [SERVERUS]
"""

# r = requests.get("http://httpbin.org/ip")
# print(r.text)

data = {"name": "Jonas", "lastname": "Jonaitis"}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
