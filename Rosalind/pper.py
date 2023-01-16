def fac(n):
	f = 1
	for i in range(n):
		f *= (i+1)
	return f

def pper(n, k):
	return fac(n)/fac(n-k) % 1000000

print(pper(91, 9))
