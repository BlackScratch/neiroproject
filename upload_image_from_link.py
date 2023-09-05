import httpx
import os
import io

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

link_image = 'https://i.ytimg.com/vi/JNMk6lKjgEQ/mqdefault.jpg'

with httpx.Client() as client:
    response_image = client.get(url=link_image)

filename = os.path.basename(link_image)

media = {
    'file': (filename, io.BytesIO(response_image.content), 'image/jpg')
}

headers = {
    'Authorization':f'Bearer {token}',
    'Content-Disposition':f'attachment;filename={filename}'
}


with httpx.Client() as client:
    result = client.post(url=f'{host}/wp-json/wp/v2/media', headers=headers, files=media)

    response = result.json()

id_media = response['id']

url_media = response['source_url']

print(id_media)
print(url_media)