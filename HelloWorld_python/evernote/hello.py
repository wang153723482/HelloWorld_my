from evernote.api.client import EvernoteClient

developer_token = "yinxiang dev token"

dev_token = developer_token
client = EvernoteClient(token=dev_token, sandbox=False, china=True)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username

note_store = client.get_note_store()
notebooks = note_store.listNotebooks()
for notebook in notebooks:
    print "Notebook: ", notebook.name
