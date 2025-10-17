import pandas as pd
df= pd.read_csv(r"e:\python\INTPCode\pandas\student1.csv")
print(df.dtypes)
p = print
# 1 دسترسی به یک ستون
p(df.country)
p(df["age"])
# 2 انتخاب چند ستون
p(df[["country","age","math"]])
p(df.iloc[:,[0,2,3]])
p(df.loc[:,["name","age","biology"]])

# 3 انتخاب ردیف با loc و iloc
p("------with loc-------")
p(df.loc[:4])
p("-------with iloc----")
p(df.iloc[2:8])
# 4 چند ستون خاص انتخاب کن 
p(df.loc[:,["name","age","biology"]])

