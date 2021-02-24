a = list(range(10))
print(a)

b = list("Pablo Fajardo")
print(b)

empty = []
print(empty)

nine = [0,1,2,3,4,5,6,7,8,9]
print(nine)

mixed = ['a',1,'b',2,'c',3,"Pablo",empty,True]
print(mixed)

#Add  a single item to a list
mixed.append("Fajardo")
print(mixed)

#Add item with index
mixed.insert(2,"PALABRA")
print(mixed)

#New List
pies = ['cherry','cream','apple']
print(pies)

#Another List
desserts = ['cookies','lemon']
print(desserts)

#Add a list with another list
pies.extend(desserts)
print(pies)

#Remove a item with the index
pies.pop(2)
print(pies)

#Remove the last item
#pies.pop()
#print(pies)

pies.remove('lemon')
print(pies)

pies.remove('cookies')
print(pies)

