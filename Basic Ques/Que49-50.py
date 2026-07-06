#49 Check whether one set is a subset of another.
A={1,2}
B={1,2,3,4}
print(f"A: {A}, B:{B}\n")
Asubset = all(i in B for i in A)
Bsubset = all(i in A for i in B)
print("A is subset of B:", Asubset)
print("B is subset of A:", Bsubset)
#OR
#print("A is subset of B: ", A.issubset(B))
#print("B is subset of A: ", B.issubset(A))

#50 Remove duplicate elements 
#   from a list using a set.
nums=[10,20,20,30,30,40]
print("original: ", nums)
nums=list(set(nums))
print("duplicates removed: ", nums)