from bs4 import BeautifulSoup
import HtmlParser
import urllib.parse
import time
import random
from selenium.common.exceptions import NoSuchElementException

class UrlManager(object):
    officialaccounturl = {}
    #officialname = ['东华纺织','纺院研究生','华阳自强志愿者','东华纺织社区','东华纺科协','纺院科学商店','红色经纬','东华服院分团委','东华服院学生会']
    officialname = []
    failofficialname = []
    articlemap = {}
    htmlparser = HtmlParser.HtmlParser()
    def __init__(self):
        with open('information.txt') as f:
            for line in f:
                if(line.startswith('#')):
                    continue
                self.officialname.append(line[:-1])
    def updateAccountsUrl(self):
        for name in self.officialname:
            timer = random.randint(1,5)
            time.sleep(timer)
            try:
                self.updateAccountUrlByName(name)
            except NoSuchElementException:
                continue

    def updateAccountUrlByName(self,name):
        factor = "http://weixin.sogou.com/weixin?query=" + urllib.parse.quote(name)
        try:
            url = self.htmlparser.parseOfficialAccountHtml(factor)
            print('公众号: ' + name + '访问成功')
            self.officialaccounturl[name] = url
        except NoSuchElementException:
            print('公众号: ' + name + '访问失败')
            self.failofficialname.append(name)
            raise
        # if(url == None):
        #     print('公众号: ' + name + '访问失败')
        #     self.failofficialname.append(name)
        # else:
        #     print('公众号: ' + name + '访问成功')
        #     self.officialaccounturl[name] = url

    def addOfficialAccount(selfname):
        self.officialname.append(name)

    def addAccountArticleUrl(self,name,urls):
    	self.articlemap[name] = urls

    def getAccountArticleUrl(self,name):
    	if name in self.officialaccounturl:
            url = self.officialaccounturl[name]
            nodes = self.htmlparser.parseSpecialAccount(url)
            if nodes == None:
                print('并没有公众号: '+name+'的地址')
                return
            temp = []
            for node in nodes:
                newurl = 'http://mp.weixin.qq.com' + node.get_attribute('hrefs')
                temp.append(newurl)
                self.addAccountArticleUrl(name,temp)
    	else:
    		print('并没有公众号: '+name+'的地址')