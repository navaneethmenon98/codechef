def sub(a,b):
	for i in range(len(a)):
		a[i]=b[i]-a[i]
def mini(a):
	x = 9999999
	for i in range(len(a)-1):
    		if (a[i] < x and a[i]!=0):
        		x = a[i]
			s = i
	return  s
T=int(raw_input())
for f in range(T):
	t=0
	N= int(raw_input())
	A=map(int, raw_input().split())
	B=map(int,raw_input().split())
	sub(A,B)
	try:
		for i in range(N-3):
			j=i
			if(A[i]<0):
				break
			i=mini(A)
			A[i]=A[i]-1
			A[i+1]=A[i+1]-2
			A[i+2]=A[i+2]-3			
			i=j
		for k in range(N-1):
			if(A[k]==0):
				t=1
			else:
				t=0
		if(t==1):
			print("TAK")
		else:
			print("NIE")

	except:
		print("NIE")
