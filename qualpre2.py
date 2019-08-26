T=int(raw_input())
for f in range(T):
	N,K= [int(x) for x in raw_input().split()]
	S= [int(x) for x in raw_input().split()]
	z=0
	S.sort(reverse=True)
	for i in range (len(S)):
		if(S[i]>=S[K-1]):
			z=z+1
	print(z)


