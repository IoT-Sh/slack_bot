import requests
import secrets
import json

def accessToken():
    url = 'https://bitbucket.org/site/oauth2/access_token'

    auth = secrets.auth

    ref_params = {
        "grant_type":"refresh_token",
        "refresh_token":secrets.ref_token
    }
    auth_params = {
        "grant_type":"authorization_code",
        "code":secrets.auth_token
    }
    try:
        res = requests.post(url, auth=secrets.auth, data=ref_params)

    except:
        res = requests.post(url, auth=secrets.auth, data=auth_params)

    x = json.loads(res.text)

    token = (x["access_token"])
    return token


