from collections.abc import Hashable

# the object_list has already been defined
# write your code here
# object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
hash_values = {}
number = 0
for hash_object in object_list:
    if isinstance(hash_object, Hashable):
        hash_value = hash_object.__hash__()
        if hash_value in hash_values.keys():
            hash_values[hash_value] = hash_values[hash_value] + 1
        else:
            hash_values[hash_value] = 1
for count in hash_values.values():
    if count > 1:
        number += count
print(number)