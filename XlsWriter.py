import xlrd
import xlwt
import datetime
from xlrd import open_workbook

class XlsWriter(object):
	__count = 0
	def __init__(self):
		self.__count = 0
		self.__file = xlwt.Workbook()
		self.getFilename()
		self.__table = self.__file.add_sheet('sheet name')
	def fileWriter(self,L = []):
		temp = 0
		for name in L:
			self.__table.write(self.__count,temp,name)
			temp = temp + 1
		self.__count = self.__count + 1
		print('百度词条'+L[0]+'写入成功')
		self.saveFile()
	def getFilename(self):
		i = datetime.datetime.now()
		times = str(i.year)+'-'+str(i.month)+'-'+str(i.day)+'-'+str(i.hour)+'-'+str(i.minute)
		self.__filename = times+'.xls'

	def saveFile(self):
		self.__file.save(self.__filename)