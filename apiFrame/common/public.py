import  os
import  datetime


def filePath(fileDir='data',fileName='login.yaml'):
	'''
	:param fileDir: 目录
	:param fileName: 文件的名称
	:return:
	'''
	return os.path.join(
		os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)


def writeContent(content):
	# print('写的时间:',datetime.datetime.now())
	with open(filePath(fileDir='data',fileName='bookID'),'w') as f:
		f.write(str(content))

def readContent():
	# print('读的时间:', datetime.datetime.now())
	with open(filePath(fileDir='data',fileName='bookID'),'r') as f:
		return f.read()






