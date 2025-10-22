import duckdb
import pandas as pd
p = print

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

p("=== SELECT یک ستون ===")
p("SQL:", duckdb.sql("SELECT name FROM df_users").df())
p("Pandas:", df_users[['name']])
p("--------------------")

p("\n=== SELECT چند ستون ===")
p("SQL:", duckdb.sql("SELECT name, email FROM df_users").df())
p("Pandas:", df_users[['name', 'email']])


p("\n=== SELECT تمام ستون‌ها ===")
p("SQL:", duckdb.sql("SELECT * FROM df_users").df())
p("Pandas:", df_users)
p("--------------------")

p("\n=== DISTINCT ===")
p("SQL:", duckdb.sql("SELECT DISTINCT type FROM df_membership").df())
p("Pandas:", df_membership[['type']].drop_duplicates())
p("--------------------")

p("\n=== ORDER BY صعودی ===")
p("SQL:", duckdb.sql("SELECT * FROM df_patients ORDER BY name").df())
p("Pandas:", df_patients.sort_values('name'))
p("--------------------")

p("\n=== ORDER BY نزولی ===")
p("SQL:", duckdb.sql("SELECT * FROM df_patients ORDER BY age DESC").df())
p("Pandas:", df_patients.sort_values('age', ascending=False))
p("--------------------")

p("\n=== WHERE با متن ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology'").df())
p("Pandas:", df_students.query("major == 'Biology'"))
p("--------------------")

p("\n=== WHERE با عدد ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE year = 1").df())
p("Pandas:", df_students.query("year == 1"))
p("--------------------")

p("\n=== عملگر نابرابری <> ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major <> 'Biology'").df())
p("Pandas:", df_students.query("major != 'Biology'"))
p("--------------------")

p("\n=== عملگر کوچکتر از < ===")
p("SQL:", duckdb.sql("SELECT * FROM df_chocolate WHERE price < 2").df())
p("Pandas:", df_chocolate.query("price < 2"))
p("--------------------")

p("\n=== عملگر بزرگتر از > ===")
p("SQL:", duckdb.sql("SELECT * FROM df_chocolate WHERE price > 2").df())
p("Pandas:", df_chocolate.query("price > 2"))
p("--------------------")

p("\n=== عملگر کوچکتر مساوی <= ===")
p("SQL:", duckdb.sql("SELECT * FROM df_chocolate WHERE price <= 2").df())
p("Pandas:", df_chocolate.query("price <= 2"))
p("--------------------")

p("\n=== عملگر بزرگتر مساوی >= ===")
p("SQL:", duckdb.sql("SELECT * FROM df_chocolate WHERE price >= 2").df())
p("Pandas:", df_chocolate.query("price >= 2"))
p("--------------------")

p("\n=== AS برای تغییر نام ستون ===")
p("SQL:", duckdb.sql("SELECT name AS student_name, major AS field FROM df_students").df())
p("Pandas:", df_students[['name', 'major']].rename(columns={'name': 'student_name', 'major': 'field'}))
p("--------------------")

p("\n=== WHERE با AND ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' AND year = 1").df())
p("Pandas:", df_students.query("major == 'Biology' and year == 1"))
p("--------------------")

p("\n=== WHERE با OR ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' OR major = 'Math'").df())
p("Pandas:", df_students.query("major == 'Biology' or major == 'Math'"))
p("--------------------")

p("\n=== SELECT ستون‌های خاص با WHERE ===")
p("SQL:", duckdb.sql("SELECT name, score FROM df_students WHERE year = 1").df())
p("Pandas:", df_students.query("year == 1")[['name', 'score']])
p("--------------------")

p("\n=== ORDER BY چند ستون ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students ORDER BY major, score DESC").df())
p("Pandas:", df_students.sort_values(['major', 'score'], ascending=[True, False]))
p("--------------------")

p("\n=== LIMIT برای محدود کردن نتایج ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students ORDER BY score DESC LIMIT 2").df())
p("Pandas:", df_students.nlargest(2, 'score'))
p("--------------------")

p("\n=== ترکیب ORDER BY و WHERE ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE year = 1 ORDER BY score DESC").df())
p("Pandas:", df_students.query("year == 1").sort_values('score', ascending=False))
p("--------------------")

p("\n=== SELECT از books ===")
p("SQL:", duckdb.sql("SELECT * FROM df_books WHERE genre = 'fiction'").df())
p("Pandas:", df_books.query("genre == 'fiction'"))
p("--------------------")

p("\n=== SELECT از pollution ===")
p("SQL:", duckdb.sql("SELECT * FROM df_pollution WHERE pollution_index > 100").df())
p("Pandas:", df_pollution.query("pollution_index > 100"))
p("--------------------")

p("\n=== SELECT از mario_games ===")
p("SQL:", duckdb.sql("SELECT name AS game_name, release AS release_year FROM df_mario_games").df())
p("Pandas:", df_mario_games[['name', 'release']].rename(columns={'name': 'game_name', 'release': 'release_year'}))
p("--------------------")

p("\n=== SELECT از flights ===")
p("SQL:", duckdb.sql("SELECT * FROM df_flights WHERE daily = 1").df())
p("Pandas:", df_flights.query("daily == 1"))
p("--------------------")

p("\n=== SELECT با شرط مرکب ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE (major = 'Biology' AND score > 80) OR (major = 'Math' AND score > 90)").df())
p("Pandas:", df_students.query("(major == 'Biology' and score > 80) or (major == 'Math' and score > 90)"))
