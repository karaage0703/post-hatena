# post-hatena
python script for posting hatena blog

# How to use
## Clone this repository
~~~~
$ git clone https://github.com/karaage0703/post-hatena.git
~~~~

maybe you need <code>requests</code> library. Execute below command

~~~~
$ sudo pip install requests
~~~~

## Preparation
 Customize below part of `post-hatena.py` according to your hatena blog setting

~~~~
username = 'username'
password = 'API key'
blogname = 'yourblogname.hatenablog.com'
draft = yes # yes or no
~~~~
## Posting
 Execute below command to post hatena blog. `title.txt` is text file written title and `body.txt` is text file written content.

~~~~
$ post-hatena.py title.txt body.txt
~~~~
