from urllib import urlencode
from urllib import quote
from urllib import unquote
data = { 'a': 'test',  'name': 's' }
print urlencode(data)

print quote('{"name":"wangc"}') 
print unquote('%7B%22name%22%3A%22wangc%22%7D') 
