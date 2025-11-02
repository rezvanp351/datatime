"""
datetime_examples.py
---------------------

This file contains all examples and explanations from the W3Schools "Python Datetime" tutorial.
Each example is numbered and explained in English for clarity and Git repository documentation.
"""

import datetime


# =====================================================
# Example 1: Get the current date and time
# -----------------------------------------------------
# Explanation:
# The datetime module allows you to get the current date
# and time using the now() method.
# =====================================================
def example_1_current_datetime():
    x = datetime.datetime.now()
    print("1️⃣ Example 1 - Current date & time:", x)


# =====================================================
# Example 2: Get only the current date
# -----------------------------------------------------
# Explanation:
# The date.today() method returns only the current date
# (without time information).
# =====================================================
def example_2_today_date():
    x = datetime.date.today()
    print("2️⃣ Example 2 - Today's date:", x)


# =====================================================
# Example 3: Access parts of a datetime object
# -----------------------------------------------------
# Explanation:
# You can extract parts such as year, month, day, hour,
# minute, and second from a datetime object.
# =====================================================
def example_3_date_parts():
    x = datetime.datetime.now()
    print("3️⃣ Example 3 - Year:", x.year)
    print("Month:", x.month)
    print("Day:", x.day)
    print("Hour:", x.hour)
    print("Minute:", x.minute)
    print("Second:", x.second)


# =====================================================
# Example 4: Create a specific datetime object
# -----------------------------------------------------
# Explanation:
# You can create a datetime object by specifying year,
# month, day, and optionally hour and minute.
# =====================================================
def example_4_create_datetime():
    x = datetime.datetime(2020, 5, 17, 10, 30)
    print("4️⃣ Example 4 - Created datetime object:", x)


# =====================================================
# Example 5: Display the weekday name using strftime()
# -----------------------------------------------------
# Explanation:
# The strftime() method formats a datetime object into
# a readable string. Here, we display the weekday name.
# =====================================================
def example_5_day_name():
    x = datetime.datetime.now()
    print("5️⃣ Example 5 - Weekday name:", x.strftime("%A"))


# =====================================================
# Example 6: Format datetime using strftime()
# -----------------------------------------------------
# Explanation:
# The strftime() method allows custom date/time formatting
# using various format codes.
# =====================================================
def example_6_custom_format():
    x = datetime.datetime(2024, 3, 21, 15, 45, 30)
    formatted = x.strftime("%Y-%m-%d %H:%M:%S")
    print("6️⃣ Example 6 - Custom formatted date:", formatted)


# =====================================================
# Example 7: Date format codes demonstration
# -----------------------------------------------------
# Explanation:
# Common strftime format codes and their meanings are shown here.
# =====================================================
def example_7_format_codes():
    x = datetime.datetime(2023, 11, 2, 14, 30, 45)
    print("7️⃣ Example 7 - Format codes demonstration:")
    print("%a  ➜", x.strftime("%a"), "(Abbreviated weekday name)")
    print("%A  ➜", x.strftime("%A"), "(Full weekday name)")
    print("%d  ➜", x.strftime("%d"), "(Day of month)")
    print("%B  ➜", x.strftime("%B"), "(Full month name)")
    print("%Y  ➜", x.strftime("%Y"), "(Full year)")
    print("%I %p ➜", x.strftime("%I %p"), "(12-hour clock with AM/PM)")
    print("%H:%M:%S ➜", x.strftime("%H:%M:%S"), "(24-hour clock)")


# =====================================================
# Example 8: Difference between two dates (timedelta)
# -----------------------------------------------------
# Explanation:
# The timedelta class allows you to find the difference
# between two dates or datetimes.
# =====================================================
def example_8_timedelta():
    date1 = datetime.datetime(2024, 5, 10)
    date2 = datetime.datetime(2024, 5, 15)
    delta = date2 - date1
    print("8️⃣ Example 8 - Difference between two dates:", delta.days, "days")


# =====================================================
# Example 9: Add or subtract time using timedelta
# -----------------------------------------------------
# Explanation:
# You can add or subtract a specific time period (days,
# hours, etc.) from a datetime object using timedelta.
# =====================================================
def example_9_add_subtract_time():
    now = datetime.datetime.now()
    future = now + datetime.timedelta(days=5)
    past = now - datetime.timedelta(days=3)
    print("9️⃣ Example 9 - 5 days from now:", future)
    print("3 days ago:", past)


# =====================================================
# Example 10: Using timezone with datetime
# -----------------------------------------------------
# Explanation:
# You can assign a specific timezone to a datetime object
# using the timezone class.
# =====================================================
def example_10_timezone():
    tz = datetime.timezone(datetime.timedelta(hours=4.5))  # Afghanistan timezone (+4:30)
    x = datetime.datetime.now(tz)
    print("🔟 Example 10 - Datetime with timezone (Afghanistan):", x)


# =====================================================
# Run all examples
# =====================================================
if __name__ == "__main__":
    print("📅 Running Python Datetime Examples:\n")
    example_1_current_datetime()
    example_2_today_date()
    example_3_date_parts()
    example_4_create_datetime()
    example_5_day_name()
    example_6_custom_format()
    example_7_format_codes()
    example_8_timedelta()
    example_9_add_subtract_time()
    example_10_timezone()
