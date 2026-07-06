#Count the number of even and 
#       odd numbers in a list.
nums = [1,2,3,4,5,6,7,8]
even = odd = 0
for i in nums:
    if i%2 == 0:
        print(i, "is even")
        even+=1
    elif i%2 != 0:
        print(i, "is odd")
        odd+=1

print("number of even = ", even)
print("number of odd = ", odd)