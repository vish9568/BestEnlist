def merge(dict1,dict2):
	return (dict1.update(dict2))

dict1={56:'Vishal',57:'Amisha',28:'Akash'}
dict2={25:'Revati',11:'Sanket'}

print(merge(dict1,dict2))

print(dict1)
