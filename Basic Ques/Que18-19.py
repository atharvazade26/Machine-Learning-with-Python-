
nums=[1,2,3,4,5]
print("original list: ", nums)
#18 Rotate a list one position to the right.
rotatedRight = nums[-1:] + nums[:-1]
print(f"right rotated list by 1 position: \n{rotatedRight}")

#19 Rotate a list one position to the left.
rotatedLeft = nums[1:] + nums[:1]
print(f"left rotated list by 1 position: \n{rotatedLeft}")
