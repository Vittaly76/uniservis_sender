import requests
import re
#r = requests.get("https://lkcab.ru/?login=yes")
#print (r)
#print (r.text)
session = requests.Session()
url = "https://lkcab.ru/?login=yes"
r= post_request = session.post(url, {
#     'backUrl': 'https://moscow.hh.ru/',
     'AUTH_FORM': 'Y',
     'TYPE': 'AUTH',
     'USER_LOGIN': '+7(***)***-**-**',
     'USER_PASSWORD': '***',
#     '_xsrf':_xsrf,
#     'remember':'yes',
  })
  
#PHPSESSID = session.cookies.get('PHPSESSID')
print (r)
#print (r.text)

match = re.search(r'\'bitrix_sessid\':\'(\w*)\'', r.text)

print (match.group(1))

session_cookies = session.cookies
cookies_dictionary = session_cookies.get_dict()
print(cookies_dictionary)
