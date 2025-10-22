import duckdb
import pandas as pd
p = print
# Read all sheets from Excel file

file_path = r'e:\python\INTPCode\DuckDB with Pandas\database3.xlsx'
all_sheets = pd.read_excel(file_path, sheet_name=None)

df_movies = all_sheets['movies']
df_patients = all_sheets['patients']
df_writers = all_sheets['writers']
df_coffee = all_sheets['coffee']
df_customers = all_sheets['customers']
df_restaurants = all_sheets['restaurants']
df_mario_games = all_sheets['mario_games']
df_users = all_sheets['users']
df_membership = all_sheets['membership']
df_students = all_sheets['students']
df_inventory = all_sheets['inventory']
df_books = all_sheets['books']

p("=== BETWEEN - Filtering ranges ===")
p("SQL:", duckdb.sql("SELECT * FROM df_movies WHERE rating BETWEEN 9 AND 10").df())
p("-----------------------------------")
p("Pandas:", df_movies.query("rating >= 9 and rating <= 10"))

p("=== BETWEEN with numbers ===")
p("SQL:", duckdb.sql("SELECT * FROM df_patients WHERE age BETWEEN 20 AND 30").df())
p("-----------------------------------")
p("Pandas:", df_patients.query("age >= 20 and age <= 30"))

p("=== LIKE - Pattern matching (starts with) ===")
p("SQL:", duckdb.sql("SELECT * FROM df_writers WHERE first_name LIKE 'a%'").df())
p("-----------------------------------")
p("Pandas:", df_writers[df_writers['first_name'].str.startswith('a')])

p("=== LIKE - Pattern matching (ends with) ===")
p("SQL:", duckdb.sql("SELECT * FROM df_users WHERE email LIKE '%.uk'").df())
p("-----------------------------------")
p("Pandas:", df_users[df_users['email'].str.endswith('.uk')])

p("=== LIKE - Pattern matching (contains) ===")
p("SQL:", duckdb.sql("SELECT * FROM df_users WHERE email LIKE '%gmail%'").df())
p("-----------------------------------")
p("Pandas:", df_users[df_users['email'].str.contains('gmail')])

p("=== IN - Filtering with options ===")
p("SQL:", duckdb.sql("SELECT * FROM df_customers WHERE country IN ('France', 'Germany')").df())
p("-----------------------------------")
p("Pandas:", df_customers[df_customers['country'].isin(['France', 'Germany'])])

p("=== IN with numbers ===")
p("SQL:", duckdb.sql("SELECT * FROM df_restaurants WHERE rating IN (3, 5)").df())
p("-----------------------------------")
p("Pandas:", df_restaurants[df_restaurants['rating'].isin([3, 5])])

p("=== AND - Multiple conditions ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' AND year = 1").df())
p("-----------------------------------")
p("Pandas:", df_students.query("major == 'Biology' and year == 1"))

p("=== AND with comparison operators ===")
p("SQL:", duckdb.sql("SELECT * FROM df_inventory WHERE ID < 3 AND year > 2000").df())
p("-----------------------------------")
p("Pandas:", df_inventory.query("ID < 3 and year > 2000"))

p("=== AND with BETWEEN ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' AND year BETWEEN 2 AND 4").df())
p("-----------------------------------")
p("Pandas:", df_students.query("major == 'Biology' and year >= 2 and year <= 4"))

p("=== AND with LIKE ===")
p("SQL:", duckdb.sql("SELECT * FROM df_inventory WHERE year BETWEEN 1950 AND 1960 AND manufacturer LIKE 'f%'").df())
p("-----------------------------------")
df_filtered = df_inventory.query("year >= 1950 and year <= 1960")
p("Pandas:", df_filtered[df_filtered['manufacturer'].str.startswith('f')])

p("=== OR - Alternative conditions ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' OR year = 1").df())
p("-----------------------------------")
p("Pandas:", df_students.query("major == 'Biology' or year == 1"))

p("=== OR with multiple conditions ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' OR name LIKE 'a%' OR year = 1").df())
p("-----------------------------------")
p("Pandas:", df_students.query("major == 'Biology' or name.str.startswith('a') or year == 1", engine='python'))

p("=== OR with IN ===")
p("SQL:", duckdb.sql("SELECT * FROM df_inventory WHERE ID BETWEEN 1 AND 3 OR manufacturer IN ('Jaguar', 'Ford')").df())
p("-----------------------------------")
p("Pandas:", df_inventory.query("(ID >= 1 and ID <= 3) or manufacturer in ['Jaguar', 'Ford']"))

p("=== NOT LIKE - Excluding patterns ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE name NOT LIKE 'a%'").df())
p("-----------------------------------")
p("Pandas:", df_students[~df_students['name'].str.startswith('a')])

p("=== NOT IN - Excluding options ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major NOT IN ('History', 'Physics')").df())
p("-----------------------------------")
p("Pandas:", df_students[~df_students['major'].isin(['History', 'Physics'])])

p("=== NOT BETWEEN - Excluding ranges ===")
p("SQL:", duckdb.sql("SELECT * FROM df_inventory WHERE year NOT BETWEEN 1950 AND 1970").df())
p("-----------------------------------")
p("Pandas:", df_inventory.query("year < 1950 or year > 1970"))

p("=== Complex AND combination ===")
p("SQL:", duckdb.sql("SELECT * FROM df_books WHERE genre = 'non-fiction' AND year < 2000").df())
p("-----------------------------------")
p("Pandas:", df_books.query("genre == 'non-fiction' and year < 2000"))

p("=== LIKE and IN with AND ===")
p("SQL:", duckdb.sql("SELECT * FROM df_books WHERE title LIKE '%a%' AND year IN (2001, 2003)").df())
p("-----------------------------------")
df_filtered_books = df_books[df_books['title'].str.contains('a')]
p("Pandas:", df_filtered_books[df_filtered_books['year'].isin([2001, 2003])])

p("=== IN vs OR equivalence ===")
p("SQL IN:", duckdb.sql("SELECT * FROM df_books WHERE year IN (1950, 2020)").df())
p("SQL OR:", duckdb.sql("SELECT * FROM df_books WHERE year = 1950 OR year = 2020").df())
p("-----------------------------------")
p("Pandas IN:", df_books[df_books['year'].isin([1950, 2020])])
p("Pandas OR:", df_books.query("year == 1950 or year == 2020"))