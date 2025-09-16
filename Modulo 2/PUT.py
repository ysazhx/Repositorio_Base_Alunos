import requests

id = 1

url = f'https://68641b8088359a373e978349.mockapi.io/produto/{id}'

data = {
    "marca":"Bella",
    "tamanho":"PP",
    "preco":199.90
}

response = requests.put(url,json=data)

print(response.status_code)
print(response.text)