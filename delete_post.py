import httpx

from connector_site.gettoken import get_token

host = "https://copy-logy.ru/"

username = "nilovaem"

password = "b7nA0pN4"

token = get_token(host=host, username=username, password=password)

headers = {
    'Authorization':f'Bearer {token}',
    'Content-Type':'application/json'
}

with httpx.Client() as client:
    response = client.delete(url=f'{host}/wp-json/wp/v2/posts/2015', headers=headers)

print(response)