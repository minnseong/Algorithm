# 넥토리얼 코딩테스트 10/07 2022
# Q6 - 100

import requests
import json

def getPhoneNumbers(country, phoneNumber):
    res = requests.get("https://jsonmock.hackerrank.com/api/countries?name=" + country)

    json_obj = json.loads(res.text)

    if not json_obj["data"]:
        return -1

    return "+" + str(json_obj['data'][0]["callingCodes"][-1]) + " " + str(phoneNumber)


print(getPhoneNumbers("Afghanistan", 656445445))
print(getPhoneNumbers("Puerto Rico", 564593986))
print(getPhoneNumbers("Oceania", 987574876))
