#Second method has 10% possibility to introduce a fault by making class id not fulfill the 
#length restriction which could be detected by the main program. Although the main program 
#doesn't know how the class id is generated, but it does know the class id 
#is a four digit one so it can calculate the length of the id to check whether there is a fault.
#After detecting the fault, main program is supposed to invoke the methed again to correct it. In this sense, 
#we are doing the multi-computation to implement fault tolerance in time dimension (nT/1H/1S)

import random

def first_method(base_num):
	magic_number = 1024

	class_id = base_num % 9 + magic_number

	# 10% possibility introduce a fault that can be detected by the main program
	if (random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) < 2):
		class_id = class_id * 10

	return magic_number