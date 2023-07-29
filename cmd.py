import requests

# print(get('https://ipapi.co/ip/').text)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
link = "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjCopjUtbSAAxVGhP0HHfC6DqgQFnoECA0QAQ&url=https%3A%2F%2Fgorganwebsite.ir%2F&usg=AOvVaw0ASimS7R51lxT0K72l41zW&opi=89978449"
num = 0
while 1:
    print(num ," ", requests.get(link,headers))
    num+=1