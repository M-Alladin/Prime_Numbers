#######################Brute Force Prime Number##########################
#by esta and muttaqi
#
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
def BruteForce(Number,mode,step):
	a = time.time()
	for i in range(1, Number,step):
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
	BruteForce(1000,i,1)
	# BruteForce(21,i,2)


