import requests
import json

last_commit = 0

def send_message(req_count):
    header = 'Content-type: application/json'

    msg = "someone requesting to pull"
    data = '{"text":'+'"'+msg+'"'+'}'
    url = 'https://hooks.slack.com/services/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'

    response = requests.post(url,data=data)
    last_commit = get_request()
    print(response.text)
    return last_commit



def get_request():
    url = "https://api.bitbucket.org/2.0/repositories/grapes-web-app/grapsweb/pullrequests"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer <kuphNlzEibrV9Z2nJeSEzwJZ5E3KHS6OOr1USMzRReqZOnWivOxm3UVqxckfj-o92MdxdXC7c9aAiuHwg0iodBqSHnhl9Vw6WSdN_12jOSk0ixk5aRoe7pgR>"
    }
    response = requests.get(url,headers=headers)
    y = json.loads(response.text)
    request_count = (y["size"])
    print(request_count)
    return request_count



if __name__ == '__main__':
    while True:
        request_count = get_request()
        
        print(request_count,last_commit)
        if(request_count>last_commit):
            last_commit = send_message(request_count)
            print("sending")

        else:
            print("no commited")