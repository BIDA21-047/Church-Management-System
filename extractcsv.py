import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "church_management_system.settings")
django.setup()

from user_management.models import Donation

donations = Donation.objects.all()

with open('donations.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "Donation Type", "Amount", "Date Donated"])

    for donation in donations:
        user = donation.user.username if donation.user else ""
        donation_type = donation.donation_type
        amount = donation.amount
        date_donated = donation.date_donated

        writer.writerow([user, donation_type, amount, date_donated])
