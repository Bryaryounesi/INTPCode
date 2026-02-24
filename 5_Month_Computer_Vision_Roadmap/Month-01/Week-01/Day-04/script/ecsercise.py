# Month-01
# Week-01
# Day-04

# تمرین تابعی بنویس که حقوق پایه + درصد کمیسیون را دریافت کرده و حقوق 
# نهایی را حساب کند
p=print
def calculate_salary(primary_salary,tax_percent):
    salary = primary_salary -(primary_salary * tax_percent)
    p("your salary is: ", salary)
    return salary
manager_salary = calculate_salary(5000,0.02)
worker_salary= calculate_salary(1500,0.01)

# این یک تابع هلپر است چون علاوه بر پیام تابع، دارای ریترن و خروجی هم هست
# خروجی تابع در متغیر های مربوه ذخیره شد