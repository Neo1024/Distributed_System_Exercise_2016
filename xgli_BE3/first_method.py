
#first method has 10% introduce an fault, which remains latent until doing multi-computation 
#on different ukko nodes and use a decision algorithm to choose a result from the returning results. 
#This situation is designed to simulate the possible fault caused by hardware failures, which could be solved by 
#doing multi-computation in hardware dimension simultaneously (1T/nH/1S) 

#the correct way to generate an class id based on the input number like this: base_num % 9 + magic_number, which generates 
#a four digit class id. The rule of generating class id here is very simple because it's just in need for 
#the illustration the threefold model

import random
import sys

base_num = sys.argv[1]

def first_method(base_num):
	magic_number = 1024

	#correct class_id
	class_id = int(base_num) % 9 + magic_number

	# 10% possibility introduce a latent fault
	if (random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) < 2):
		class_id = class_id + 1000

	print(class_id)

if __name__ == "__main__":
	first_method(base_num)