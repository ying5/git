from selenium import webdriver
import urllib.request
import http.client
import random
import time
class HtmlDownloader(object):

    def getHtmlByUrlopen(self,url):
        try:
            response = urllib.request.urlopen(url)
            if(response.getcode() == 200):
                context = response.read()
                return context
            return None
        except:
            print('出现一条访问失败的词条')
            timer = random.randint(5,10)
            time.sleep(timer)
            return None

    def getHtmlByPhantojs(self,url):
        self.driver =  webdriver.PhantomJS(
    executable_path=r'D:\tools\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        self.driver.get(url)
        # if(self.driver.getcode() != 200):
        #     return None
        context = self.driver.page_source
        return context

    def getArticleDriver(self,url):
        self.driver = webdriver.PhantomJS(
    executable_path=r'D:\tools\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        self.driver.get(url)
    	# if(self.driver.getcode() != 200):
    	# 	return None
        return self.driver
    def getDriverByPhantojs(self,url):
    	self.driver.get(url)
    	return self.driver


    def getHtmlByHttpLib(self,url):
        conn = http.client.HTTPConnection("www.cnseay.com")   
        conn.request('get', '/')
        res = conn.getresponse()   
        if res.status == 200:
            b = res.read()
            return b
        return