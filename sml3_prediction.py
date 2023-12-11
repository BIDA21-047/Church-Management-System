import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset - replace 'total_donations_per_date.csv' with the actual file name or path
df = pd.read_csv('total_donations_per_date.csv')

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract month from the date and use it as a feature
df['Month'] = df['Date'].dt.month

# Select the feature and target variable for linear regression
X = df[['Month']]  # Feature (Month)
y = df['Total Amount Donated']  # Target variable

# Add a column of 1s to the features to represent the intercept term
X['Intercept'] = 1

# Convert the data to matrices for easier matrix operations
X = X.to_numpy()
y = y.to_numpy()

# Calculate the coefficients using the normal equation for simple linear regression
coefficients = np.linalg.inv(X.T @ X) @ X.T @ y

# Get the predicted values
y_pred = X @ coefficients

# Extend X values for future predictions (next 12 months)
future_months = np.arange(13, 25).reshape(-1, 1)  # Creating the next 12 months (13 to 24)
future_X = np.hstack((future_months, np.ones((12, 1))))  # Adding Intercept column

# Predict future values
future_predictions = future_X @ coefficients

# Plot actual vs. predicted values for simple linear regression including future predictions
plt.scatter(X[:, 0], y, label='Actual')  # Plotting the existing data
plt.plot(X[:, 0], y_pred, color='red', label='Line of Best Fit')  # Regression line for known data
plt.plot(np.hstack((X[:, 0], future_X[:, 0])), np.hstack((y_pred, future_predictions)), color='green', label='Extended Line of Best Fit')  # Extended regression line
plt.xlabel('Month')
plt.ylabel('Total Donation Amount')
plt.title('Linear Regression: Past and Future Total Donation Amount')
plt.legend()

plt.xticks(np.arange(1, 25), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec','Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])


plt.show()

# Calculate R-squared for the known data
y_mean = np.mean(y)
SS_total = np.sum((y - y_mean) ** 2)
SS_residual = np.sum((y - y_pred) ** 2)
r_squared = 1 - (SS_residual / SS_total)

print("Coefficients:", coefficients)  # Display the coefficients
print(f"R-squared: {r_squared}")  # Print R-squared for the known data
