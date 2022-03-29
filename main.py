import requests
import json


url = "https://api.bitbucket.org/2.0/repositories/grapes-web-app/grapsweb/pullrequests"

headers = {
   "Accept": "application/json",
   "Authorization": "Bearer <OtiiJO5r5YMDq6-lOGmbVibw-QWUQnqFNOjs22jNBMXJEe5vH4gKdGdPZOIoir94gRdKsVyrB8KE_2FSvdWhABVWUacrfdiq5Az0Sj3t9r3mphYwrBDFfWz5>"
}

response = requests.request(
   "GET",
   url,
   headers=headers
)

y = json.loads(response.text)
print(y["size"])

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))