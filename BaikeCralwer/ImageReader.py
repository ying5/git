from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from PIL import Image,ImageEnhance,ImageFilter
import pytesseract
import urllib.request
class ImageReader(object):
	def __init__(self):
		self.__filename = '1.png'
	def findImage(self,driver):
		pass

	def dealwithimage(self,driver):
		try:
			self.__imageurl = driver.find_element_by_id('verify_img').get_attribute('src')
			self.__inputarea = driver.find_element_by_id('input')
			self.__bt = driver.find_element_by_id('bt')
			self.__change = driver.find_element_by_id('verify_change')
			print('发现验证码！！')
			#self.userFunction()
			return True
		except NoSuchElementException:
			print('未发现验证码.....')
			return False

	def userFunction(self):
		self.imageSave()
		im = Image.open(self.__filename)
		im.show()
		code = input()
		# while(code =='H'):
		# 	self.__change.click()
		# 	self.__imageurl = driver.find_element_by_id('verify_img').get_attribute('src')
		# 	self.imageSave()
		# 	im = Image.open(self.__filename)
		# 	im.show()
		# 	code = input()
		self.__inputarea.send_keys(code)
		self.__bt.click()
	def imageSave(self):
		urllib.request.urlretrieve(self.__imageurl, self.__filename)
	def deletePicture(self):
		try:
			os.remove(self.__filename)
		except OSError:
			pass
