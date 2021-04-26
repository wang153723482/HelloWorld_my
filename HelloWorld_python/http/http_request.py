# encoding=utf8
import requests

r = requests.get('http://www.bigerhead.com')
# print r.text

# 设置代理 proxy
proxies = {
    'http': '127.0.0.1:9999',
    'https': '127.0.0.1:9999'
}

param = {'name': 'wangc', 'age': 12}
r2 = requests.get('http://www.bigerhead.com', proxies=proxies, params=param)
print(r2.text)

print(r2.headers)

print(r2.url)

# 定制请求头
headers = {'user-agent': 'my-app/0.0.1'}
url = 'http://www.bigerhead.com'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)

# 发送json数据
import json

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))
print(r.text)

# 上传文件
# files = {'file':open('a.xls','rb')}
# r = requests.post(url,files=files)
