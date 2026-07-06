
arr = [int(x) for x in input('Enter array of houses: ').split()]

n = len(arr)

print("Max money robbed = ")
if n == 0:
    print(0)

elif n == 1:
    print(arr[0])

else:
    dp = [0] * n

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], arr[i] + dp[i-2])

    print(dp[-1])