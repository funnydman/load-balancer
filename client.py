import requests

for i in range(10):
    requests.get(f"http://localhost/{i}")
