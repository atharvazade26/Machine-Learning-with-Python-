def fibonacci(n):

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n+1)
    dp[1] = 1

    print(f"Initial DP table: {dp}")
    print("-" * 30)

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

        print(f"Step {i}: Calculating dp[{i}] -> {dp[i - 1]} + {dp[i - 2]} = {dp[i]}")
        print(f"Current DP table state: {dp}\n")

    return dp[n]

n_terms = int(input("Enter the initial number: "))

print(f"Calculating the {n_terms}th Fibonacci number:\n")
result = fibonacci(n_terms)

print("-" * 30)
print(f"The {n_terms}th Fibonacci number is: {result}")