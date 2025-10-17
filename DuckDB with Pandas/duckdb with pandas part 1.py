import duckdb
import pandas as pd
file_path = r'e:\python\INTPCode\DuckDB with Pandas\database1.xlsx'
all_sheets = pd.read_excel(file_path, sheet_name=None)

df_users = all_sheets['users']
df_students = all_sheets['students']
df_books = all_sheets['books']
df_patients = all_sheets['patients']
df_chocolate = all_sheets['chocolate']
df_membership = all_sheets['membership']
df_pollution = all_sheets['pollution']
df_mario_games = all_sheets['mario_games']
df_flights = all_sheets['flights']

print("=== SELECT یک ستون ===")
print("SQL:", duckdb.sql("SELECT name FROM df_users").df())
print("Pandas:", df_users[['name']])
print("--------------------")

print("\n=== SELECT چند ستون ===")
print("SQL:", duckdb.sql("SELECT name, email FROM df_users").df())
print("Pandas:", df_users[['name', 'email']])


print("\n=== SELECT تمام ستون‌ها ===")
print("SQL:", duckdb.sql("SELECT * FROM df_users").df())
print("Pandas:", df_users)
print("--------------------")

print("\n=== DISTINCT ===")
print("SQL:", duckdb.sql("SELECT DISTINCT type FROM df_membership").df())
print("Pandas:", df_membership[['type']].drop_duplicates())
print("--------------------")

print("\n=== ORDER BY صعودی ===")
print("SQL:", duckdb.sql("SELECT * FROM df_patients ORDER BY name").df())
print("Pandas:", df_patients.sort_values('name'))
print("--------------------")

print("\n=== ORDER BY نزولی ===")
print("SQL:", duckdb.sql("SELECT * FROM df_patients ORDER BY age DESC").df())
print("Pandas:", df_patients.sort_values('age', ascending=False))
print("--------------------")

print("\n=== WHERE با متن ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology'").df())
print("Pandas:", df_students.query("major == 'Biology'"))
print("--------------------")

print("\n=== WHERE با عدد ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE year = 1").df())
print("Pandas:", df_students.query("year == 1"))
print("--------------------")

print("\n=== عملگر نابرابری <> ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major <> 'Biology'").df())
print("Pandas:", df_students.query("major != 'Biology'"))
print("--------------------")

print("\n=== عملگر کوچکتر از < ===")
print("SQL:", duckdb.sql("SELECT * FROM df_chocolate WHERE price < 2").df())
print("Pandas:", df_chocolate.query("price < 2"))
print("--------------------")

print("\n=== عملگر بزرگتر از > ===")
print("SQL:", duckdb.sql("SELECT * FROM df_chocolate WHERE price > 2").df())
print("Pandas:", df_chocolate.query("price > 2"))
print("--------------------")

print("\n=== عملگر کوچکتر مساوی <= ===")
print("SQL:", duckdb.sql("SELECT * FROM df_chocolate WHERE price <= 2").df())
print("Pandas:", df_chocolate.query("price <= 2"))
print("--------------------")

print("\n=== عملگر بزرگتر مساوی >= ===")
print("SQL:", duckdb.sql("SELECT * FROM df_chocolate WHERE price >= 2").df())
print("Pandas:", df_chocolate.query("price >= 2"))
print("--------------------")

print("\n=== AS برای تغییر نام ستون ===")
print("SQL:", duckdb.sql("SELECT name AS student_name, major AS field FROM df_students").df())
print("Pandas:", df_students[['name', 'major']].rename(columns={'name': 'student_name', 'major': 'field'}))
print("--------------------")

print("\n=== WHERE با AND ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' AND year = 1").df())
print("Pandas:", df_students.query("major == 'Biology' and year == 1"))
print("--------------------")

print("\n=== WHERE با OR ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' OR major = 'Math'").df())
print("Pandas:", df_students.query("major == 'Biology' or major == 'Math'"))
print("--------------------")

print("\n=== SELECT ستون‌های خاص با WHERE ===")
print("SQL:", duckdb.sql("SELECT name, score FROM df_students WHERE year = 1").df())
print("Pandas:", df_students.query("year == 1")[['name', 'score']])
print("--------------------")

print("\n=== ORDER BY چند ستون ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students ORDER BY major, score DESC").df())
print("Pandas:", df_students.sort_values(['major', 'score'], ascending=[True, False]))
print("--------------------")

print("\n=== LIMIT برای محدود کردن نتایج ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students ORDER BY score DESC LIMIT 2").df())
print("Pandas:", df_students.nlargest(2, 'score'))
print("--------------------")

print("\n=== ترکیب ORDER BY و WHERE ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE year = 1 ORDER BY score DESC").df())
print("Pandas:", df_students.query("year == 1").sort_values('score', ascending=False))
print("--------------------")

print("\n=== SELECT از books ===")
print("SQL:", duckdb.sql("SELECT * FROM df_books WHERE genre = 'fiction'").df())
print("Pandas:", df_books.query("genre == 'fiction'"))
print("--------------------")

print("\n=== SELECT از pollution ===")
print("SQL:", duckdb.sql("SELECT * FROM df_pollution WHERE pollution_index > 100").df())
print("Pandas:", df_pollution.query("pollution_index > 100"))
print("--------------------")

print("\n=== SELECT از mario_games ===")
print("SQL:", duckdb.sql("SELECT name AS game_name, release AS release_year FROM df_mario_games").df())
print("Pandas:", df_mario_games[['name', 'release']].rename(columns={'name': 'game_name', 'release': 'release_year'}))
print("--------------------")

print("\n=== SELECT از flights ===")
print("SQL:", duckdb.sql("SELECT * FROM df_flights WHERE daily = 1").df())
print("Pandas:", df_flights.query("daily == 1"))
print("--------------------")

print("\n=== SELECT با شرط مرکب ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE (major = 'Biology' AND score > 80) OR (major = 'Math' AND score > 90)").df())
print("Pandas:", df_students.query("(major == 'Biology' and score > 80) or (major == 'Math' and score > 90)"))
