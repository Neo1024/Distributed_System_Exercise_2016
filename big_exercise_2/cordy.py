#Li Xin
#Student number: 014696390
#xin.li@helsinki.fi

import os

def send_cat(action, catname, searchnode):
	#connect to remote ukko node by ssh and run chase_cat.py
	command = 'ssh xgli@' + searchnode + \
			' python3 /cs/home/xgli/Distributed_System_Exercise_2016/big_exercise_2/chase_cat.py' + action + catname
	os.system(command)
	

def check_listy(previouse_lines):
	with open('cmsg', 'r') as f:
		i = 0
        for line in f:
            i = i + 1
            #if new line is written, then return it
            if(i > previouse_lines):
            	return line
    return ''




