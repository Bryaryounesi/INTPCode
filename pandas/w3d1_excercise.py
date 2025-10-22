# 1- یک فایل Excel (مثلاً داده فروش یا دانش‌آموزان) باز کن
import pandas as pd
path = r"e:\python\INTPCode\pandas\w3d1_excel.xlsx"
df = pd.read_excel(path,sheet_name=None)
# 2- داده‌ها رو با read_excel بخون
p = print
p(df.keys())
# خواندن سه شیت منتخب که اسامی آنها را از تابع کیز به دست آوردیم
p(*[df[i] for i in ['orders', 'reservation', 'flights']],sep="\n\n")

# 3- فقط چند ستون خاص رو انتخاب کن
sh4df= pd.read_excel(path,sheet_name=4 , usecols=range(0,2))
# 4- چند ردیف اول و آخر رو با head() و tail() ببین
p(sh4df.tail(4))
p(sh4df.head(3))
# 5- اگه فایل چند شیت داره، فقط یکی از شیت‌ها رو بخون
sh5df=pd.read_excel(path,sheet_name=5,nrows= 3)
p(sh5df)