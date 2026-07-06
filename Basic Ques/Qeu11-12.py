nums = [12,45,67,23,89]

#11 Find the second largest element.
nums.sort(reverse = True)
print(f"second largest = {nums[1]}")

#12 Find the second smallest element.
nums.sort()
print(f"second smallest = {nums[1]}")