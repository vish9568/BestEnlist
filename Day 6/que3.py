n=int(input("Enter how many numbers:"))
n1,n2=0,1
cnt=0
if n==1:
	print("Fibonacci sequence:")
	print(n1)
else:
	print("Fibonacci sequence:")
	while cnt<n:
		print(n1)
		nth=n1+n2
		n1=n2
		n2=nth
		cnt=cnt+1
