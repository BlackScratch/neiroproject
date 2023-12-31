import httpx

host = "https://copy-logy.ru"

username = "nilovaem"
password = "b7nA0pN4"

def get_token(host: str, username: str, password: str):
    with httpx.Client() as client:
        response = client.post(url=f"{host}/wp-json/jwt-auth/v1/token", data={'username': username, 'password':password})
        response.raise_for_status()
        token = response.json()['token']
        return token

token = get_token(host=host, username=username, password=password)

path_image = r'd:\1.jpg'

media_byte = open(file=path_image, mode='rb')

media = {
    'file': media_byte
}

headers = {
    'Authorization':f'Bearer {token}'
}

with httpx.Client() as client:
    result = client.post(url=f'{host}/wp-json/wp/v2/media', headers=headers, files=media)

    response = result.json()

id_media = response['id']

url_media = response['source_url']

print(id_media)
print(url_media)