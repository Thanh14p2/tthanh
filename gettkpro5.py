import requests
import json
import os
f = open("token.txt", "w")
file_token = open("tokenacc.txt").read().split("\n")
for token in file_token:
  try:
    get = requests.get("https://graph.facebook.com/me/accounts?access_token="+ token).json()
    data_number=len(get["data"])
    for x in range(int(data_number)):
      try:
        token_page = get["data"][x]
        tokenpage = token_page["access_token"]
      except:
        exit()
      f.write(tokenpage+"\n")
  except:
    print(token+"Thành Công")
    
