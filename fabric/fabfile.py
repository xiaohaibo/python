#coding=utf-8
#!/usr/bin/env python

from fabric.api import run
def host_type():	#定义一个任务函数，通过run方法实现远程执行‘uname -s’命令
	run('uname -s')
