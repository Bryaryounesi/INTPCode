# Month-01
# Week-01
# Day-02

# برنامه‌ای بنویس که قد و وزن را بگیرد و بر اساس 
# BMI
# وضعیت کاربر را تشخیص دهد (ساده، دقیق نباشد)

p = print

def bmi(height,wight):
    bmi = wight/(height/100)**2
#   ابتدا فرمول بی ام آی را در تابع تعریف کردیم
    if bmi >=40:
        p("extra fat","bmi: ", round(bmi))
    elif bmi  >=35:
        p("fat class 2","bmi: ", round(bmi))  
    elif bmi  >=30:
        p("fat class 1","bmi: ", round(bmi)) 
    elif bmi  >=25:
        p("extra weight","bmi: ", round(bmi)) 
    elif bmi  >=18.5:
        p("normal","bmi: ", round(bmi)) 
    else:
        p("low weight","bmi: ", round(bmi)) 
p("weight is by kg and height is by cm")           
bmi(172,84)  