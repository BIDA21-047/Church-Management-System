import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Load the data from the CSV file
df = pd.read_csv('member_donations.csv')

# Convert 'DateDonated' to datetime format
df['DateDonated'] = pd.to_datetime(df['DateDonated'])

# Calculate the days until the next birthday
today = datetime.now().date()
next_birthdays = df['DateDonated'].apply(lambda x: x.replace(year=today.year))
df['DaysUntilNextBirthday'] = (next_birthdays - pd.Timestamp(today)).dt.days

# Select the feature and target variable for linear regression
X = df['DaysUntilNextBirthday'].values  # Feature (DaysUntilNextBirthday) as numpy array
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

# Plot the data and regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, y, label='Actual Donation Amount')
plt.plot(X, y_pred, color='red', label='Predicted Donation Amount')
plt.xlabel('Days Until Next Birthday')
plt.ylabel('Donation Amount')
plt.title('Predicted Donation Amount based on Days Until Next Birthday')
plt.legend()
plt.grid()
plt.show()
