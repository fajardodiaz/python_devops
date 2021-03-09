print("%s + %s = %s" % (1,2,3))

#Format arguments include the conversation specifier.
print("%.3f"%1.123999999)


"""
Format method, template strings, and f-strings
"""

#Format method
print("My name is {} and I'm {} years old. I'm from {}".format("Pablo Fajardo","21","Guatemala "))
print("My name is {2} and I'm {0} years old. I live in {1}".format("21","Panama","Pablo Fajardo"))
print("My name is {name} and I'm {age} years old. I want to live in {city}".format(name="Pablo Fajardo",age="21",city="England"))

#Dict works to suply the key value for name-based replacement fields
values = {'name':'Pablo','lastname':'Fajardo'}
print("Welcome to my house {name} {lastname}".format(**values))

#Format specifications arguments
text = "|{0:>22}||{0:<22}|"
print(text.format('O','O'))

text = "|{0:<>22}||{0:><22}|"
print(text.format('O','O'))