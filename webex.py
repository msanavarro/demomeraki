import requests

url = "https://api.ciscospark.com/v1/rooms"

payload = {}
headers = {
  'Authorization': 'Bearer MmM1MzJlNmQtZjVlNS00YTk0LWI5YTktOTE0MWNkZWY0ZDllZWFhNGM0YTUtNzJk_PF84_consumer'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
