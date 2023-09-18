import io

import httpx
from typing import Dict
import transliterate

class RequestorMysite:
    def __init__(self, token:str, host: str, proxy:str=None):
        self.authorization = {
            'Authorization':f'Bearer {token}'
        }
        self.host = host
        self.proxy = proxy

    def _post_request(self, url:str, headers:Dict, files:Dict = None, data: Dict = None):
        for i in range(10):
            try:
                with httpx.Client(proxies=self.proxy, timeout=30) as client:
                    response=client.post(
                        url=url,
                        headers=headers,
                        files=files,
                        json=data
                    )
                    response.raise_for_status()
                    return response.json()
            except httpx.HTTPStatusError as exc:
                print(f'Error. Status code {exc.response.status_code}')
            except httpx.ConnectError as exc:
                print(f'Error accured {exc}')
            except httpx.HTTPError as exc:
                print(f'HTTP error {exc}')
            except httpx.TimeoutException as exc:
                print(f'TimeOutError {exc}')
            except httpx.PoxyError as exc:
                print(f'Proxy error has accured {exc}')
            except httpx.NetworkError as exc:
                print(f'Network error has accured {exc}')
            except Exception as exc:
                print(f'Error {exc}')
        raise Exception('Не удалось получить ответ от сайта. Проверить работу Апи и Прокси.')

    def _get_request(self, url: str):
        for i in range(10):
            try:
                with httpx.Client(proxies=self.proxy, timeout=30) as client:
                    response = client.get(
                        url=url
                    )
                    response.raise_for_status()
                    return response
            except httpx.HTTPStatusError as exc:
                print(f'Error. Status code {exc.response.status_code}')
            except httpx.ConnectError as exc:
                print(f'Error accured {exc}')
            except httpx.HTTPError as exc:
                print(f'HTTP error {exc}')
            except httpx.TimeoutException as exc:
                print(f'TimeOutError {exc}')
            except httpx.PoxyError as exc:
                print(f'Proxy error has accured {exc}')
            except httpx.NetworkError as exc:
                print(f'Network error has accured {exc}')
            except Exception as exc:
                print(f'Error {exc}')
        raise Exception('Не удалось получить выполнить get запрос.')

    def _post_content(self, url: str, data: Dict):
        headers = {
            'Content-Type':'application/json'
        }
        headers.update(self.authorization)
        response = self._post_request(url=url, headers=headers, data=data)
        return response
    def publish_content(self, title: str, content:str, id_featured_media:int):
        data = {
            'title':title,
            'slug': transliterate.translit(title.replace(' ','_'), reversed=True),
            'content': content,
            'status':'draft',
            'feautured_media':int(id_featured_media)
        }

        data_post = self._post_content(url=f'{self.host}/wp-json/wp/v2/posts', data=data)
        link_post = data_post['link']
        print(link_post)

    def _upload_media(self,url: str, link_image: str, theme: str):
        result_get_request = self._get_request(url=link_image)
        filename = f"{transliterate.translit(value=theme, reversed=True).encode('latin-1', 'replace').decode('latin-1')}.jpg"
        media ={
            'file':(filename, io.BytesIO(result_get_request.content), 'image/jpeg')
        }

        headers = {
            'Content-Desposition':f'attachment: filename={filename}'
        }

        headers.update(self.authorization)
        response = self._post_request(url=url, headers=headers, files=media)
        id_media = response['id']
        url_media = response['source_url']
        print(id_media)
        print(url_media)
        return id_media, url_media

    def get_image(self, link_image: str, theme: str):
        url = f'{self.host}/wp-json/wp/v2/media'
        id_media, url_media = self._upload_media(url=url, link_image=link_image, theme=theme)
        return id_media, url_media

if __name__ == '__main__':
    from get_token import get_token
    token = get_token(host = "https://copy-logy.ru/", username = "nilovaem", password = "b7nA0pN4")

    requestor_my_site = RequestorMysite(token =token, host='https://copy-logy.ru')
    requestor_my_site.publish_content(title='Заголовок', content='Контент', id_featured_media=372)

    requestor_my_site.get_image(link_image='https://i.discogs.com/iIgElryG03MNic4LHxx4rPLTdzmQ64SyWrJac9kD9d0/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTQzNzg5/OTMtMTM2MzMwODI5/MC0zOTY4LmpwZWc.jpeg', theme='Тема')