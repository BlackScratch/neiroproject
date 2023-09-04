import httpx

from connector_site.gettoken import get_token

host = "https://copy-logy.ru/"

username = "nilovaem"

password = "b7nA0pN4"

token = get_token(host=host, username=username, password=password)

title = "Просто тестовый заголовок"
content = "Тестовая запись"

data = {
    'title': title,
    'content': content,
    'slug': title.replace(' ','_'),
    # 'status': 'publish'
    'status': 'draft',
    'categories':21
}

headers = {
    'Authorization':f'Bearer {token}',
    'Content-Type':'application/json'
}

with httpx.Client() as client:
    response = client.post(url=f'{host}/wp-json/wp/v2/posts', headers=headers, json=data)