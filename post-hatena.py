# -*- coding: utf-8 -*-
import datetime
import random
import hashlib
import base64
import requests

def wsse(username, password):
    created = datetime.datetime.now().isoformat() + 'Z'
    nonce = hashlib.sha1(str(random.random())).digest()
    digest = hashlib.sha1(nonce + created + password).digest()
    
    return 'UsernameToken Username="{}", PasswordDigest="{}", Nonce="{}", Created="{}"'.format(username, base64.b64encode(digest), base64.b64encode(nonce), created)


username = 'username'
password = 'api'
blogname = 'blogname.hatenablog.com'
headers = {'X-WSSE': wsse(username, password)}

url = 'http://blog.hatena.ne.jp/{}/{}/atom/entry'.format(username, blogname)

data = """<?xml version="1.0" encoding="utf-8"?>
<entry xmlns="http://www.w3.org/2005/Atom"
       xmlns:app="http://www.w3.org/2007/app">
  <title>title</title>
  <author><name>name</name></author>
  <content type="text/plain">
    content
  </content>
  <updated>2013-09-05T00:00:00</updated>
  <app:control>
    <app:draft>yes</app:draft>
  </app:control>
</entry>
"""

r = requests.post(url, data=data, headers=headers)
print (r)
