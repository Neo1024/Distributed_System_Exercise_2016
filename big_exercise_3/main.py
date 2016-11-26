#In main program, three different methods are called to show the threefold model
#First, running first method on 5 different ukko nodes, and make a decision to choose a result from all the returning results
#Second, 

import sys
import second_method
import third_method
from collections import Counter

#the base number used for generating the class_id, which simulates the input data
base_num = sys.argv[1]

if __name__ == "__main__":
	
	# running the first method in 1T/nH/1S model
	results = []
	distinct_res = []
	counts = []

	#remotely running first method on ukko050 - 054 and save the results
	for i in range(50, 55):
		ukkonode = 'xgli@ukko0' + str(i) + '.hpc.cs.helsinki.fi '
		comm = 'ssh ' + ukkonode + 'python3 first_method.py ' 
				+ str(base_num) + ' > id.txt'
		os.system(comm)
		f = open('id.txt', 'r')
		results.append(f.read())

	#a simple decision algorithm: choose the result which appears the most times in results[]
	results_count = Counter(results)
	top = results_count.most_common(1)
	temp = results_count[0]
	result = temp[0]
	print('the class id is: ' + result)

