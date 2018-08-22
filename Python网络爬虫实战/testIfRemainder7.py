#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'


def isEvenNum(num):
	if num%7 == 0:
		print(u"%d 可以被7整除" %num)
	else:
		print(u"%d 不可被7整除" %num)

if __name__ == '__main__':
	numStr = raw_input("请输入一个整数：")
	try:
		num = int(numStr)
	except ValueError:
		print(u"输入错误，要求输入一个整数")
		exit()
	
	isEvenNum(num)
