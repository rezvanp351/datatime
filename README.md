# 🕓 Python Datetime — Full Tutorial Examples (W3Schools Version)

This document contains **all examples** and **clear explanations** from the  
W3Schools **Python Datetime** tutorial — converted from the file  
`datetime_examples.py`.

Each example is **numbered**, **explained**, and includes **expected outputs**  
for easy understanding and GitHub documentation.

---

## 📘 Importing the Datetime Module

```python
import datetime
```

The `datetime` module allows working with **dates and times** in Python.

---

## 🧩 Example 1: Get the Current Date and Time

```python
x = datetime.datetime.now()
print("1️⃣ Example 1 - Current date & time:", x)
```

📝 **Explanation:**  
`datetime.now()` returns the **current local date and time**.

💡 **Example Output:**
```
1️⃣ Example 1 - Current date & time: 2025-11-02 10:25:31.123456
```

---

## 📅 Example 2: Get Only the Current Date

```python
x = datetime.date.today()
print("2️⃣ Example 2 - Today's date:", x)
```

📝 **Explanation:**  
`date.today()` gives **today’s date** without time information.

💡 **Example Output:**
```
2️⃣ Example 2 - Today's date: 2025-11-02
```

---

## 🧠 Example 3: Access Parts of a Datetime Object

```python
x = datetime.datetime.now()
print("Year:", x.year)
print("Month:", x.month)
print("Day:", x.day)
print("Hour:", x.hour)
print("Minute:", x.minute)
print("Second:", x.second)
```

📝 **Explanation:**  
You can access **year, month, day, hour, minute, second** attributes.

💡 **Example Output:**
```
Year: 2025
Month: 11
Day: 2
Hour: 10
Minute: 30
Second: 15
```

---

## 🛠️ Example 4: Create a Specific Datetime Object

```python
x = datetime.datetime(2020, 5, 17, 10, 30)
print("4️⃣ Example 4 - Created datetime object:", x)
```

📝 **Explanation:**  
Specify `year, month, day` (and optionally `hour`, `minute`, `second`)  
to create a custom datetime object.

💡 **Output:**
```
4️⃣ Example 4 - Created datetime object: 2020-05-17 10:30:00
```

---

## 📆 Example 5: Display the Weekday Name Using strftime()

```python
x = datetime.datetime.now()
print("5️⃣ Example 5 - Weekday name:", x.strftime("%A"))
```

📝 **Explanation:**  
`strftime("%A")` converts the datetime object into a **string**  
showing the **weekday name** (e.g., Sunday, Monday, etc.).

💡 **Output Example:**
```
5️⃣ Example 5 - Weekday name: Sunday
```

---

## 🎨 Example 6: Format Datetime Using strftime()

```python
x = datetime.datetime(2024, 3, 21, 15, 45, 30)
formatted = x.strftime("%Y-%m-%d %H:%M:%S")
print("6️⃣ Example 6 - Custom formatted date:", formatted)
```

📝 **Explanation:**  
`strftime()` allows **custom date/time formatting**.

💡 **Output Example:**
```
6️⃣ Example 6 - Custom formatted date: 2024-03-21 15:45:30
```

---

## 🔤 Example 7: Date Format Codes Demonstration

```python
x = datetime.datetime(2023, 11, 2, 14, 30, 45)
print("%a  ➜", x.strftime("%a"), "(Abbreviated weekday name)")
print("%A  ➜", x.strftime("%A"), "(Full weekday name)")
print("%d  ➜", x.strftime("%d"), "(Day of month)")
print("%B  ➜", x.strftime("%B"), "(Full month name)")
print("%Y  ➜", x.strftime("%Y"), "(Full year)")
print("%I %p ➜", x.strftime("%I %p"), "(12-hour clock with AM/PM)")
print("%H:%M:%S ➜", x.strftime("%H:%M:%S"), "(24-hour clock)")
```

📝 **Explanation:**  
Common formatting codes in Python’s `strftime()` method.

💡 **Example Output:**
```
%a  ➜ Thu (Abbreviated weekday name)
%A  ➜ Thursday (Full weekday name)
%d  ➜ 02 (Day of month)
%B  ➜ November (Full month name)
%Y  ➜ 2023 (Full year)
%I %p ➜ 02 PM (12-hour clock with AM/PM)
%H:%M:%S ➜ 14:30:45 (24-hour clock)
```

---

## ⏳ Example 8: Difference Between Two Dates (timedelta)

```python
date1 = datetime.datetime(2024, 5, 10)
date2 = datetime.datetime(2024, 5, 15)
delta = date2 - date1
print("8️⃣ Example 8 - Difference between two dates:", delta.days, "days")
```

📝 **Explanation:**  
`timedelta` calculates the **difference between two dates**.

💡 **Output Example:**
```
8️⃣ Example 8 - Difference between two dates: 5 days
```

---

## ⏰ Example 9: Add or Subtract Time Using timedelta

```python
now = datetime.datetime.now()
future = now + datetime.timedelta(days=5)
past = now - datetime.timedelta(days=3)
print("9️⃣ Example 9 - 5 days from now:", future)
print("3 days ago:", past)
```

📝 **Explanation:**  
Add or subtract a **specific period** (e.g., days, hours)  
from a datetime using `timedelta`.

💡 **Output Example:**
```
9️⃣ Example 9 - 5 days from now: 2025-11-07 10:35:22.000000
3 days ago: 2025-10-30 10:35:22.000000
```

---

## 🌍 Example 10: Using Timezone with Datetime

```python
tz = datetime.timezone(datetime.timedelta(hours=4.5))  # Afghanistan timezone (+4:30)
x = datetime.datetime.now(tz)
print("🔟 Example 10 - Datetime with timezone (Afghanistan):", x)
```

📝 **Explanation:**  
You can use the `timezone` class to assign a specific time zone  
(such as **Afghanistan UTC+4:30**).

💡 **Output Example:**
```
🔟 Example 10 - Datetime with timezone (Afghanistan): 2025-11-02 10:35:22.123456+04:30
```

---

## 🧭 Running All Examples Together

```python
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
```

---

## 🌟 Final Notes

You have now learned how to:

✅ Get current date & time  
✅ Create and format datetime objects  
✅ Use `strftime()` format codes  
✅ Calculate date differences  
✅ Work with timezones  

---

### ❤️ Support This Project

If this tutorial helped you:

⭐ **Give it a Star** on GitHub  
👤 **Follow** for more Python examples  
🔁 **Share** it with your friends!

---

**Author:** *W3Schools + Adapted & Explained by Rezvan Panah*  
📅 **Updated:** November 2025
