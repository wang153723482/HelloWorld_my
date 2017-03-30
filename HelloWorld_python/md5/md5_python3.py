# python3.*

import hashlib
m = hashlib.md5()

# m.update(b"123") #参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误  
# md5value=m.hexdigest()
# print(md5value)  #bb649c83dd1ea5c9d9dec9a18df0ffe9  

s = '123'
m.update(s.encode(encoding="utf-8"))
md5v = m.hexdigest()
print(md5v)