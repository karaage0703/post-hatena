# post-hatena
python script for posting hatena blog

# Dependency
- Python 2.7
- Requests


# How to use
## Preparation
Execute following command:
```sh
$ git clone https://github.com/karaage0703/post-hatena.git
```

Execute following command to install `requests`:
```sh
$ pip install requests
```

## Setting
 Customize below part of `post-hatena.py` according to your hatena blog setting

~~~~
username = 'username'
password = 'API key'
blogname = 'yourblogname.hatenablog.com'
draft = yes # yes or no
~~~~
## Posting
 Execute below command to post hatena blog. `title.txt` is text file written title and `body.txt` is text file written content.

```sh
$ python post-hatena.py title.txt body.txt
```
