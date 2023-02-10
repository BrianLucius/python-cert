import requests

try:
    reply = requests.get('http://localhost:3000/cars', timeout=1)
except requests.RequestException as e:
    print("Communication error: " + str(e))
else:
    if reply.status_code == requests.codes.ok:
        print(reply.headers['Content-Type'])
        print(reply.json())
    else:
        print("Server error")
