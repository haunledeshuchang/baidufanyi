import requests
import json
url='https://fanyi.baidu.com/basetrans'
qury_string=input('请输入中文内容：')
data={'query': qury_string,
              'from': 'zh',
              'to': 'en'}
headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
response=requests.post(url,data=data,headers=headers)
html_str=response.content.decode()
dic_str=json.loads(html_str)
print(dic_str)

print(type(dic_str))
#ret=dic_str['trans'][0]['dst']
ret=dic_str['trans'][0]['src']

print('翻译结果是：',ret)
