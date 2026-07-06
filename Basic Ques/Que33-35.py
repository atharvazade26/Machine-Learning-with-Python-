marks={'A':80,'B':95,'C':88}
print("dict marks: ", marks)
print()

#33 Find the key with the highest value.
maxValue = max(marks.values())
reqKey = [k for k, v in marks.items() if v == maxValue][0]
print(f"key with the highest value({maxValue}) is {reqKey}")
print()

#34 Find the key with the lowest value.
minValue = min(marks.values())
reqKey = [k for k, v in marks.items() if v==minValue][0]
print(f"key with the lowest value({minValue}) is {reqKey}")
print()

#35 Merge two dictionaries.
d1={'a':1,'b':2}
d2={'c':3,'d':4}

d = d1 | d2 #method 1

#d = d1.copy()
#   d.update(d2) #method 2

#d = {**d1, **d2} #method 3

#for k, v in dict1.items(): #method 4
#    merged[k] = [v]        #Keep duplicate keys & combine values
#for k, v in dict2.items():
#    merged.setdefault(k, []).append(v) 

print(f"dict 1: {d1}, dict 2: {d2}\nmerged dict: {d}")
