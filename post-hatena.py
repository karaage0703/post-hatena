# -*- coding: utf-8 -*-
import datetime
import random
import hashlib
import base64
import requests
import sys

username = 'username'
password = 'API key'
blogname = 'yourblogname.hatenablog.com'
category = 'from post-hatena'
draft = 'yes' # yes or no

def wsse(username, password):
    created = datetime.datetime.now().isoformat() + 'Z'
    nonce = hashlib.sha1(str(random.random()).encode()).digest()
    digest = hashlib.sha1(nonce + created.encode() + password.encode()).digest()
    return 'UsernameToken Username="{}", PasswordDigest="{}", Nonce="{}", Created="{}"'.format(username, base64.b64encode(digest), base64.b64encode(nonce).decode(), created)


def posthatena(data):
    headers = {'X-WSSE': wsse(username, password)}

    url = 'http://blog.hatena.ne.jp/{}/{}/atom/entry'.format(username, blogname)

    r = requests.post(url, data=data, headers=headers)
    print (r.text)

if __name__ == '__main__':

    param = sys.argv
    if (len(param) != 3):
        print ("Usage: $ python " + param[0] + " title.txt body.txt")
        quit()

    with open(param[1]) as f1:
            title = f1.read()

    with open(param[2]) as f2:
        body = f2.read()

    data = """<?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom"
           xmlns:app="http://www.w3.org/2007/app">
      <title>""" + title + """</title>
      <author><name>name</name></author>
      <content type="text/plain">
        """ + body + """
      </content>
      <category term=" """ + category + """ " />
      <app:control>
        <app:draft>""" + draft + """</app:draft>
      </app:control>
    </entry>
    """

    posthatena(data)
