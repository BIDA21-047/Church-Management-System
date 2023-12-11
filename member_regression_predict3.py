import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('member_donations.csv')

# Convert 'DateDonated' to datetime format
df['DateDonated'] = pd.to_datetime(df['DateDonated'])

# Extract the month of the year
df['MonthOfDonation'] = df['DateDonated'].dt.month


# Logistic regression function
def logistic_regression(x, y, alpha=0.01, iterations=100):
    m = len(x)
    theta = np.zeros(2)
    x = np.column_stack((np.ones(m), x))

    for _ in range(iterations):
        z = np.dot(x, theta)
        h = 1 / (1 + np.exp(-z))
        gradient = np.dot(x.T, (h - y)) / m
        theta -= alpha * gradient

    return theta


# Prepare the data for logistic regression
X = df['MonthOfDonation'].values
y = (df['Amount'] > 0).astype(int)

# Fit logistic regression
theta = logistic_regression(X, y)

# Generate probability predictions based on the fitted parameters
X_values = np.linspace(1, 12, 100)
X_values = np.column_stack((np.ones(100), X_values))
predicted_probs = 1 / (1 + np.exp(-np.dot(X_values, theta)))

# Specify a date for the vertical line
chosen_date = '2023-02-03'
chosen_date = pd.to_datetime(chosen_date)

# Plot the probability of donation based on the month
plt.figure(figsize=(10, 6))
plt.plot(X_values[:, 1], predicted_probs, color='blue')
plt.xlabel('Months Left of Donation')
plt.ylabel('Probability of Donation')
plt.title('Probability of Member Donating based on Month of Donation')
#plt.axvline(chosen_date.month, color='green', linestyle='--', label='Birthday date')
plt.xticks(np.arange(1, 13), ['-12', '-11', '-10', '-9', '-8', '-7', '-6', '-5', '-4', '-3', '-2', '-1'])
plt.yticks([ 0.6, 0.7, 0.8, 0.9], ['Low of 0.4', 'Moderate of 0.5', 'Good of 0.7', 'High of 0.8+'])
plt.grid()
plt.show()
