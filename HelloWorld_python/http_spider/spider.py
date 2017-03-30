import urllib2


url = 'http://item.jd.hk/1952014601.html'
url_item = urllib2.urlopen(url,'utf-8')
html_source = url_item.read()
print html_source
url_item.close()