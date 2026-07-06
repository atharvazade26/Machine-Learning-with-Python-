#Count the frequency of each element.
nums = [1, 2, 2, 3, 1, 2]
print(f"frequency of values in {nums} is:")
print("value : frequency")
unique = set(nums)

for val in unique:
    print(val, "    :   ", nums.count(val))
