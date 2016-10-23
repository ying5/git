import HtmlDownloader
from bs4 import BeautifulSoup
import re
import urllib.parse
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

#class HtmlParser(object):

class HtmlDownloader(object):
	def __init__(self):
		pass

	def download(self):
		self.__driver = webdriver.PhantomJS(
    executable_path=r'D:\tools\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
		url = r'http://epub.cnki.net/'
		self.__driver.get(url)
		print('?')
		js = 'document.getElementById("rehidenavlist").style.display="block"'
		self.__driver.execute_script(js)
		print('!')
		div = self.__driver.find_element_by_id('rehidenavlist')
		keya = div.find_elements_by_tag_name('li')
		href = keya[4].find_element_by_tag_name('a')
		href.click()
		self.__driver.switch_to_frame('iframeResult')
		wait = WebDriverWait(self.__driver, 30)
		print("@")
		try:
			wait.until(expected_conditions.visibility_of_element_located(By.CLASS_NAME, "fz14"))
		except:
			print('传输超时！')
		self.articleDolad()
		#print(self.__driver.page_source)
		#test = self.__driver.find_element_by_id('SqlValue')
		#print(test)
		#self.__driver.switch_to_window(self.__driver.window_handles[1])
		#tests = self.__driver.find_elements_by_class_name('fz14')
		#title - self.__driver.getWindowHandle()
		#print(driver.current_url)
		#print(title)
		pass

	def articleDolad(self):
		print("2")
		hrefs = self.__driver.find_elements_by_class_name('fz14')
		for href in hrefs:
			print(href.text)
			href.click()
			try:
				wait.until(expected_conditions.visibility_of_element_located(By.ID, "ChDivKeyWord"))
				#self.__driver.switch_to_window(self.__driver.window_handles[1])
				print(self.__driver.page_source)
			except:
				print("heheda")
			break

