# Month-01
# Week-01
# Day-05

# ساخت آرایه با np.array
import numpy as np
p=print
numbers=[i for i in range(-20,50,3)]
a= np.array(numbers)
# p(a)
# ساخت ماتریس با zeros, ones, arange
m_zeros=np.zeros((4,4))
m_ones = np.ones((5,5))
m_arrange= np.arange(100).reshape(25,4)

# shape و reshape

# ریشیب برای تبدیل کردن آرایه های خطی به ماتریس است
# البته قبل از ریشیب باید بدانیم آرایه اولیه چند عنصر دارد
# چون حاصلضرب تعداد ردیف ها و ستون های ماتریسی که با ریشیب میسازیم باید برابر عدد کل عناصر آرایه اولیه باشد

newarr= np.array([i for i in range(15,45,2)]) #ساخت آرایه جدید
p("newarr elements count:" , np.size(newarr)) #محاسبه تعداد المنت های آرایه جدید
reshaped_arr= newarr.reshape(5,3) #ریشیپ آرایه برای ساخت ماتریس
# p(reshaped_arr)

# پی بردن به تعداد ستون ها و ردیف های ماتریس با شیپ
p("matrix rows count: ",reshaped_arr.shape[0])
p("matrix columns count: ",reshaped_arr.shape[1])
p("--------------------------------------------")
p("excercise:")
# تمرین یک آرایه 12تایی بساز
arr_12= np.array([i for i in range(12)])

# آن را به ماتریس 3×4 تبدیل کن و نمایش بده
mtx_12=arr_12.reshape(4,3)
p("mtx_12 matrix:")
p(mtx_12)