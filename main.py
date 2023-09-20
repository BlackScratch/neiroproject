from utils.get_directories import get_directories
from connector_site.get_token import get_token
from utils.get_settings import get_settings
from connector_site.connect_site import RequestorMysite
from connector_gpt.connect_gpt import RequestorChatGPT
import betterlogging as logging
import sys
from create_content.get_data import CreateContent

if __name__ == '__main__':
    if sys.platform == 'win32':
        logging.basic_colorized_config(level=logging.DEBUG, format="%(asctime)s - [%(levelname)s] - %(name)s - %(filename)s.%(funcName)s.%(lineno)d - %(message)s")
    else:
        logging.basic_colorized_config(level=logging.DEBUG, filename='logging.log', filemode='a',format="%(asctime)s - [%(levelname)s] - %(name)s - %(filename)s.%(funcName)s.%(lineno)d - %(message)s")

    directories = get_directories('./job_data')

    for directory in directories:
        logging.info(directory)
        try:
            settings = get_settings(path=directory)
            logging.info(settings)

            token_wordpress = get_token(host=settings.cs.host, username=settings.cs.username, password=settings.cs.password)

            requestor_my_site = RequestorMysite(token=token_wordpress, host=settings.cs.host)
            requestor_chat_gpt = RequestorChatGPT(token='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')

            create_content = CreateContent(file_keys=settings.jb.keys, file_title=settings.jb.title, file_questions=settings.jb.questions,requestor_gpt=requestor_chat_gpt,requestor_site=requestor_my_site)
            create_content.generate_content()
        except Exception as exc:
            logging.error(f'Exception: {exc}')