import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset - replace 'total_donations_per_date.csv' with the actual file name or path
df = pd.read_csv('total_donations_per_date.csv')

# Convert 'Date Donated' to datetime format
df['Date Donated'] = pd.to_datetime(df['Date Donated'])

# Extract month from the date and use it as a feature
df['Month'] = df['Date Donated'].dt.month

# Select the feature and target variable for linear regression
X = df[['Month']]  # Feature (Month)
y = df['Amount']  # Target variable

# Add a column of 1s to the features to represent the intercept term
X['Intercept'] = 1

# Convert the data to matrices for easier matrix operations
X = X.to_numpy()
y = y.to_numpy()

# Calculate the coefficients using the normal equation for simple linear regression
coefficients = np.linalg.inv(X.T @ X) @ X.T @ y

# Get the predicted values
y_pred = X @ coefficients

# Calculate R-squared
y_mean = np.mean(y)
SS_total = np.sum((y - y_mean) ** 2)
SS_residual = np.sum((y - y_pred) ** 2)
r_squared = 1 - (SS_residual / SS_total)

# Calculate Adjusted R-squared
n = len(y)
p = X.shape[1] - 1  # Number of predictors (excluding the intercept)
adjusted_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)

# Calculate Mean Squared Error (MSE) and Mean Absolute Error (MAE)
mse = np.mean((y - y_pred) ** 2)
mae = np.mean(np.abs(y - y_pred))

# Display the coefficients
coefficients_dict = {
    'donation_amount / B1 (Coefficient of independent var)': coefficients[0],
    'donation_date / B0 (Y intercept)': coefficients[1]
}
#print("Coefficients:", coefficients_dict)
print("Coefficients:")
for key, value in coefficients_dict.items():
    print(f"{key}: {value}")

# Plot actual vs. predicted values for simple linear regression
plt.scatter(X[:, 0], y)  # Plotting the feature against the target variable
plt.plot(X[:, 0], y_pred, color='red')  # Regression line
plt.xlabel('Month')
plt.ylabel('Donation Amount')
plt.title('Simple Linear Regression: Event Month vs Donation Amount')

# Change x-axis ticks to display rightful months (1 represents January, 12 represents December)
plt.xticks(np.arange(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.show()

# Print R-squared, Adjusted R-squared, MSE, and MAE
print(f"R-squared: {r_squared}")
print(f"Adjusted R-squared: {adjusted_r_squared}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Error (MAE): {mae}")
