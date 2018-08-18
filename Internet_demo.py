# from urllib.request import urlopen
#
# for line in urlopen('https://www.baidu.com/'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     print(line)

# 处理get请求，不传data，则为get请求

# import urllib
# from urllib.request import urlopen
# from urllib.parse import urlencode
#
# url = 'http://116.228.77.183:25080/crmuat/action/base/user/dmslogin'
# data = {"username": "LK001", "password": "111111"}
# req_data = urlencode(data)  # 将字典类型的请求数据转变为url编码
# res = urlopen(url + '?' + req_data)  # 通过urlopen方法访问拼接好的url
# res = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
#
# print(res)
# 处理post请求,如果传了data，则为post请求

import urllib
from urllib.request import Request
from urllib.parse import urlencode
from urllib.request import urlopen

url = 'http://116.228.77.183:25080/crmuat/action/base/user/dmslogin'
data = {"username": "LK001", "password": "111111"}
data = urlencode(data)  # 将字典类型的请求数据转变为url编码
data = data.encode('ascii')  # 将url编码类型的请求数据转变为bytes类型
req_data = Request(url, data)  # 将url和请求数据处理为一个Request对象，供urlopen调用
with urlopen(req_data) as res:
    res = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

print(res)
