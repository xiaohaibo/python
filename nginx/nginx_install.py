#!/usr/bin/env python
#coding:utf-8

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
env.user='root'
env.hosts=['192.168.12.99','192.168.12.163']
env.password = 'haibo123'
@runs_once
def local_task():
    local("uname -a")

#@runs_once
def put_task():
        # run("mkdir /data")
        with cd("/data"):
            with settings(warn_only=True):
                result = put("/hai/nginx/*","/data/")
            if result.failed and not confirm("put file failed, Continue[Y/N]?"):
                abort("Aborting file put task!")

def install_libunwind():
    with cd("/data"):
        run("tar zxvf libunwind-1.2.tar.gz")
        with cd("lib*/"):
            run("CFLAGS=-FPIC ./configure")
            run("make CFLAGS=-FPIC && make CFLAGS=-FPIC install")
            run("yum install pcre")
            run("yum install zlib-devel")

def install_gp():
    with cd("/data"):
        run("tar zxvf google*.gz")
        with cd("google*/"):
            run("./configure")
            run("make && make install")
            run("echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf")
            run("ldconfig")

def install_pcre():
    with cd("/data"):
        run("tar zxvf pcre*.gz")
        with cd("pcre*/"):
            run("./configure")
            run("make && make install")


def install_nginx():
    with cd("/data"):
        run("tar zxvf nginx*.gz")
        with cd("nginx*/"):
            run("./configure --prefix=/usr/local/nginx --with-google_perftools_module --with-http_stub_status_module")
            run("make && make install")
def nginx_conf():
    run("mkdir /tmp/tcmalloc")
    run("chmod 0777 /tmp/tcmalloc")
    run("sed -i '/pid/a\google_perftools_profiles /tmp/tcmalloc; ' /usr/local/nginx/conf/nginx.conf")
    run("ln -s /lib64/libpcre.so.0.0.1 /lib64/libpcre.so.1")

