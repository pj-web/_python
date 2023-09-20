# cat = {
#     'name': 'Murzic',
#     'age': 5,
#     'color': 'black',
#     'weight': 4.5,
# }
#
# keys = cat.keys()
# values = cat.values()
# items = cat.items()
#
# name = cat['name']
# age = cat.get('age')
#
# for data in cat:
#     print(data)

nested_dict = {
    'one': {'a': 1, 'b': 2},
    'two': {'c': 3, 'd': 4},
    'three': {'e': 5, 'f': 6},
}

for key in nested_dict.keys():
    for nested_key in nested_dict[key].keys():
        print(key, nested_key)

