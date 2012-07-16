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

from gevent.pool import Pool
pool = Pool(30)
N = 30

f = open('images-urllist.txt')
data = f.readlines()
f.close()

urls = []
for d in data:
    urls.append(d[:-1])

finished = 0

def download_file(url):
    global finished
    print('starting %s' % url)
    try:
        data = urllib2.urlopen(url, timeout=10000)
    except urllib2.URLError, e:
        print 'e : ' % e
    else:
        data = data.read()
        filename = os.path.basename(url)
        f = open(filename, 'wb')
        f.write(data)
        f.close()
    finally:
        finished += 1


with gevent.Timeout(10000000, False):
    for x in xrange(10, 10 + N):
        jobs = [pool.spawn(download_file, url) for url in urls]
        pool.join(jobs)

print('Finished %s' % (finished, N))

