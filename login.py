""" This is short example login function """


def login_with_username(device, username, password, cookies):
    url = ""
    body = {
        "mix_mode": "1",
        "multi_login": "1",
        "password": xorEncrypt(password),
        "account_sdk_source": "app",
        "username": xorEncrypt(username)
    }
    params = {
       
      ''' Available after purchase '''
    
    }
    url = url + urlencode(params)
    
    gorgon = xgorgon()
    stub = md5stub(urlencode(body).encode())
    headers = {
         ''' Available after purchase '''
    }

    r = client.post(url, data=body, headers=headers)
    headers = header2dict(r.headers)
    cookie = parsecookie(r.cookies)
    result = {"headers": headers, "cookie": cookie, "response": r.json()}
    return result
