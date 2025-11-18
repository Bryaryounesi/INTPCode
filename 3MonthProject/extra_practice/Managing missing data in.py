# Managing missing data in pandas
p= print
import pandas as pd
path = r"e:\python\INTPCode\pandas\to_excel.xlsx"
df6= pd.read_excel(path,sheet_name="sh6",nrows = 30)
df7= pd.read_excel(path,sheet_name="sh7",nrows = 30)
dfm = pd.merge(df6,df7,how = "outer",on =["names","country","age","gender"])


# dfm.dropna(inplace=True,ignore_index=True)

# پرکردن کل مقادیر خالی با یک مقدار ثابت/با مقدار قبل یا بعد 
# dfm.fillna(0,inplace=True)
# dfm.ffill(inplace=True)
# dfm.bfill(inplace=True)
# p(dfm)

#روش دوم . پاکسازی سلولی کل داتافریم
# در پاکسازی سلولی با دراپنا نباید از پارامتر اینپلیس ترو استفاده کنیم

# for i in dfm.columns:
    # dfm[i] = dfm[i].dropna(ignore_index=True)
# p(dfm)

# روش سوم. پاکسازی سلولی انتخابی  
# تنها ستون های عددی

num_cols = dfm.select_dtypes(include="number")
# for i in num_cols.columns:
    # dfm[i] =dfm[i].dropna(ignore_index=True)
    #  پر کردن ستون های عددی به روش های مختلف
    # dfm[i] =dfm[i].fillna(dfm[i].mean().round())
    # dfm[i] =dfm[i].fillna(dfm[i].mode()[0]) 
    # dfm[i] =dfm[i].fillna(0)
    # dfm[i].ffill()/bfill()
# p(dfm)

# تنها سلول های غیر عددی
unnum_cols= dfm.select_dtypes(include=(["string","object"]))
# for i in unnum_cols.columns:
    # dfm[i] = dfm[i].dropna(ignore_index=True)
    # پر کردن ستون های غیر عددی به روش های مختلف
    # dfm[i] =dfm[i].fillna(dfm[i].mode()[0]) 
    # dfm[i] =dfm[i].fillna(0)
    # dfm[i].ffill()/bfill()
# p(dfm)

#  روش چهارم . سمپل گیری از تمام ستون ها و  جایگزینی سمپل با مقادیر خالی آن ستون
'''
for i in dfm.columns:
    cleaned = dfm[i].dropna(ignore_index=True)
    #  این یک داتافریم پاکسازی شده از مقادیر خالی به ما میده
    sampled = cleaned.sample(n=dfm[i].isna().sum(), replace=True, random_state=1)    
    # سمپل گیری به اندازه مقادیر خالی هر ستون از مقادیر پاکسازی شده آن ستون 
    dfm.loc[dfm[i].isna(), i] = sampled.values
p(dfm)
'''