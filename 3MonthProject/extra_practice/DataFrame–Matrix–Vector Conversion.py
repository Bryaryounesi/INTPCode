# تبدیل ستون داتافریم به بردار و بالعکس

# ستون <<<>>>لیست<<<>>> بردار
import pandas as pd
import numpy as np
p= print
path=r"e:\python\INTPCode\3MonthProject\Month-01\data\students_scores_shared.xlsx"
df= pd.read_excel(path)
# p(df)

df1= df.select_dtypes(include="number").drop("id",axis=1)
# یک داتافریم از داده های عددی ساختیم

col1= [i for i in df["age"]]
# col1= df1["age"].values.tolist()
# p(col1)
# یک ستون آن را به لیست تبدیل کردیم به دو روش 


v= np.array(col1)
p(v)
# آن ستون را به بردار تبدیل کردیم

newlist= v.tolist()
p(newlist)

# بردار را دوباره به لیست تبدیل کردیم

p("-------------------------")

# تبدیل داتافریم به ماتریس و بالعکس
# داتافریم<<<>>> لیست لیست ها >>> ماتریس 
ListOfList= df1.values.tolist()
# p(ListOfList)
# داتافریم را به لیستی از لیست ها تبدیل کردیم

m= np.array(ListOfList)
# p(m)
# لیست لیست ها رو به ماتریس تبدیل کردیم

# اگر بخواهیم دوباره ماتریس را به داتافریم تبدیل کنیم 
# باید خودمان اسامی ستون ها را با داتافرین بدهیم 
#اسامی ستون ها حذف شده اند در ماتریس

p(df1.columns)
# بدست آوردن اسامی ستون های داتافریم اولیه 

col= ['age', 'math', 'biology', 'chemistry']
# ساخت لیستی از اسامی نام ستون ها برای استفاده از 
# این لیست به عنوان والیوی پارامتر کولومنز
dfm=pd.DataFrame(m,columns=col)
# p(dfm)


