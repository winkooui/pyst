import json

#webdrive获取cookie
def Get_Cookie(wd):
    cookies = wd.get_cookies() #获取cookie
    print(cookies)
    cookiesFile = json.dumps(cookies)
    with open(r'D:\cookiesFile.json', 'w') as f:
        f.write(cookiesFile)