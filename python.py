t=int(input())
for _ in range(t):
	n=int(input())
	l=[int(i) for i in input().split()]
	i,j=0,len(l)-1
	while i<=j:
		l[i],l[j]=l[j],l[i]
		i+=1
		j-=1
	print("Reversed list is : ",*l)

