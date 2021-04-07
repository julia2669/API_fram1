import  xlrd
from common.public import filePath
from utils.operationYaml import OperationYaml
from common.public import *
import  json

class ExcelVarles:
	caseID="测试用例ID"
	caseModel="模块"
	caseName="接口名称"
	caseUrl="请求地址"
	casePre="前置条件"
	method="请求方法"
	paramsType="请求参数类型"
	params="请求参数"
	expect="期望结果"
	isRun="是否运行"
	headers="请求头"
	statusCode="状态码"
	# caseID=0
	# des=1
	# url=2
	# method=3
	# data=4
	# expect=5
	#
	# @property
	# def getCaseID(self):
	# 	return self.caseID
	#
	# @property
	# def description(self):
	# 	return self.des
	#
	# @property
	# def getUrl(self):
	# 	return self.url
	#
	# @property
	# def getMethod(self):
	# 	return self.method
	#
	# @property
	# def getData(self):
	# 	return self.data
	#
	# @property
	# def getExpect(self):
	# 	return self.expect

class OperationExcel:
	def getSheet(self):
		book=xlrd.open_workbook(filePath('data','api.xlsx'))
		return book.sheet_by_index(0)

	# @property
	# def getRows(self):
	# 	'''获取总行数'''
	# 	return self.getSheet().nrows
	#
	# @property
	# def getCols(self):
	# 	'''获取总列数'''
	# 	return self.getSheet().ncols
	#
	# def getValue(self,row,col):
	# 	return self.getSheet().cell_value(row,col)
	#
	# def getCaseID(self,row):
	# 	return self.getValue(row=row,col=ExcelVarles().getCaseID)
	#
	# def getUrl(self,row):
	# 	url=self.getValue(row=row, col=ExcelVarles().getUrl)
	# 	if '{bookID}' in url:
	# 		return str(url).replace('{bookID}',readContent())
	# 	else:
	# 		return url
	#
	# def getMethod(self,row):
	# 	return self.getValue(row=row, col=ExcelVarles().getMethod)
	#
	# def getData(self,row):
	# 	return self.getValue(row=row,col=ExcelVarles().getData)
	#
	# def getJson(self,row):
	# 	return self.dictYaml()[self.getData(row=row)]
	#
	# def getExpect(self,row):
	# 	return self.getValue(row=row, col=ExcelVarles().getExpect)

	@property
	def getExcelDatas(self):
		datas=list()
		title=self.getSheet().row_values(0)
		#忽略首行
		for row in range(1,self.getSheet().nrows):
			row_values=self.getSheet().row_values(row)
			datas.append(dict(zip(title,row_values)))
		return datas

	def runs(self):
		'''获取到可执行的测试用例'''
		run_list=[]
		for item in self.getExcelDatas:
			isRun=item[ExcelVarles.isRun]
			if isRun=='y':run_list.append(item)
			else:pass
		return run_list

	def case_lists(self):
		'''获取excel中所有的测试点'''
		cases=list()
		for item in self.getExcelDatas:
			cases.append(item)
		return cases

	def params(self):
		'''对请求参数为空做处理'''
		params_list=[]
		for item in self.runs():
			params=item[ExcelVarles.params]
			if len(str(params).strip())==0:pass
			elif len(str(params).strip())>=0:
				params=json.loads(params)

	def case_prev(self,casePrev):
		'''
		依据前置测试条件找到关联的前置测试用例
		:param casePrev: 前置测试条件
		:return:
		'''
		for item in self.case_lists():
			if casePrev in item.values():
				return item
		return None

	def prevHeaders(self,prevResult):
		'''
		替换被关联测试点的请求头变量的值
		:param prevResult:
		:return:
		'''
		for item in self.runs():
			headers=item[ExcelVarles.headers]
			if '{token}' in headers:
				headers=str(headers).replace('{token}',prevResult)
				return json.loads(headers)

if __name__ == '__main__':
    obj=OperationExcel()
    for item in obj.case_lists():
	    print(item)
