import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Dataset
x = np.array([-4,-3,-2,-1,0,1,2,3,4]).reshape(-1,1)
y = np.array([13,6,1,-2,-3,-2,1,6,13])

# ---------------- Linear Regression ----------------
linear = LinearRegression()
linear.fit(x, y)
y_linear = linear.predict(x)

# ---------------- Polynomial Regression (Degree 2) ----------------
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

poly_model = LinearRegression()
poly_model.fit(x_poly, y)
y_poly = poly_model.predict(x_poly)

# ---------------- Metrics ----------------
mse_linear = mean_squared_error(y, y_linear)
rmse_linear = np.sqrt(mse_linear)
r2_linear = r2_score(y, y_linear)

mse_poly = mean_squared_error(y, y_poly)
rmse_poly = np.sqrt(mse_poly)
r2_poly = r2_score(y, y_poly)

# ---------------- Print Results ----------------
print("Linear Regression")
print("MSE :", round(mse_linear,4))
print("RMSE:", round(rmse_linear,4))
print("R²  :", round(r2_linear,4))

print("\nPolynomial Regression (Degree 2)")
print("MSE :", round(mse_poly,4))
print("RMSE:", round(rmse_poly,4))
print("R²  :", round(r2_poly,4))

print("\nBetter Model:")
print("Polynomial Regression performs better because the dataset follows a quadratic curve.")

# ---------------- Plot ----------------
plt.scatter(x, y, color="blue", label="Data")

plt.plot(x, y_linear, color="red", label="Linear Regression")
plt.plot(x, y_poly, color="green", label="Polynomial Regression")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.grid(True)
plt.show()