# py_socket_chat



# 安装 VirtualBox
## 下载ubuntu.iso ubuntu-releases-20.04 地址：http://mirrors.aliyun.com/ubuntu-releases/20.04/
# 安装ubuntu20.04.iso

## 安装必要组件

* ssh

 * ` apt-get install ssh-server`

* Mysql5.7
 * ` apt-get install mysql `

* Python3 
 * ` apt-get install python3` 
 * ` apt install python3-pip` 

* Vim  
 * ` apt-get install vim` 
* Git 
 * ` apt-get install git`
* sshkey 
 * ` ssh-keygen -t rsa` 

# 操作步骤

* 拷贝 /home/{user}/.ssh/   中的公钥 放到 github中 
* 登录github并新建仓库 py_socket_chat

* 克隆仓库到本地或者ubuntu中（目前是ubuntu中） 
 * git clone git@github.com:hiberoo/py_socket_chat.git 

	
# 准备建库语句
` CREATE DATABASE master DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;`

# 准备 建表语句
```
CREATE TABLE `chat_log` (
	id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	user_name VARCHAR(10) NOT NULL DEFAULT "",
	target_name VARCHAR(10) NOT NULL DEFAULT "",
	content VARCHAR(255) NOT NULL DEFAULT "",
	ctime INT(10) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

```
# 编码
* 创建本地数据库和数据表
* 创建本地项目py_socket_chat
* 完成 client.py 和 server.py dbhelper  filehelper config.ini 
* 完成测试

# 在ubuntu中部署脚本和数据库

* 将本地文件传到ubuntu中
 * ` scp -r py_socket_chat test@{虚拟机ip}:~/Desktop/py_socket_chat `
* 在ubuntu 部署数据库和数据表
* 运行并测试脚本

# 导出镜像（vdi）
* 镜像地址 

# github地址
* https://github.com/hiberoo/py_socket_chat


	


