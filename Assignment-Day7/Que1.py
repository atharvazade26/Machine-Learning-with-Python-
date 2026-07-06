# Gradient Descent for f(x) = x^2 + 4x + 1

# Function
def f(x):
    return x**2 + 4*x + 1

# Derivative
def gradient(x):
    return 2*x + 4

# Initial values
x = 5
learning_rate = 0.1
iterations = 5

print("Iteration\t x\t\t Gradient\t New x")

for i in range(1, iterations + 1):
    grad = gradient(x)
    new_x = x - learning_rate * grad

    print(f"{i}\t\t {x:.4f}\t {grad:.4f}\t\t {new_x:.4f}")

    x = new_x

print("\nFinal x =", round(x, 4))
print("Function value =", round(f(x), 4))

# Analytical minimum
x_min = -2
print("Analytical minimum x =", x_min)
print("Minimum function value =", f(x_min))