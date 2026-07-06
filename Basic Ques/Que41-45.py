#41 Create a dictionary from two lists.
keys=['A','B','C']
values=[10,20,30]
d = dict(zip(keys,values)) #method 1
#or
#d = {k:v for k,v in zip(keys,values)} #method 2
print(f"keys: {keys}, values: {values}\ndictionary: {d}")

#42 Find the sum of all values in a dictionary.
d={'a':10,'b':20,'c':30}
print("\n", d, "\n")
d_sum = sum(d.values())
print(f"sum of values in the dictionary = {d_sum}")

#43 Update the value of a key.
d={'apple':5,'banana':3}
print(f"before update: {d}")
#Update apple to 10
d['apple'] = 10
print(f"after update: {d}")

#44 Delete a key from a dictionary.
d={'a':1,'b':2,'c':3}
print(f"before delete: {d}")
#Delete key 'b'
del d['b'] #deletes key directly
d.pop('b',None) #handles error if key not present
print(f"after delete: {d}")

#45 Sort a dictionary by keys.
d={'b':2,'c':3,'a':1}
print(f"before sorting: {d}")
d = dict(sorted(d.items()))
print(f"after sorting: {d}")