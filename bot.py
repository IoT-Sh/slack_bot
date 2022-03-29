def send_message(msg):
    header = 'Content-type: application/json'
    data = '{"text":'+'"'+msg+'"'+'}'
    url = 'https://hooks.slack.com/services/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'

    response = requests.post(url,data=data)
    print(response.text)

def main():


if __name == '__main__':
    