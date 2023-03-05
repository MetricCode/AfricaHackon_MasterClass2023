#!/usr/bin/env python3
#Author : M3tr1c_r00t

import base64
import requests
from urllib.parse import unquote

url = "http://wcamxwl32pue3e6m5l3n94wbq36o4nzy8kr5snzk-web.cybertalentslabs.com/index.php"
s = requests.Session()

get = s.get(url)

cookies = unquote(get.cookies['secret'])

decoded_cookie = base64.b64decode(cookies).decode()

post =  s.post(url,data={'Q': decoded_cookie})

#respost = requests.post(url,data = data)
print(post.text)

