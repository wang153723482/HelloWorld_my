d = u'\u81e7\u73ca'

utf8string = d.encode("utf-8")
f = open('a.txt','w')
f.write(utf8string)
f.close()



# 以下内容未进行测试
# 
# unicodestring = u"Hello world"
# # 将Unicode转化为普通Python字符串："encode"  
# utf8string = unicodestring.encode("utf-8")
# asciistring = unicodestring.encode("ascii")
# isostring = unicodestring.encode("ISO-8859-1")
# utf16string = unicodestring.encode("utf-16")
# # 将普通Python字符串转化为Unicode："decode"  
# plainstring1 = unicode(utf8string, "utf-8")
# plainstring2 = unicode(asciistring, "ascii")
# plainstring3 = unicode(isostring, "ISO-8859-1")
# plainstring4 = unicode(utf16string, "utf-16")
# assert plainstring1 == plainstring2 == plainstring3 == plainstring4