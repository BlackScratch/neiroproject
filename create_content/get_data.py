from connector_gpt.connect_gpt import RequestorChatGPT
from connector_site.connect_site import RequestorMysite
from utils.rotate_line_file import rotate_elements
from dataclasses import dataclass
from typing import Optional
import betterlogging as logging
@dataclass()
class Data:
    questions: Optional[str]=None
    header: Optional[str]=None

class CreateContent:
    def __init__(self, file_keys:str, file_questions:str, file_title:str, requestor_gpt:str, requestor_site:str):
        self.file_keys = file_keys
        self.file_questions = file_questions
        self.file_title = file_title
        self.requestor_gpt = requestor_gpt
        self.requestor_site = requestor_site


    def _get_theme(self):
        return rotate_elements(filename=self.file_keys)

    def _get_questions(self, theme:str):
        result=[]
        with open(file=self.file_questions, mode='r', encoding='utf-8') as file:
            for line in file:
                elements = line.strip().replace('%theme%', theme).split('|')
                data=Data(*elements)
                result.append(data)
        return result
    def _get_data_for_content(self):
        theme = self._get_theme()
        questions = self._get_questions(theme=theme)
        return theme, questions
    def generate_content(self):
        theme, questions = self._get_data_for_content()
        logging.info(theme)
        logging.info(questions)