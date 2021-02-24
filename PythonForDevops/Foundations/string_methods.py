my_list = list()
print(str(list))

input_phrase = "      Hello World "
a = input_phrase.strip()
b = input_phrase.rstrip()
c = input_phrase.lstrip()
print(a)
print(b)
print(c)

output = 'Pablo'
d = output.ljust(10)
e = output.rjust(12,'x')
print(d)
print(e)

text = "Marry had a little lamb"
print(text.split())

url = "gt.motomomo.io/v2/api/asset/143"
print(url.split('/'))

items = ['banana','apple','grape','strawberry']
print(" and ".join(items))
