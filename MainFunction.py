import XlsWriter
import random
import time
import sys
import Baike
import XlsWriter
import urllib.parse
def readFile(urlmanage):
	with open('information.txt') as f:
		for line in f:
			if(line.startswith('#')):
				continue
			url = r"http://baike.baidu.com/search/word?word="+urllib.parse.quote(line)
			urlmanage.add_new_url(url)

if __name__ == "__main__":
	urlmanage = Baike.UrlManager()
	htmlparser = Baike.HtmlParser()
	xlswriter = XlsWriter.XlsWriter()
	readFile(urlmanage)
	count = 0
	while urlmanage.has_new_url and count < 10000:
		url = urlmanage.get_new_url()
		urls,data = htmlparser.parser(url)
		urlmanage.add_new_urls(urls)
		if data is None:
			continue
		xlswriter.fileWriter(data)
		count = count + 1
		#timer = random.randint(1,3)
		#time.sleep(timer)
