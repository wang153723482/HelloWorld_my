import base64
s = 'i am string'
a = base64.b64encode(s)
print a
# ztLKx9fWt/u0rg==
print base64.b64decode(a)