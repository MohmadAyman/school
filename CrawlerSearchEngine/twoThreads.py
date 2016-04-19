from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
from concurrent import futures	
from urllib import robotparser
import threading
import sys
import time
import os.path

# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
class LinkParser(HTMLParser):
	visited = []
	numVisited = 0
	# This is a function that HTMLParser normally has
	# but we are adding some functionality to it
	def handle_starttag(self, tag, attrs):
		# We are looking for the begining of a link. Links normally look
		# like <a href="www.someurl.com"></a>
		if tag == 'a':
			for (key, value) in attrs:
				if key =='href':
					# We are grabbing the new URL. We are also adding the
					# base URL to it. For example:
					# www.netinstructions.com is the base and
					# somepage.html is the new URL (a relative URL)
					#
					# We combine a relative URL with the base URL to create
					newUrl = parse.urljoin(self.baseUrl, value)
					# And add it to our colection of links:
					self.links = self.links + [newUrl]

	# This is a new function that we are creating to get links
	# that our spider() function will call
	def getLinks(self, url):
		self.links = []
		# Remember the base URL which will be important when creating
		# absolute URLs
		self.baseUrl = url
		# Use the urlopen function from the standard Python 3 library
		response = urlopen(url)
		# Make sure that we are looking at HTML and not other things that
		# are floating around on the internet (such as
		# JavaScript files, CSS, or .PDFs for example)
		if response.getheader('Content-Type')=='text/html':
			htmlBytes = response.read()
			# Note that feed() handles Strings well, but not bytes
			# (A change from Python 2.x to Python 3.x)
			htmlString = htmlBytes.decode("utf-8")
			self.feed(htmlString)
			return htmlString, self.links
		else:
			return "",[]

# And finally here is our spider. It takes in an URL, a word to find,
# and the number of pages to search through before giving up
def spider(url,superMaxPages):
	print(threading.current_thread())

	toBeProcessed = threading.local()
	data = threading.local()
	parser = threading.local()
	links = threading.local()

	urlLock = threading.Lock()
	lock = threading.Lock()
	writeLock = threading.Lock()
	writeLockFile = threading.Lock()

	# Start from the beginning of our collection of pages to visit:
	# frequency of visitingg the URL, we chose it to be based on the domain (to be easier for us)
	while 1:
		if len(url)>100:
			del url[0]

#		if LinkParser.numVisited > int(maxPages):
		if LinkParser.numVisited > maxPages:
			print ('max pages reached')
			break

		lock.acquire()
		try:
			if not url:
				print('first continue')
				lock.release()
				continue
			else:
				print('to be processed ')
				toBeProcessed = url[0]
				del url[0]
		except:
			print('first lock Failed')
			lock.release()
			time.sleep(0.01)
			continue
			# lock the vistied list, since more than one thread reads and writes to it.
		lock.release()
		# In case we are not allowed to read the page -> delete url -> continue.
		try:
			rp = robotparser.RobotFileParser()
			rp.set_url(toBeProcessed +'/robots.txt')
			rp.read()
			if not(rp.can_fetch("*", toBeProcessed)):
				print('second continue')
				continue
		except:
			print('cant find the robot file')
			continue

		try:
			parser = LinkParser()
			data, links = parser.getLinks(toBeProcessed)		
			# Add the pages that we visited to the end of our collection
			# of pages to visit:
			writeLockFile.acquire:
				w = open(LinkParser.numVisited+'.html','w+')					
				w.write(data)
				w.close()
			writeLockFile.release()
		
			urlLock.acquire()
			try:
				url = url + links
			except:
				print('url lock failed')
				time.sleep(0.01)
				urlLock.release()
				continue
			urlLock.release()
			print("One more page added from &i",threading.get_ident())
		except:
			print("Couldnt exctract links from the page")

		if toBeProcessed in LinkParser.visited:
			continue

		LinkParser.visited.append(toBeProcessed)

		LinkParser.numVisited += 1

		writeLock.acquire()
		try:
			f.write(toBeProcessed+'\n')
		finally:
			writeLock.release()

class myThread (threading.Thread):
	def __init__(self, url, maxPages):
		threading.Thread.__init__(self)
		self.maxPages = maxPages
		self.url = url
	def run(self):
		spider (url, maxPages)


def file_len(fname):
	with open(fname) as f:
		return(sum(1 for _ in f))


if __name__ == '__main__':

# Retirve previously made list.
	if (os.path.isfile("urls.txt")): 
		length = file_len("urls.txt")
		print (length)
		f = open('urls.txt','r+')
		print('opened')	
		for x in range(length):
			LinkParser.visited.append(f.readline().strip('\n'))
	else:
		f = open('urls.txt','w+')					

	threads = []
	url = []
	url.append("https://docs.python.org/2/py-modindex.html")
	url.append("https://docs.python.org/4/py-modindex.html")
	url.append("https://docs.python.org/3/py-modindex.html")
	l = [ 'http://sphinx-doc.org/', 'http://sphinx-doc.org/contents.html', 'http://sphinx-doc.org/']
	url = url + l

	numberOfThreads = sys.argv[1]
#	maxPages = sys.argv[2]
	maxPages = 8
	for i in range(0,int(numberOfThreads)):
		threads.append(myThread( spider, (url,maxPages) ))	# This value is overriden in the function Spider #

	print("Number of created threads is ", threading.active_count(), "threads len is" , len(threads))

	for i in range(0,int(numberOfThreads)):
		threads[i].start()

	print("Number of created threads is ", threading.active_count(), "threads len is" , len(threads))

	for j in range(0,int(numberOfThreads)):
		threads[j].join()

	# This zero should be overriden after we know the number of acual urls crawled.
	#f.write('0')		# This '0' means the Indexer was here, -the indexer sets the '0'-,	// Fares.
										# if it is 'x', then, 'x' pages have been added to the list, since last time the indexer has indexed.
										# This is done to save the indexer from re indexing indexed pages.
	f.close()
