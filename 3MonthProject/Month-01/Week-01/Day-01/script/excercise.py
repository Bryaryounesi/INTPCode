# month-01
# week-01
# Day-01

# ساخت Series ساده از لیست اعداد و اسامی
import pandas as pd

# ساخت Series از اعداد
numbers = [30, 32, 13, 40, 19, 27]
s = pd.Series(numbers)
print(s)

# ساخت Series با اسامی و ایندکس دلخواه
names = ["Ali", "Sara", "Reza", "Neda"]
scores = [85, 90, 78, 92]
s = pd.Series(scores, index=names)
print(s)

# دسترسی به عناصر Series با index
print(s["Sara"])  # خروجی: 90

# تغییر مقادیر Series
s["Sara"] = 95
print(s)

# اعمال عملیات ساده روی Series
print(s + 10)    # جمع با همه مقادیر
print(s * 2)     # ضرب همه مقادیر