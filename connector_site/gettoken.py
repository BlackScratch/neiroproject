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
token = get_token(host, username, password)

print(token)