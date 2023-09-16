import httpx


url = 'https://api.openai.com/v1/images/generations'

token = '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'

prompt = 'Паста карбоанара'

data = {
    'prompt': prompt,
    'n': 1,
    'size': '1024x1024'
}

auth = ('Bearer', token)

with httpx.Client(timeout=30) as client:
    response = client.post(url=url, auth=auth, json=data)

print(response.json())

print(response.json()['data'][0]['url'])

