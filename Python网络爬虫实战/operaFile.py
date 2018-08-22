#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import os

def operaFile():
	print(u'创建一个名字为test.txt的文件，并在其中写入Hello Python')
	print(u'先得保证test.txt不存在')
	os.system('rm test.txt')
	os.system('ls -l test.txt')
	print(u'现在再来创建文件并写入内容\n')
	fp = open('test.txt', 'w')
	fp.write('Hello Python')
	fp.close()
	print(u'不要忘记用close关闭文件哦')
	print(u'再来看看test.txt是否存在，和内容\n')
	os.system('ls -l test.txt')
	os.system('cat test.txt')
	print('\n')

	print(u'如何避免open文件失败的问题呢？')
	print(u'使用with as就可以了')
	with open('test.txt', 'r') as fp:
		st = fp.read()
	print('test.txt的内容为:%s' %st)

if __name__ == '__main__':
	operaFile()
