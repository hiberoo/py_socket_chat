# py_socket_chat


安装 vmware 
下载ubuntu.iso ubuntu-releases-16.04安装包下载_开源镜像站-阿里云 (aliyun.com)
安装ubuntu.iso
安装必要组件
	Ssh               apt-get install ssh-server
	Mysql5.7    apt-get install mysql
	Python3      apt-get install python3
	Vim              apt-get install vim
	Git                apt-get install git
在ubuntu中安装sshkey    ssh-keygen -t rsa 
拷贝 /home/user/.ssh/   中的公钥 放到 github中 
登录github并新建仓库 py_socket_chat
克隆仓库到本地或者ubuntu中（目前是ubuntu中）  git clone git@github.com:hiberoo/py_socket_chat.git
创建项目py_socket_chat
安装python3  apt install python3-pip
安装pymysql  pip3  install pymysql (sudo pip3 install pymysql==0.10.1 由于服务器的python是3.5版本，pymysqsl 版本要更换)
安装TK   apt-get install python3-tk (pip3 install 找不到包 环境：ubuntu16.04)
	需要多安装一个 apt install tk-dev（ubuntu）
	
创建数据库
CREATE DATABASE master DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

准备 建表语句
CREATE TABLE `chat_log` (
	id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	user_name VARCHAR(10) NOT NULL DEFAULT "",
	target_name VARCHAR(10) NOT NULL DEFAULT "",
	content VARCHAR(255) NOT NULL DEFAULT "",
	ctime INT(10) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

本地编写并测试通过 client.py 和 server.py dbhelper  filehelper config.ini 源码文件和配置文件
将本地文件传到ubuntu中
scp -r chat test@192.168.232.128:~/Desktop/test (将本地chat目录里所有文件 复制到 远程服务器的用户目录的/Desktop/test 里面)
在ubuntu中（或ssh登录到ubuntu中）将源码和配置加入本地仓库并push到远端（github）
完善README(就是本篇)
导出虚拟机

测试步骤：
	运行聊天脚本
		ubuntu新建terminal   
		 cd ~/Desktop/py_socket_chat/ 
		Python3 server.py
		再次新建terminal
		cd ~/Desktop/py_socket_chat/ 
		Python3 client.py 
		互发消息
		日志文件会生成在当前目录下  比如名为 “2022_6_12” 的文本文件
	查看消息记录
	           新建terminal
		 cd ~/Desktop/py_socket_chat/ 
		Python3 ListChat.py
	   
流程待优化。。。

![image](https://user-images.githubusercontent.com/12488600/173242814-80cca27e-8918-44ea-b6b5-ef4b22c93aba.png)
