items = [[0,'t',5], [2,"f",3,1.3],[1,'z',2,7]]
a = sorted(items)
print(a)

def second(item):
    return item[1]

b = sorted(items,key=second)
print(b)

c = sorted(items, key=lambda item:item[0])
print(c)