#Count frequency of each element in a list using a dictionary.
nums=[1,2,2,3,1,2]
dict_nums = {}
for i in nums:
    dict_nums[i] = dict_nums.get(i,0) + 1

print(f"frequency of values in {nums} is \n{dict_nums}")