import os
import django
import pandas as pd

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'church_management_system.settings')  # Replace 'your_project_name' with your actual project name
django.setup()

# Import the Django models
from user_management.models import CustomUser, Donation

# Get the user 'jason'
jason_user = CustomUser.objects.get(username='jason')

# Get all donations related to the user 'jason'
jason_donations = Donation.objects.filter(user=jason_user)

# Create a list to store donation details
data = []

# Iterate through each donation and append it to the data list
for donation in jason_donations:
    data.append({
        'DateDonated': donation.date_donated,
        'Amount': float(donation.amount)  # Convert Decimal to float
    })

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Write the data to a CSV file
df.to_csv('member_donations2.csv', index=False)
