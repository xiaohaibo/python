#coding=utf-8
#!/usr/bin/env python
from fabric.api import *
env.user='root'
env.hosts=['172.16.100.7','172.16.100.8']
env.password='haibo123'
@runs_once	#主机遍历过程中，只有第一台触发此函数
def input_raw():
	return prompt("please input directory name:", default="/home")
def worktask(dirname):
	run("ls -l "+dirname)
@task	#限定只有go函数对fab命令可见
def go():
	getdirname = input_raw()
	worktask(getdirname)
