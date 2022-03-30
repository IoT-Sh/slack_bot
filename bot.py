import requests
import json
import schedule
import time
import secrets
from token_generation import accessToken

author = []

def send_message(req_count):

    header = 'Content-type: application/json'

    for i in range(len(req_count)):
        msg = req_count[i]+" has pull request"
        
        data = '{"text":'+'"'+msg+'"'+'}'
        print(data)
        url = secrets.bot_url
        print(url)

        response = requests.post(url,data=data)
        print(response.text)



def get_request():
    url = secrets.bitbucket_url
    access_token = accessToken()

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer <"+access_token+">"
    }
    response = requests.get(url,headers=headers)
    y = json.loads(response.text)

    

    request_count = (y["values"])
    for i in range(len(request_count)):
        s = (request_count[i]["author"]["display_name"])
        author.append(s)

    return author

def main():
    request_count = get_request()
    send_message(request_count)

if __name__ == '__main__':

    schedule.every().day.at("09:00").do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)