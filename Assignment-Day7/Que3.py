import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dataset
x = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([2.2, 3.9, 6.1, 8.0, 10.2, 12.1, 14.3, 15.8])

# Create and train model
model = LinearRegression()
model.fit(x, y)

# Predictions
y_pred = model.predict(x)

# Metrics``
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

# Print results
print("Scikit-Learn Linear Regression")
print("------------------------------")
print(f"Slope (Coefficient): {model.coef_[0]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R² Score: {r2:.4f}")

# Predict y when x = 10
prediction = model.predict([[10]])
print(f"\nPredicted y when x = 10: {prediction[0]:.4f}")

# Plot
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression using Scikit-Learn")
plt.legend()
plt.grid(True)
plt.show()