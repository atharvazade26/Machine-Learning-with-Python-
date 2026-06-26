def list_to_dictionary(keys, values):
    return dict(zip(keys, values))

list1 = input('Enter keys: ')
list2 = input('Enter values: ')
list_keys = [item.strip() for item in list1.split(" ") if item.strip()]
list_values = [item.strip() for item in list2.split(" ") if item.strip()]
print('Dictionary created: ', list_to_dictionary(list_keys, list_values))   