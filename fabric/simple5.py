#!/usr/bin/env python
#coding=utf-8
"""
LNMP的自动化部署
"""
from fabric.colors import *
from fabric.api import *
env.user = 'root'
env.roledefs = {        # 定义业务角色分组
        'webservers': ['172.16.100.7','172.16.100.8'],
        'dbservers': ['172.16.100.9']
}

env.password = 'haibo123'

@roles('webservers')    #webtask任务函数引用'webservers'角色修饰符
def webtask():
        print yellow("install nginx php php-fpm...")
        with settings(warn_only=True):
                run("yum -y install nginx")
                run("yum -y install php-fpm php-mysql php-mbstring php-xml php-mcrypt php-gd")
                run("chkconfig --levels 235 php-fpm on")
                run("chkconfig --levels 235 nginx on")

@roles('dbservers')     #dbtask任务函数引用'dbservers'角色修饰符
def dbtask():   #部署mysql环境
        print yellow("install Mysql....")
        with settings(warn_only=True):
                run("yum -y install mysql mysql-server")
                run("chkconfig --levels 235 mysqld on")

@roles('webservers','dbservers')        # publictask任务函数同时引用两个角色修饰符
def publictask():       #部署公共类环境，如epel、ntp等
        with settings(warn_only=True):
                run("rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm")
                run("yum -y install ntp")

def deploy():
        execute(publictask)
        execute(webtask)
        execute(dbtask)
