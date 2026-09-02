import requests

url = "http://127.0.0.1:5000/Educa"

resposta = requests.get(url)
print(f"Status: {resposta.status_code}")
print(resposta.json())
