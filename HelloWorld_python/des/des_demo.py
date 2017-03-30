from pyDes import *
import base64



data = "Please"
k = des("Yq58713Z1", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)
print "Encrypted: %r" % base64.b64encode(d)
# print "Decrypted: %r" % k.decrypt(d)
# assert k.decrypt(d, padmode=PAD_PKCS5) == data