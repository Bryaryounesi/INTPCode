# month-02
# week-01
# Day-02

# ۱- ساخت یک ماتریس 3×3
import numpy as np
p=print
m=np.array([
    [2,3,0],[4,-5,6],[1,4,6]
])
# p(m)

# 2- انتخاب یک ردیف، یک ستون، و یک عنصر
p("second row:",m[1])
p("last column:",m[:,2])
p("second element of third column:",m[1,2])

# 3- محاسبه جمع و میانگین هر ستون یا ردیف
p("columns sumation:",np.sum(m,axis=1))
p("columns mean:",np.mean(m,axis=1).round())

p("rows sumation:",np.sum(m,axis=0))
p("rows mean:",np.mean(m,axis=0).round())
