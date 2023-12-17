# standard way to create a dictionary
dicionario = {}

# create a dict using prototype
my_dict = dict()

# examples
my_new_dict = {'nome': 'Abc', 'idade':26, 'altura':1.77}

print(my_new_dict)
print(my_new_dict['idade'])

# methods for dictionaries
my_new_dict['programmer'] = True
print(my_new_dict)

# overwrite items
my_new_dict['altura'] = 245
print(my_new_dict)

# loops for dictionaries
for i in my_new_dict:
    print(i, my_new_dict[i])

#just testing a new detail.
print("i'm using it from the web")