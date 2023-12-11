from eralchemy import render_er
from IPython.display import Image

# Define the schema for the ERD
schema = """
[USERS]
*id AutoField
username CharField
password CharField
email EmailField
name CharField
surname CharField
date_of_birth DateTimeField
member_category CharField
is_member BooleanField
is_admin BooleanField
is_verified BooleanField
contact_details CharField
is_staff BooleanField

[DONATIONS]
*id AutoField
donation_id AutoField
user_id AutoField > USERS.id
user CharField
DonationType CharField
Amount FloatField
Date_donated DateTimeField

[EVENT]
*id AutoField
event_id AutoField
event_name CharField
event_date CharField
event_location CharField
event_leader CharField
event_description CharField

[EMAIL_MESSAGES]
*id AutoField
sender_email CharField
recipient_email CharField
subject CharField
timestamp DateTimeField
"""

# Create the ERD
erd_path = '/mnt/data/church_management_system_erd.png'
render_er(schema, erd_path)

# Display the ERD
Image(erd_path)