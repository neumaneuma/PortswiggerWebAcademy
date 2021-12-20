import requests

requests.packages.urllib3.disable_warnings()

verify = False
proxy = "127.0.0.1:8080"
scheme = "https://"
proxies = {scheme: proxy}
host_domain = ".web-security-academy.net"


def post(host_subdomain, data, session_cookie="", path=""):
    cookies = {"session": session_cookie}
    host = host_subdomain + host_domain
    url = scheme + host + path
    requests.post(url, verify=verify, proxies=proxies,
                  cookies=cookies, data=data)


def get(host_subdomain, params, session_cookie="", path=""):
    cookies = {"session": session_cookie}
    host = host_subdomain + host_domain
    url = scheme + host + path
    requests.get(url, verify=verify, proxies=proxies,
                 cookies=cookies, params=params)
