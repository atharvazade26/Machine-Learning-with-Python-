#Count occurrences of an element in a tuple.
t=(1,2,3,2,4,2)
element=2
count = 0
for i in t:
    if i == element:
        count+=1

print(f"element {element} occured {count} times in the tuple")