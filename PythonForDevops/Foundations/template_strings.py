from string import Template

greeting = Template("$hello Mark Anthony")
print(greeting.substitute(hello="Bonjour"))
print(greeting.substitute(hello="Hi"))