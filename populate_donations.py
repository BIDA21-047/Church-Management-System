import os
import django
import random
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "church_management_system.settings")
django.setup()

from user_management.models import CustomUser
from user_management.models import Donation

# Get users for whom you want to create donations
users = CustomUser.objects.all()

# Create random donation data for each user
donation_data = []
donation_amounts = []

for _ in range(50):
    for user in users:
        # Check if the user has a valid date of birth
        if user.date_of_birth:
            today = datetime.now()
            user_birthday = user.date_of_birth.replace(year=today.year)

            # Vary donation amount based on the user's birthday and end of the month
            if today.month == user_birthday.month and today.day == user_birthday.day:
                amount = 130  # Extra donation on birthday
            else:
                amount = 30  # Base donation amount

            end_of_month = today.replace(day=28) + timedelta(days=4)
            if today < end_of_month:
                end_of_month = end_of_month - timedelta(days=today.day)
            else:
                end_of_month = end_of_month.replace(month=end_of_month.month + 1, day=1) - timedelta(days=1)

            # Check only the month and day
            if today.month == end_of_month.month and today.day == end_of_month.day:
                amount += 50  # Extra donation at the end of the month

            # Create some randomness to simulate the variations in donations
            amount += round(random.uniform(-5, 5), 2)

            # Generate timestamps for regression model
            date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
            date_stamp = date.timestamp()

            data = {
                'user': user,
                'donation_type': random.choice(['Tithes', 'Other Givings']),
                'amount': amount,
                'date_donated': date,
            }

            donation_data.append(data)
            donation_amounts.append([date_stamp, amount])

# Create donations for each user
for data in donation_data:
    Donation.objects.create(**data)

# Convert donation amounts to DataFrame for regression
df = pd.DataFrame(donation_amounts, columns=['Date_Stamp', 'Amount'])

# Plot donation data
plt.scatter(df['Date_Stamp'], df['Amount'])
plt.title('Donation Amount vs Time/Date')
plt.xlabel('Date')
plt.ylabel('Donation Amount')
plt.show()
