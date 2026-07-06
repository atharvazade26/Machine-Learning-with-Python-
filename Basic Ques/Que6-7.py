#6 Find the maximum and minimum element 
#        without using max() or min().
nums = [15,3,28,9,11]
max = nums[0]
min = nums[0]
for i in nums:
    if max < i:
        max = i
    elif min > i:
        min = i

print("max = ", max,"min = ", min)

#7 Reverse a list without using reverse().
nums = [1,2,3,4,5]
print("Reverse = ", nums[::-1]) #reversing