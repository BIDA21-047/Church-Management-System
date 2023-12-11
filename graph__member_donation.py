import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('member_donations.csv')

# Convert 'DateDonated' to datetime format
df['DateDonated'] = pd.to_datetime(df['DateDonated'])

# Plot the graph with only markers and no connecting line
plt.figure(figsize=(10, 6))
plt.plot(df['DateDonated'].values, df['Amount'].values, marker='o', linestyle='', label='Donation Amount')
plt.xlabel('Date Donated')
plt.ylabel('Donation Amount')
plt.title('Donation Amount Over Time')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()
plt.tight_layout()
plt.show()
