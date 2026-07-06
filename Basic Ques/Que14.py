#Find all duplicate elements.
nums = [1,2,3,2,4,5,1]
dups = []
nums.sort()
for i in range(len(nums)-1):
    if nums[i] == nums[i+1] and nums[i] not in dups:
        dups.append(nums[i])
print(f"duplicate elements: {dups}")

#confusion
seen = set()
dup = []

for num in nums:
    if num in seen and num not in dup:
        dup.append(num)
    seen.add(num)

print(dup)
