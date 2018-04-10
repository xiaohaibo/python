#coding=utf-8
#!/usr/bin/env python
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
#from fabric.contrib.console import confirm
env.user='root'
env.hosts=['172.16.100.7','172.16.100.8']
env.password='haibo123'
@task
@runs_once
def tar_task():		#本地打包任务函数，只限执行一次
	with lcd("/var/log"):
		local("tar -czf message.tar.gz messages")

@task
def put_task():		#上传文件任务函数
	run("mkdir -p /data/logs")
	with cd("/data/logs"):
		with settings(warn_only=True):	#put（上传）出现异常时继续执行，非终止
			result=put("/var/log/message.tar.gz","/data/logs/message.tar.gz")
		if result.failed and not confirm("put file failed, Continue[Y/N]?"):
			abort("Aborting file put task!")	#出现异常时，确认用户是否继续，（Y继续）

@task
def check_task():		#校验文件任务函数
	with settings(warn_only=True):
		#本地local命令需要配置capture=True才能捕获返回值
		lmd5=local("md5sum /var/log/message.tar.gz",capture=True).split(' ')[0]
		rmd5=run("md5sum /data/logs/message.tar.gz").split(' ')[0]
	if lmd5==rmd5:		#对比本地及远程文件md5信息
		print "OK"
	else:
		print "ERROR"
@task
def go():
	tar_task()
	put_task()
	check_task()
