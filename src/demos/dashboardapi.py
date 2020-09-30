'''
Created on 6 ago. 2020

@author: msanavarro
'''
import requests
import json

meraki_api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
url = "https://api.meraki.com/api/v0/organizations/"+'549236'+"/networks"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
networks = requests.get(url,headers=headers)
networks = networks.json()
for network in networks:
    print(network['name'])