import requests

url = "https://api.ciscospark.com/v1/messages"

payload = "{\n  \"roomId\": \"Y2lzY29zcGFyazovL3VzL1JPT00vOTUxNjhjODAtYjRkOC0xMWVhLWE4NjgtM2I1NDc5YzA0NzQz\",\n  \"text\": \"Hello World!\"\n}"
headers = {
  'Authorization': 'Bearer MmM1MzJlNmQtZjVlNS00YTk0LWI5YTktOTE0MWNkZWY0ZDllZWFhNGM0YTUtNzJk_PF84_consumer',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
