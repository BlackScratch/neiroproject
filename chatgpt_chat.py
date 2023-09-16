import httpx

url = 'https://api.openai.com/v1/chat/completions'

token = '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'

messages = [
    {
        'role':'system',
        'content':' Тебя зовут Бильбо Торбинс и ты самый медленный фермер во вселенной'
    }
]

question = 'Как тебя зовут и чем занимаешься?'

messages.append({
    'role': 'user',
    'content': question
})

data = {
    'model':'gpt-3.5-turbo',
    'messages': messages
}

auth = ('Bearer', token)

with httpx.Client(timeout=30) as client:
    response = client.post(url=url, auth=auth, json=data)

print(response.json())
print(response.json()['choices'][0]['message']['content'])