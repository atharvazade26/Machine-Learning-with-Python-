import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Dataset
x = np.array([-3,-2,-1,0,1,2,3]).reshape(-1,1)
y = np.array([-20,-3,0,1,2,11,34])

degrees = [1,2,3]

print("Degree\tMSE\t\tRMSE\t\tR²")

best_degree = None
best_r2 = -1

for d in degrees:

    poly = PolynomialFeatures(degree=d)
    x_poly = poly.fit_transform(x)

    model = LinearRegression()
    model.fit(x_poly, y)

    y_pred = model.predict(x_poly)

    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y, y_pred)

    print(f"{d}\t{mse:.4f}\t\t{rmse:.4f}\t\t{r2:.4f}")

    if r2 > best_r2:
        best_r2 = r2
        best_degree = d

print("\nBest Degree:", best_degree)

print("\nExplanation")
print("Underfitting : Model is too simple and cannot capture the data pattern.")
print("Good Fit     : Model captures the pattern without unnecessary complexity.")
print("Overfitting  : Model becomes too complex and may fit noise instead of the true relationship.")