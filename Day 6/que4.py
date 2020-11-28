def arms(n):
	order=len(n)
	n=int(n)
	temp=n
	sum=0
	while temp>0:
		digit=temp%10
		sum+=digit**order
		temp=temp//10
	if n==sum:
		print("Number is Armstrong")
	else:
		print("Not an Armstrong")

n=input("Enter a Number:")
arms(n)