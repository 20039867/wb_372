import random

def binsearch(v,L):
	low, high=0, len(L) - 1
	while low <= high:
		mid = (low + high)/2
		if v < L[mid]:
			high= mid -1
		elif v > L[mid]:
			low = mid +1
		else:
			return mid
	return -1

if __name__ == '__main__':
	L= [x for x in xrange(20) if bool(random.randint(0,1))]
	print 'L={}'.format(L)
	print binsearch(7,L)
	print binsearch(31,L)
