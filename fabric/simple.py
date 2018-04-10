#coding=utf-8
#!/usr/bin/env python
from fabric.api import *
env.user='root'
env.hosts=['172.16.100.7','172.16.100.8']
env.password='haibo123'
@runs_once	#查看本地系统信息，当有多台主机时只运行一次
def local_task():
	local("uname -a")	#本地任务函数
def remote_task():
	with cd("/tmp"):	#“with”的作用是让后面的表达式的语句继承当前状态，实现
		run("ls -l")		 # “cd /data/logs && ls -l”的效果
