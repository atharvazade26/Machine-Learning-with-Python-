#Check whether a list is sorted.
nums=[1,2,3,4,5]
if nums == sorted(nums):
    print(f"{nums} is alredy sorted")
else:
    print(f"{nums} is not sorted\nSorted: {sorted(nums)}")