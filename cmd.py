import requests

# print(get('https://ipapi.co/ip/').text)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
link = "gorganwebsite.ir"
num = 0
while 1:
    print(num ," ", requests.get(link,headers))
    num+=1