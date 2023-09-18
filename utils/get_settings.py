from dataclasses import dataclass

from environs import Env
from utils.check_paths import check_paths
@dataclass
class CredentialsSite:
    host:str
    username:str
    password:str

@dataclass
class JobFiles:
    keys: str
    questions:str
    title: str

@dataclass
class WorkData:
    jb: JobFiles
    cs: CredentialsSite

def get_settings(path:str):
    env = Env()

    cred = f'{path}/credentials.txt'

    env.read_env(cred)

    settings = WorkData(
        jb=JobFiles(
            keys=f'{path}/keys.txt',
            questions=f'{path}/questions.txt',
            title=f'{path}/title.txt',
        ),
        cs=CredentialsSite(
            host=env.str('HOST'),
            username=env.str('LOGIN'),
            password=env.str('PASSWORD')
        )
    )

    check_paths(list(vars(settings.jb).values()))

    return settings