import requests, time ,threading
id =input("nhập id của bạn:")
def url():
 while True:
  url = requests.get(f'https://faceslitevn.site/grap/index.php?id={id}').json
  print(url)
threads=[]
for i in range(5000):
    kk=threading.Thread(target=url)
    kk.start()
  

  


