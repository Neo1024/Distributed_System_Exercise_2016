#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

import pexpect
from pexpect import pxssh

def sendcat(action, catname, searchnode):
	s = pxssh.pxssh()
	s.login('ukko010.hpc.cs.helsinki.fi', 'xgli')
	s.sendline('ls -l')
	s.prompt()
	print('hahah')

sendcat(1, 2, 3)


