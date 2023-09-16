import httpx
import time
from typing import Dict, List

class RequestorChatGPT:
    def __init__(self, token: str, proxy: str = None):
        self.token = token
        self.headers = {'Content-Type': 'application/json'}
        self.proxy = proxy
        self.messages = [
            {
                'role':'system',
                'content': 'Отвечай без вводных слов, канцеляритов и лишних конструкций'
            }
        ]

    def _post_request(self, url: str, data: Dict):
        auth = ('Bearer', self.token)
        for i in range(10):
            try:
                with httpx.Client(auth=auth, headers=self.headers, proxies=self.proxy, timeout=300) as client:
                    response = client.post(
                        url=url,
                        json=data
                    )
                    response.raise_for_status()
                    return response.json()
            except httpx.HTTPStatusError as exc:
                print(f'Error status. Status code {exc.response.status_code}. More {exc}')
                time.sleep(30)
            except httpx.HTTPError as exc:
                print(f'HTTP error occured: {exc}')
            except httpx.TimeoutException as exc:
                print(f'A timeout occured: {exc}')
            except httpx.ProxyError as exc:
                print(f'A proxyerror occured: {exc}')
            except httpx.NetworkError as exc:
                print(f'A network error occured: {exc}')
            except Exception as exc:
                print(f'An error occured: {exc}')
        raise Exception('Не удалось получить ответа от сервера')

    def _get_chat(self, url: str, messages:List[Dict]):
        data = {
            'model': 'gpt-3.5-turbo',
            'messages':messages
        }
        result = self._post_request(url=url, data=data)
        return result['choices'][0]['message']['content']

    def _update_messages(self, role: str, content:str):
        data = {'role':role, 'content': content.replace('"','')}
        if len(self.messages)>5:
            del self.messages[1:-4]
        self.messages.append(data)
    def answer_chat(self, question: str):
        self._update_messages(role='user', content=question)
        answer_chat_gpt = self._get_chat(url='https://api.openai.com/v1/chat/completions', messages=self.messages).replace('"','')
        self._update_messages(role='assistent', content=answer_chat_gpt)
        return answer_chat_gpt

    def _get_image(self, url: str, prompt: str):
        data = {
            'prompt':prompt,
            'n':1,
            'size': '512x512'
        }

        result = self._post_request(url=url, data = data)

        return result['data'][0]['url']

    def answer_image(self, prompt: str):
        url = 'https://api.openai.com/v1/images/generations'
        link_image = self._get_image(url=url, prompt=prompt)
        return link_image

if __name__=='__main__':
    token='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'
    requestor_chat_gpt= RequestorChatGPT(token=token)
    # answer = requestor_chat_gpt.answer_chat(question='Привет')
    # print(answer)
    link_image = requestor_chat_gpt.answer_image(prompt='Паста карбонара')
    print(link_image)