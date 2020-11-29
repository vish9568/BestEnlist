import my_module

length = len(my_module.a)
for i in range(length):
	my_module.a[i]=my_module.a[i]+2
print(my_module.a)