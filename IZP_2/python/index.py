import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print("Статус код:", response.status_code)
print("респонс сервера:", response.json())
