# 操作步骤

# 1. 安装 VirtualBox
* https://www.virtualbox.org/wiki/Downloads

# 2. 安装ubuntu20.04.iso
 * http://mirrors.aliyun.com/ubuntu-releases/20.04/
# 3. 安装必要组件
* Vim  
 	* `sudo apt-get install vim` 
* openssh
 	* `sudo apt-get install openssh-server`(网络设置为NAT模式时，要进行端口转发，否则本地无法链接虚拟机)
* Mysql8.0
	* `sudo apt-get install mysql-server `
* Python3 
 	* `sudo apt-get install python3` 
 	* `sudo apt install python3-pip` 
* Git 
 	* `sudo apt-get install git`
* sshkey 
 	* `ssh-keygen -t rsa` 
* pymysql 
 	* `pip3 install pymysql`
* python3-tk
	* `sudo apt-get install python3-tk`  

# 4. 准备工作

* 拷贝 /home/{user}/.ssh/   中的公钥 放到 github中 
* 登录github并新建仓库 py_socket_chat

* 克隆仓库到本地或者ubuntu中（目前是ubuntu中） 
 	* ` git clone git@github.com:hiberoo/py_socket_chat.git ` 

	
# 5. 准备建库语句
` CREATE DATABASE master DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;`

# 6. 准备 建表语句
```
CREATE TABLE `chat_log` (
	id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	user_name VARCHAR(10) NOT NULL DEFAULT "",
	target_name VARCHAR(10) NOT NULL DEFAULT "",
	content VARCHAR(255) NOT NULL DEFAULT "",
	ctime INT(10) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

```
# 7. 本地编码并测试(数据库可直接链接虚拟机中数据库，代码也可将虚拟机中目录通过sftp 映射到本地，这样就不用专门部署代码了)
* 创建本地数据库和数据表
* 创建本地项目py_socket_chat
* 完成 client.py 和 server.py dbhelper  filehelper config.ini 
* 完成测试

# 8. 在ubuntu中部署脚本和数据库

* 将本地文件传到ubuntu中（可直接将虚拟机目录映射到本地直接编写，省去这一步）
 	* ` scp -r py_socket_chat test@{虚拟机ip}:~/Desktop/py_socket_chat `
* 在ubuntu 部署数据库和数据表
* 运行并测试脚本

# 9. 导出镜像（vdi）
* 镜像地址 



	


