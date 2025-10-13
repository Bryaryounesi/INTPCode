import pandas as pd

df = pd.read_csv(r"e:\python\test-project\pandas\student1.csv",index_col="id")
"""print(df.head())"""
"""print(df.info())"""
"""print(df.describe())"""
"""print(df.isna().sum())"""
for i in ["age", "math", "chemistry", "biology"]:
    df[i].fillna(df[i].mean(), inplace=True)
for x in ["name", "country"]:
    df[x].fillna("UNKNOWN", inplace=True)
"""print(df)"""
# df.columns=["namha","keshwarha","sen","riyazi","zist","shimi"]
# حذف نام ستون ایندکس
# df.index.name = None
"""print(df[df["sen"]>20])"""
"""print(df[["namha","sen"]])"""
# print(df.sen)
# print(df[["namha","keshwarha"]])
# print(df.loc[:,["name","math"]])
# print(df.iloc[5:10,0:3])
# df.sort_index(inplace=True)
# print(df.iloc[1:6,[0,2]])
# df.sort_values(by="math",inplace=True,ascending=False)
# print(df)
# دادن پارامتر ascending به صورت لیست برای دو ستون
# df.sort_values(by=["age","math"],inplace= True,ascending=[True,False])
# print(df)
# print(df["math"].mean())
# print()
# print( df[df["biology"] == df["biology"].max()])
# print(df.iloc[-5:])
# print(df.tail())
# print(df.iloc[:5])
# print(df.iloc[1:4])
# print(df.loc[:5])
# print(df.iloc[-5:])
print(df.info())
# df.reset_index(inplace=True)
print(df)
