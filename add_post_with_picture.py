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

link_image = 'https://oir.mobi/uploads/posts/2021-04/1619133829_49-oir_mobi-p-slonik-zhivotnie-krasivo-foto-51.jpg'

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

block_image = f"""<img src="{url_media}">/<figcaption>Description picture</figcaption>"""

title = 'Its my first post'
content = '<p>Its my first content with picture</p><br>' + block_image

data = {
    'title': title,
    'slug': title,
    'content': content,
    'status': 'draft',
    'featured_media': int(id_media),
    'categories': [21],
}


with httpx.Client() as client:
    response = client.post(url=f'{host}/wp-json/wp/v2/posts', headers=headers, json=data)

print(response.json())