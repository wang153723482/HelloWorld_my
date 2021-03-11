# encoding=utf8
from evernote.api.client import EvernoteClient

token_yx = ''
token_en = ''

client_yx = EvernoteClient(token_yx, sandbox=False, china=True)
client_en = EvernoteClient(token_en, sandbox=False, china=False)



