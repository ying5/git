import HtmlDownloader
from bs4 import BeautifulSoup
import re
import urllib.parse
class UrlManager(object):
	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()

	def add_new_url(self,url):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def add_new_urls(self,urls):
		if urls is None or len(urls) == 0:
			return None
		for url in urls:
			self.add_new_url(url)

	def has_new_url(self):
		return len(self.new_urls)!=0

	def get_new_url(self):
		url = self.new_urls.pop()
		self.old_urls.add(url)
		return url 

class HtmlParser(object):
	def __init__(self):
		self.__downloader = HtmlDownloader.HtmlDownloader()
		self.__keyword =['疾病','医学术语','医学','科学','医学人物','细菌','科技','生物','内科','抗生素','药物','西药','中药','医疗']
	def _get_new_urls(self,url,soup):
		new_urls = set()
		links = soup.find_all('a',href=re.compile('/view/\d+\.htm'))
		for link in links:
			url = link['href']
			url = 'http://baike.baidu.com'+ url
			new_urls.add(url)
		return new_urls
	def _get_new_data(self,url,soup):
		data = []
		div = soup.find('div',class_='main-content')
		self._removeNiose(div)
		titledd = soup.find('dd',class_='lemmaWgt-lemmaTitle-title')
		title="???"
		if titledd != None:
			title = titledd.find('h1').get_text()
			titledd.decompose()
		text = div.get_text()
		lines = (line.strip() for line in text.splitlines())
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		text = ''.join(chunk for chunk in chunks if chunk)
		data.append(title)
		data.append(text)
		return data
	def _removeNiose(self,div):
		#删除右上角点赞数
		remove = div.find('div',class_='top-tool')
		if remove != None:
			remove.decompose()
		#删除目录
		remove = div.find('div',class_='lemmaWgt-lemmaCatalog')
		if remove != None:
			remove.decompose()
		#删除基本信息
		remove = div.find('div',class_='basic-info cmn-clearfix')
		if remove != None:
			remove.decompose()
		#删除图册
		remove = div.find('div',class_='album-list')
		if remove != None:
			remove.decompose()
		#删除下方标签
		remove = div.find('div',id='open-tag')
		if remove != None:
			remove.decompose()
		#删除医疗提示
		remove = div.find()
	def parser(self,url):
		content = self.__downloader.getHtmlByUrlopen(url)
		if url is None or content is None:
			return None,None
		soup = BeautifulSoup(content,"html.parser",from_encoding = 'utf-8')
		tag = soup.find('div',id='open-tag')
		ok = 0
		if tag != None:
			attrs = tag.find_all('span',class_='taglist')
			if attrs!=None:
				for attr in attrs:
					#print(attr.get_text().strip())
					if(attr.get_text().strip() in self.__keyword):
						ok = 1
						break
		if(ok == 0):
			titledd = soup.find('dd',class_='lemmaWgt-lemmaTitle-title')
			title="???"
			if titledd != None:
				title = titledd.find('h1').get_text()
			print('排除一条信息:'+title)
			return None,None
		urls = self._get_new_urls(url,soup)
		data = self._get_new_data(url,soup)
		return urls,data

