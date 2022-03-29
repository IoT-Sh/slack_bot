import requests
import json
import secrets
from token_generation import accessToken

last_commit = 0
access_token = accessToken()

def send_message(req_count):
    header = 'Content-type: application/json'

    msg = "someone requesting to pull"
    data = '{"text":'+'"'+msg+'"'+'}'
    url = secrets.bot_url

    response = requests.post(url,data=data)
    last_commit = get_request()
    print(response.text)
    return last_commit



def get_request():
    url = secrets.bitbucket_url

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer <"+access_token+">"
    }
    response = requests.get(url,headers=headers)
    y = json.loads(response.text)
    request_count = (y["size"])

    return request_count



if __name__ == '__main__':
    while True:
        request_count = get_request()
        
        if(request_count>last_commit):
            last_commit = send_message(request_count)

        else:
            print("no request found")