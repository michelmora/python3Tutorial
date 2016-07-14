# Dictionary
# A dictionary in Python is a one to one mapping. Every key points to a value, separated by a colon (:).
# A dictionary is defined using curly brackets. The value left of the colon is called the key,
# the value right of the colon is called the value. Every (key,value) pair is separated by a comma.
# Keys must be unique values, you can not use the same key twice. Values may or may not be unique.
k = {'EN': 'English', 'FR': 'French'}
print(k['EN'])
# To modify a value
k['EN'] = 'English-USA'
# To add a new value
k['DE'] = 'German'
print(k)
# To remove a key/value pair use the del keyword
del k['FR']
print(k)

# Iterate over a dictionary
fruitsVegetables = {'apple': 'Canada, USA', 'mango': 'South America, Central', 'potato': 'Mexico, Argentina'}
for key, items in fruitsVegetables.items():
    print('The ' + key + ' is from ' + items)
