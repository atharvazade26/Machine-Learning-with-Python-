#Remove duplicate elements from a list.
nums = [1,2,2,3,4,4,5]
result = []
print(f"before removing duplicates: {nums}")
for i in nums:
    if i not in result:
        result.append(i)
nums = result
print(f"after removing duplicates:{nums}")