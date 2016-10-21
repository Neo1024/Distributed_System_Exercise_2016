#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

import pexpect

def sendcat(action, catname, searchnode):
	# 新建一个ssh客户端对象
	myclient = ssh.SSHClient()
	# 设置成默认自动接受密钥
	myclient.set_missing_host_key_policy(ssh.AutoAddPolicy())
	# 连接远程主机
	myclient.connect("shell.cs.helsinki.fi", port=22, username="xgli", password="08358857675Lx")
	# 在远程机执行shell命令
	stdin, stdout, stderr = client.exec_command("ls -l")
	# 读返回结果
	print(stdout.read())
	# 在远程机执行python脚本命令
	stdin, stdout, stderr = client.exec_command("python test.py")

