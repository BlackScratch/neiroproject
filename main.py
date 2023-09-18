from utils.get_directories import get_directories
from connector_site.get_token import get_token
from utils.get_settings import get_settings
from connector_site.connect_site import RequestorMysite
from connector_gpt.connect_gpt import RequestorChatGPT

if __name__ == '__main__':
    directories = get_directories('./job_data')

    for directory in directories:
        print(directory)
        try:
            settings = get_settings(path=directory)
            print(settings)

            token_wordpress = get_token(host=settings.cs.host, username=settings.cs.username, password=settings.cs.password)

            requestor_my_site = RequestorMysite(token=token_wordpress, host=settings.cs.host)
            requestro_chat_gpt = RequestorChatGPT(token='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')
        except Exception as exc:
            print(f'Exceprion: {exc}')