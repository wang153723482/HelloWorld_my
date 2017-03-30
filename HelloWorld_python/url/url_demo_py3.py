
import urllib.parse

s = urllib.parse.quote('sdkf3243{}":|>?<')
print(s)

ss = urllib.parse.unquote(s)
print(ss)