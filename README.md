# Pieceful Stress
本负载测试基于[locust](http://locust.io/)的[python3分支](https://github.com/locustio/locust/tree/python3-justiniso)开发。可以单机部署，也可以分布式部署运行。

## 安装依赖包
	pip install -r requirements.txt

## 运行前按需修改“配置文件”和“启动脚本”
### 1. 配置文件
settings.py

	REDIS = 'redis://172.16.131.129:6379/5'

	FAKE_EMAIL_FORMAT = "fake_user_{index}@xxx.com"
	
### 2. 启动脚本
startup.sh

	#! /bin/bash
	#
	locust="/home/debian/lushu/stress/bin/locust"
	work_dir="/home/debian/lushu/stress/src"
	host="http://172.16.131.1:8000"
	web_port="8090"
	logfile="./locust.log"
	
	# 下面三个选项可通过命令行参数覆盖
	mode="standalone"
	master_host="127.0.0.1"
	slave_count=1

## 单机部署方法
	./startup.sh
	
## 分布式部署方法
### 1. 启动 master
	./startup.sh --master
### 2. 启动 slave
    ./startup.sh --slave --master-host=x.x.x.x --slave-count=X
参数说明:

参数          | 含义
------------- | -------------
master-host   | master的主机IP
slave-count   | 本机启动的slave数量，可设为CPU核数

## 程序停止方法
### 1. 在master所在机器执行
	./startup.sh --stop
会停止master及其对应的所有slave
### 2. 在slave所在机器执行
	./startup.sh --stop
只会停止当前机器上的slave

## 发起测试
	# 假如有下面配置：
	master_host=127.0.0.1 
	web_port=8090  
浏览器访问 http://127.0.0.1:8090，设定模拟的用户总数和每秒触发的用户数。
