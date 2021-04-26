# encoding=utf8

# from pyDes import *
# import base64
#
#
#
# data = "Please"
# k = des("Yq58713Z1", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
# d = k.encrypt(data)
# print "Encrypted: %r" % base64.b64encode(d)
# # print "Decrypted: %r" % k.decrypt(d)
# # assert k.decrypt(d, padmode=PAD_PKCS5) == data


from pyDes import des, PAD_PKCS5, ECB
import base64

#  秘钥  （如果和Java对接，两边要有相同的秘钥）
DES_SECRET_KEY = 'asdfasdf'
s = '1234567890'.encode()  # 这里中文要转成字节， 英文好像不用
des_obj = des(DES_SECRET_KEY, ECB, DES_SECRET_KEY, padmode=PAD_PKCS5)  # 初始化一个des对象，参数是秘钥，加密方式，偏移， 填充方式
secret_bytes = des_obj.encrypt(s)  # 用对象的encrypt方法加密
s = des_obj.decrypt(secret_bytes)  # 用对象的decrypt方法解密
print(base64.b64encode(secret_bytes))
print(s.decode())
