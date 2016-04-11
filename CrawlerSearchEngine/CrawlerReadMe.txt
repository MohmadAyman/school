usage of oldclawrer
python3.4 oldclawrer <maxPages per url> <numberofThreads>
to add urls, look line:138

usage of clawrer
python3.4 clawrer <numberofThreads> <maxTotalPages>
to add urls, look line:134

explination for clawrer:
	an array of urls is shared between all the threads, each thread first enters the loop
	acquires the lock, then process the first url and deletes it, then releases the lock.
	for the frecuency of the search, the sites that ends with a '.org' will have a more in 
	depth crawling than the others.
	the comments carry more details.
