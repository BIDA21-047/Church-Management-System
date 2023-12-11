import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
#df = pd.read_csv('member_donations.csv') #Jason's Donations Data
df = pd.read_csv('member_donations2.csv') #Sofia Donations Data
 
# Convert 'DateDonated' to datetime format
df['DateDonated'] = pd.to_datetime(df['DateDonated'])

# Extract the month of the year
df['MonthOfDonation'] = df['DateDonated'].dt.month

# Select the feature and target variable for linear regression
X = df['MonthOfDonation'].values  # Feature (MonthOfDonation) as numpy array
y = df['Amount'].values  # Target variable as numpy array

# Calculate the means for X and y
x_mean = np.mean(X)
y_mean = np.mean(y)

# Calculate regression coefficients (slope and intercept) manually
numerator = ((X - x_mean) * (y - y_mean)).sum()
denominator = ((X - x_mean) ** 2).sum()
beta = numerator / denominator
alpha = y_mean - (beta * x_mean)

# Generate predicted values
y_pred = alpha + beta * X

# Specify a date for the vertical line
chosen_date = '2023-06-11'
chosen_date = pd.to_datetime(chosen_date)

# Plot the data and regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, y, label='Actual Donation Amount')
plt.plot(X, y_pred, color='red', label='Predicted Donation Amount')
plt.xlabel('Month of Donation')
plt.ylabel('Donation Amount')
plt.title('Predicted Donation Amount based on Month of Donation')
plt.legend()

# Vertical line on the chosen date
plt.axvline(chosen_date.month, color='green', linestyle='--', label='Birthday date')
plt.xticks(np.arange(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.grid()
plt.show()
