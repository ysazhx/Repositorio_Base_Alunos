import requests

i = 0


for id in range(1,101):
    url = f'https://68641b8088359a373e978349.mockapi.io/produto/{id}'
    response = requests.delete(url)
    print(response.status_code)
    print(response.text)        