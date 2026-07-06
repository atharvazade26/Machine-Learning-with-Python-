#Find the index of an element in a tuple.
t=(10,20,30,40)
element=30
for i in range(len(t)):
    if t[i] == element:
        print(f"index of {element} in the tupple is {i}")
