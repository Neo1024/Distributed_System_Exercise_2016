
#In main program, three different methods are called to show the threefold model
#The service designed in this program is to generate a four_digit class id based on an input integer
#Both the first method and second method could generate the class id, however there's possibility 
#that a fault could hanppen and results in the wrong class_id, which could be detected and solved
#in threefold dimension model

import sys
import second_method
import third_method
from collections import Counter
import os

#the input base number used for generating the class_id, which simulates the input data
base_num = sys.argv[1]

if __name__ == "__main__":
	############# First Method #############
	
	# running the first method in 1T/nH/1S model
	results = []

	#remotely running first method on ukko050 - 054 and save the results
	for i in range(92, 94):
		ukkonode = 'xgli@ukko0' + str(i) + '.hpc.cs.helsinki.fi '
		comm = 'ssh ' + ukkonode + 'python3 /cs/home/xgli/Distributed_System_Exercise_2016/big_exercise_3/first_method.py ' \
			+ str(base_num) + ' > id.txt'
		os.system(comm)
		f = open('id.txt', 'r')
		lines = f.read().split('\n')
		temp = lines[0].split()
		r = temp[0]
		results.append(r)
	print(results)

	#a simple decision algorithm: choose the result which appears the most times in results[]
	results_count = Counter(results)
	top = results_count.most_common(1)
	temp = results_count[0]
	print(results_count)
	print(top)
	print(temp)
	result_1 = temp[0]
	print('the class id is: ' + result_1)

	########################################

	############# Second Method ############
	result_2 = second_method.second_method(base_num)

	#detect whether there's an error by checking the length of class_id
	#if not call the method again
	while (len(str(result_2)) != 4):
		result_2 = second_method.second_method(base_num)
		print("An error has been detected!")
	print('The class id is: ' + str(result_2))

	########################################


	############# Third Method ############
	#simulate an error
	third_method.third_method(base_num)		
	########################################
