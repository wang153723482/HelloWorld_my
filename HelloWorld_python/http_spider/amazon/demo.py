import urllib2

url = 'https://amazon.com/gp/your-account/order-history/ref=oh_aui_pagination_3_1?ie=UTF8&orderFilter=year-2016&search=&startIndex=0'

headers = {
    'Host': 'www.amazon.cn',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,de;q=0.6',
    'Cookie': 'x-wl-uid=1ogEyiSA9YK4Y+4nOnwh4L6iDu5baHWHS4vzxVKxjMBGVNBXWn7En4KZ32xJfziqDYq3F7FcP29yMm9R9V9pI26RdL7lxGCKjwbbBOLBl56hWh5eSyFQ+gHam21S1nEjOF6ygB+8iP3c=; lc-acbcn=zh_CN; amznacsleftnav-35363d87-6ad8-3127-81c7-1758b6f22fcc=1; s_vnum=1913503091917%26vn%3D1; s_nr=1481503352984-New; s_dslv=1481503352986; a-ogbcbff=1; session-token="72Jdb9rk+kkYRIwis8i01wOiFFtcPikz1eNJbUys3tjrLrqiLQVI8nevjy0TtZuPQWNsmB0bsge5BFQM4LxDxHzK2v9tWKccN8N3BJyPxMXVd6U4m7A0tRGt6DnmzrW18He4mvzANLVjeiD94czdU7+on9CURuXMwvMI9g3K1EQCLHdqdogIsEpQgg8kywIRQNhnUlf4yJJqpmAamZNaPDSCO0P30ZNF6N7Bg/gvjJ90ZO8lKxnlJFJ+wipypMfzQEJ74f/CxR0="; x-acbcn="nNqh?PA66mB9FaxcEkbsXRuyd3oewD9F"; at-main=Atza|IwEBIEvz2mB2k2OSAi2feiA61MVfE7uXyDLyuBdIbCfVmTC5YRtV0mM90N3gyDIMDuEwlozzu9vF190m87AX3ipa36HzI_sS3-O9wjxJBeQz5RuVnVVF5OG8JSU-8OvDOfrtAHzItOFnZGIkvicX0z0yDPyraAtsKviTL5yjwlUyYJH30wK4BJIqmL_hERKH89RnTaF5OcDmLbRkMjci6lPcF_ajXKdCd3I-CTSLr4T3o5uYPdyZbhr6F6xMLo757Yu-CcLbJSb5A5qZYaE45lh_CyxDkmidzW4UuzSHkYPpZaC5iWDTkua2wJ-Iy8tG-K-2jMPOBz3bcbl682Thgp-1slTFHDPWS4IKbbXnN_rHoPs4tFO95D6cLPWFDN_Zos03gd2FrwyERkDLlv32zGidmzY7; sess-at-main="V9Ww7r1soxz3PHNjZ80ytWNC727RVQV9kw/+kOmeIvU="; ubid-acbcn=454-0441116-5101412; session-id-time=2082729601l; session-id=453-0946315-3319510; csm-hit=0ZWACRQFVNKXD7SJ3EG3+s-T9J8TRMB8GN0GXA1C6B5|1485076872141'
}


request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request).read()
print response