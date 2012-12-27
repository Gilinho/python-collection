import threading
import urllib2

class openWebsite(threading.Thread):
	def __init__(self, urls, output):
		threading.Thread.__init__(self)
		self.urls = urls
		self.output = output

	def run(self):
		while self.urls:
			url = self.urls.pop()
			req = urllib2.urlopen(urllib2.Request(url))
			self.output.write(req.read())

if __name__ == "__main__":
	urls = ["http://yodi.sg", "http://yoodey.com"]
	urls2 = ["http://yodi.me", "http://google.com"]	
	f = open("output.txt", "w+")
	t1 = openWebsite(urls, f)
	t2 = openWebsite(urls2, f)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	f.close()