"""Create a dict object using the dict() constructor"""

dict1 = dict()
print(type(dict1))
print(dict1)

dict2 = [['key1','value1'],['key2','value2'],['key3','value3']]
print(dict(dict2))

dict3 = {'key-1':'value-1','key-2':'value-2'}
print(dict3['key-1'])
print(dict3['key-2'])

dict3['key-3'] = 'value-3'

print('key-4' in dict3)

#If the value does not exists, it returns None or the string that you define
print(dict3.get('key3','Value not exist'))

#remove a value from a dict
# del(dict3['key-1'])
# print(dict3)

# Keys() method return a dict_keys object with the dict's keys
print(dict3.keys())
# values() method return a dict_values object
print(dict3.values())
# items() method return a key-value pairs
print(dict3.items())

for key,value in dict3.items():
    print(f'Key: {key} Value: {value}')
