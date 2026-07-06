#Remove duplicate elements from a list.
nums = [1,2,2,3,4,4,5]
print(f"before removing duplicates: {nums}")
nums = list(set(nums))
print(f"after removing duplicates:{nums}")