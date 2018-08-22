#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import cls
import time

def getList():
	#构建一个纯数字列表
	numList = []
	num = 'q'
	while num:
		cls.clear()
		print numList
		print(u'结束构建列表，请按回车')
		num = raw_input('请输入一个整数：')
		if num == '':
			break
		try:
			num = int(num)
		except ValueError:
			print(u'要求输入整数，请重新输入')
			time.sleep(1)
			continue
		numList.append(num)
	return numList

def getMaxNum(List):
	#获取列表中最大值
	#import pdb
	#pdb.set_trace()
	num = List[0]
	for i in List[1:]:
		if num <= i:
			num = i
	return num

def getMinNum(List):
	#获取列表中最小值
	num = List[0]
	for i in List[1:]:
		if num >= i:
			num = i
	return num


if __name__ == '__main__':
	numList = getList()
	maxNum = getMaxNum(numList)
	print(u'列表中最大值为:%d' %maxNum)
	minNum = getMinNum(numList)
	print(u'列表中最小值为:%d' %minNum)
