s=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
print("total no. is",len(s))

a=[]
for i in range(len(s)-1):
	for j in range(len(s)-1):
		if((s[i]*s[j])<200 and s[i]!=s[j]):
			a.append(s[i]*s[j])
a.sort()
print(a)
print("length is", len(a))
b=[]
for k in range(len(a)-1):
	if(a[k] not in b):
		b.append(a[k])
print(b)
print("length is",len(b)) 









