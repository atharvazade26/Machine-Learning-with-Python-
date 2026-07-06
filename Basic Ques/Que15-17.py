#15 Merge two lists.
list1=[1,2,3]
list2=[4,5,6]
mergedList = list1 + list2
print(f"list1: {list1}\nlist2: {list2}\nmerged list: {mergedList}\n")

#16 Find common elements between two lists.
list1=[1,2,3,4]
list2=[3,4,5,6]
common = list(set(list1) & set(list2))
print(f"list1: {list1}\nlist2: {list2}\ncommon elements: {common}\n")

#17 Find elements present in first list but not second.
list1=[1,2,3,4]
list2=[3,4,5,6]
reqList = list(set(list1) - set(list2))
print(f"list1: {list1}\nlist2: {list2}\nelements in 1 but not in 2: {reqList}\n")
