student={'name':'Rahul','age':20}
print(student, "\n")
#36 Check whether a key exists.
key = 'age'
if key in student.keys():
    print(f"key '{key}' is present in dictionary")
else:
    print(f"key '{key}' not found in dictionary")

#37 Check whether a value exists.
value = 20
if value in student.values():
    print(f"value '{value}' is present in dictionary")
else:
    print(f"value '{value}' not found in dictionary")

d={'a':1,'b':2,'c':3}
print("\n", d, "\n")

#38 Print all keys of a dictionary.
print(d.keys())
#39 Print all values of a dictionary.
print(d.values())

#40 Swap keys and values.
swapped = {v: k for k, v in d.items()}
print(f"swapped dictionary: {swapped}")