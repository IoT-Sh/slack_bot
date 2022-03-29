import requests

url = "https://bitbucket.org/site/oauth2/access_token"

payload={}
files=[

]
data = {
  'grant_type=authorization_code&code=e5jCUJyztSx8ArB5GR'

}

response = requests.post(url,data=data)

print(response.text)