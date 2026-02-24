# Month-01
# Week-01
# Day-02

# برنامه‌ای بنویس که قد و وزن را بگیرد و بر اساس 
# BMI
# وضعیت کاربر را تشخیص دهد (ساده، دقیق نباشد)

weight=input("please inter your weight by kg ")
height=input("please inter your height by cm ")
bmi=round(int(weight)/(int(height)/100)**2)
p=print

if bmi< 18.5:
    p(f"your bmi is {bmi}, so you are low weight")
elif bmi >=18.5 or bmi< 25:
    p(f"your bmi is {bmi}, so your weight is normal")
elif bmi>=25 or bmi <30:   
    p(f"your bmi is {bmi}, so you have extra weight")
else:
    p(f"your bmi is {bmi}, so you are fat")
    # از اف استرینگ استفاده کردیم که در مباحث مرور شده نبود
    # از مبحث عملگرهای مقایسه ای و 
    # if,elif,else , input

# این کد صرفا برای یادآوری مبحث شرط هاست
# چون از لوپ ها، مدیریت خطا و مدیریت ورودیِ درست استفاده نشده
# ممکن است به سرعت خطا دهد    