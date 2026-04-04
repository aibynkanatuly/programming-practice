# dates.py

from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Current date and time:", now)

# Create specific date
specific_date = datetime(2024, 1, 1)
print("Specific date:", specific_date)

# Date formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted)

# Time difference
future = now + timedelta(days=10)
difference = future - now
print("Difference in days:", difference.days)