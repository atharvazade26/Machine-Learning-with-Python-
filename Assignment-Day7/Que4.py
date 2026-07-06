import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dataset
x = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([2, 5, 10, 17, 26, 37, 50, 65])

# Plot dataset
plt.scatter(x, y, color='blue', label='Data Points')

# Train Linear Regression Model
model = LinearRegression()
model.fit(x, y)

# Predictions
y_pred = model.predict(x)

# Plot regression line
plt.plot(x, y_pred, color='red', label='Regression Line')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression on Non-Linear Data")
plt.legend()
plt.grid(True)
plt.show()

# Metrics
slope = model.coef_[0]
intercept = model.intercept_
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Display results
print("Slope:", round(slope, 4))
print("Intercept:", round(intercept, 4))
print("MSE:", round(mse, 4))
print("R² Score:", round(r2, 4))

# Explanation
print("\nExplanation:")
print("The dataset follows a quadratic pattern (approximately y = x² + 1).")
print("A linear regression model can only fit a straight line.")
print("Therefore, it cannot capture the curved relationship,")
print("resulting in a high MSE and a lower R² score compared to a suitable polynomial model.")