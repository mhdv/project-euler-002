fib=[1,2,2] # 3rd element is 2, because its first even value
while fib[2]<4000000:
	if (fib[0]+fib[1])%2==0:
		fib[2]+=fib[0]+fib[1]
		if fib[0]<fib[1]:
			fib[0]=fib[0]+fib[1]
		else:
			fib[1]=fib[0]+fib[1]
	else:
		if fib[0]<fib[1]:
			fib[0]=fib[0]+fib[1]
		else:
			fib[1]=fib[0]+fib[1]
print(fib[2])