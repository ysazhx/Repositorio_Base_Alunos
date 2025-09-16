import requests

url = 'https://68641b8088359a373e978349.mockapi.io/produto'

data = {
    "marca":"Ysabella",
    "tamanho":"PP",
    "preco":190.90
}

response = requests.post(url,json=data)

print(response.status_code)
print(response.text)