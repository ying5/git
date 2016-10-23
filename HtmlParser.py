from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import ImageReader
import HtmlDownloader
class HtmlParser(object):
	htmldownloader = HtmlDownloader.HtmlDownloader()
	imagereader = ImageReader.ImageReader()
	def parseOfficialAccountHtml(self,url):
		driver = self.htmldownloader.getDriverByPhantojs(url)
		try:
			href = driver.find_element_by_id('sogou_vr_11002301_box_0').get_attribute('href')
			return href
		except NoSuchElementException:
			raise

		# if(context == None):
		# 	return None
		# soup = BeautifulSoup(context,'html.parser',from_encoding='utf-8')
		# node = soup.find('div', id='sogou_vr_11002301_box_0')
		# return node['href']


	def parseSpecialAccount(self,url):
		# context = self.htmldownloader.getHtmlByPhantojs(url)
		# if(context == None):
		# 	return None
		# else:
		# 	soup = BeautifulSoup(context,'html.parser',from_encoding='utf-8')
		# 	nodes = soup.find_all('h4', class_='weui_media_title')
		# 	return nodes
		driver = self.htmldownloader.getDriverByPhantojs(url)
		if(self.imagereader.dealwithimage(driver)):
			#print('出现验证码干扰')
			driver.refresh()
			try:
				nodes = driver.find_elements_by_css_selector('h4.weui_media_title')
			except NoSuchElementException:
				return None
			return nodes
		else:
			nodes = driver.find_elements_by_css_selector('h4.weui_media_title')
			return nodes

	def parseArticl(self,url):
		driver = self.htmldownloader.getArticleDriver(url)
		L = ['No_Such_value','No_Such_value','No_Such_value','No_Such_value']
		try:
		    title = driver.find_element_by_id('activity-name')
		    L[0] = title.text
		    readnum = driver.find_element_by_id('sg_readNum3')
		    L[1] = title.text
		    likenum = driver.find_element_by_id('sg_likeNum3')
		    L[2] = title.text
		    context = driver.find_element_by_id('js_article').text
		except NoSuchElementException:
			return  L
		soup = BeautifulSoup(context,'html.parser',from_encoding='utf-8')
		text = soup.get_text()
		lines = (line.strip() for line in text.splitlines())
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		text = ''.join(chunk for chunk in chunks if chunk)
		return title.text,readnum.text,likenum.text,text

