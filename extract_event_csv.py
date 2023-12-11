import csv
import os
import django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "church_management_system.settings")
django.setup()

from user_management.models import Donation

# Dates to filter the donations
target_dates = [
    datetime(2023, 1, 16),
    datetime(2023, 2, 20),
    datetime(2023, 4, 8),
    datetime(2023, 9, 13),
    datetime(2023, 11, 1)
]

donations = Donation.objects.filter(date_donated__in=target_dates)

with open('donations_filtered.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "Donation Type", "Amount", "Date Donated"])

    for donation in donations:
        user = donation.user.username if donation.user else ""
        donation_type = donation.donation_type
        amount = donation.amount
        date_donated = donation.date_donated

        writer.writerow([user, donation_type, amount, date_donated])
