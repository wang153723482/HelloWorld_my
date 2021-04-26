# encoding=utf8
from evernote.api.client import EvernoteClient

developer_token = "token"

dev_token = developer_token
client = EvernoteClient(token=dev_token, sandbox=False, china=True)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username

note_store = client.get_note_store()
notebooks = note_store.listNotebooks()
# for notebook in notebooks:
#     print "Notebook: ", notebook.name

print note_store.getSyncState()

note = note_store.getNote(dev_token, 'e36cf272-1fa8-4aad-a608-f71f2bab3a04', True, True, True, True)
print note.title
print '======================'
# print note.updated
print '======================'
# print note.content
print '======================'
ress = note.resources
for res in ress:
    print '-----'
    print str(res).decode('utf-8')

    pass

# 列出第一个笔记本中的所有笔记的标题
notebookGuid = note_store.listNotebooks()[0]
f = note_store.NoteFilter
f.notebookGuid = notebookGuid
# for note in note_store.findNotes(dev_token, f, 0, 2).notes:
#     print(note.title)
