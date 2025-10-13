import pandas as pd
# 1- یک داتاست واقعی بخون
df = pd.read_csv(r"e:\python\test-project\pandas\student1.csv",index_col="id")
p = print
df.dropna(inplace=True)
# 2- ستون ها و ردیف ها رو انتخاب کن
# p(df[["name","math"]])
# p(df.iloc[:15])

# 3- فیلتر چند شرطی اعمال کن

# p(df.query("age.gt(40) and country.isin(['Iran','Iraq'])"))
# p(df.query("country != 'Iran'"))
# p(df.query("not country.isin(['Iran','Iraq'])"))
# p(df.query("country not in['Iran','Iraq'] and not age >40"))
# p(df.query("not(age > 40 or math < 14)"))
# p(df.query("not age >40 and not country == 'Iran'"))
df = df.query("not age.between(20,40) ")
# p(df)

# 4-داده ها را مرتب کن
df.sort_values(by="age",inplace=True,ascending=False)
p(df)

# 5-نتایج آماری پایه را نمایش بده

# p(df["age"].sum())
# p(df[["age","math","chemistry"]].mean())
p(df.agg({"math":["median","std","min"],
                      "chemistry":["sum","max","mean"]}))
# اعمال چند تابع آماری روی کل داتافریم به صورت یکجا
p(df.agg(["sum","min","max"]))
