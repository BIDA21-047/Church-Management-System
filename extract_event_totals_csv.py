import csv
import os
import django
from datetime import datetime
from collections import defaultdict
from decimal import Decimal

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

# Calculate total amounts for each date
totals = defaultdict(Decimal)

for donation in donations:
    totals[donation.date_donated] += donation.amount

# Write the total amounts for each date to a CSV file
with open('total_donation_per_date.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Total Amount Donated"])

    for date, total_amount in totals.items():
        writer.writerow([date, total_amount])
