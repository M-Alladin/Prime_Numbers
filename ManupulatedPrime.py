#######################Brute Force Prime Number##########################
# by esta and muttaqi
# excluding even numbers by taking step 2
#########################################################################

import time
import sys
# print(sys.argv[1])
MODE = ['full', 'half', 'root']
def Condition(i,mode):
	if mode == 0:
		return i
	elif mode == 1:
		return int(i/2)+1
	elif mode == 2:
		return int(i**0.5)+1
def BruteForce(Number,mode):

	a = time.time()
	print('Prime Found :',2)
	for i in range(3, Number,2):
		NotPrime = False
		# print(i,'Condition: ',Condition(i,mode))
		for j in range(2,Condition(i,mode)):
			# print(i,j)
			if i%j ==0:
				NotPrime = True
				break
		if NotPrime != True:
			pass
			# print('Prime Found :',i)
		b = time.time()
		# print("time ",b-a)
	timeNow = time.time() -a
	print(MODE[mode]+': ',timeNow)
	return timeNow

for i in range(3):
	BruteForce(1000,i)
	# BruteForce(21,i,2)

