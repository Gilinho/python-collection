"""
Download dependencies:
    sudo pip install greenlet
    sudo pip install gevent

try import gevent in python console.
If problem occur, please check if you have libevent installed.

url.txt : File that contain list of images urls that you want to download.
"""
from gevent import monkey; monkey.patch_socket()
import gevent
from gevent import socket
import urllib2
import os

f = open('url.txt')
data = f.readlines()
f.close()

urls = []
for d in data:
    urls.append(d[:-1])

def download_file(url):
    print('starting %s' % url)
    data = urllib2.urlopen(url).read()
    filename = os.path.basename(url)
    f = open(filename, 'wb')
    f.write(data)
    f.close()

jobs = [gevent.spawn(download_file, url) for url in urls]
gevent.joinall(jobs, timeout=5)

[job.value for job in jobs]

