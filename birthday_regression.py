import os
import django
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Configure Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'church_management_system.settings')
django.setup()

# Now import the Django models and perform the necessary tasks
from user_management.models import Donation

# Fetching data from the Django Donation model
donations = Donation.objects.all()

# Extracting the date of donations and donation amounts into lists
donation_dates = [donation.date_donated for donation in donations]
donation_amounts = [float(donation.amount) for donation in donations]  # Convert amounts to float

# Create a dictionary with the data
data = {
    'DateDonated': donation_dates,
    'Amount': donation_amounts,
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert 'DateDonated' to datetime
df['DateDonated'] = pd.to_datetime(df['DateDonated'])

# Get today's date
today = datetime.now()

# Calculate days until next donation date
df['DaysUntilDonation'] = (pd.to_datetime(today.strftime('%Y-%m-%d')) - df['DateDonated']).dt.days

# Calculate linear regression without sklearn
x = df['DaysUntilDonation'].astype(float).values  # Convert Series to numpy array
y = df['Amount'].values

# Compute means
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate regression coefficients (slope and intercept)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
beta = numerator / denominator
alpha = y_mean - (beta * x_mean)

# Generate predicted values
y_pred = alpha + beta * x

# Plot the predicted amounts
plt.figure(figsize=(8, 5))
plt.scatter(x, y, label='Actual Donation Amount')
plt.plot(x, y_pred, color='red', label='Predicted Donation Amount')
plt.xlabel('Days Until Donation')
plt.ylabel('Donation Amount')
plt.title('Predicted Donation Amount')
plt.legend()
plt.grid()
plt.show()
