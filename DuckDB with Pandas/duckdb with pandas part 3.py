import duckdb
import pandas as pd

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

print("=== BETWEEN - Filtering ranges ===")
print("SQL:", duckdb.sql("SELECT * FROM df_movies WHERE rating BETWEEN 9 AND 10").df())
print("-----------------------------------")
print("Pandas:", df_movies.query("rating >= 9 and rating <= 10"))

print("=== BETWEEN with numbers ===")
print("SQL:", duckdb.sql("SELECT * FROM df_patients WHERE age BETWEEN 20 AND 30").df())
print("-----------------------------------")
print("Pandas:", df_patients.query("age >= 20 and age <= 30"))

print("=== LIKE - Pattern matching (starts with) ===")
print("SQL:", duckdb.sql("SELECT * FROM df_writers WHERE first_name LIKE 'a%'").df())
print("-----------------------------------")
print("Pandas:", df_writers[df_writers['first_name'].str.startswith('a')])

print("=== LIKE - Pattern matching (ends with) ===")
print("SQL:", duckdb.sql("SELECT * FROM df_users WHERE email LIKE '%.uk'").df())
print("-----------------------------------")
print("Pandas:", df_users[df_users['email'].str.endswith('.uk')])

print("=== LIKE - Pattern matching (contains) ===")
print("SQL:", duckdb.sql("SELECT * FROM df_users WHERE email LIKE '%gmail%'").df())
print("-----------------------------------")
print("Pandas:", df_users[df_users['email'].str.contains('gmail')])

print("=== IN - Filtering with options ===")
print("SQL:", duckdb.sql("SELECT * FROM df_customers WHERE country IN ('France', 'Germany')").df())
print("-----------------------------------")
print("Pandas:", df_customers[df_customers['country'].isin(['France', 'Germany'])])

print("=== IN with numbers ===")
print("SQL:", duckdb.sql("SELECT * FROM df_restaurants WHERE rating IN (3, 5)").df())
print("-----------------------------------")
print("Pandas:", df_restaurants[df_restaurants['rating'].isin([3, 5])])

print("=== AND - Multiple conditions ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' AND year = 1").df())
print("-----------------------------------")
print("Pandas:", df_students.query("major == 'Biology' and year == 1"))

print("=== AND with comparison operators ===")
print("SQL:", duckdb.sql("SELECT * FROM df_inventory WHERE ID < 3 AND year > 2000").df())
print("-----------------------------------")
print("Pandas:", df_inventory.query("ID < 3 and year > 2000"))

print("=== AND with BETWEEN ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' AND year BETWEEN 2 AND 4").df())
print("-----------------------------------")
print("Pandas:", df_students.query("major == 'Biology' and year >= 2 and year <= 4"))

print("=== AND with LIKE ===")
print("SQL:", duckdb.sql("SELECT * FROM df_inventory WHERE year BETWEEN 1950 AND 1960 AND manufacturer LIKE 'f%'").df())
print("-----------------------------------")
df_filtered = df_inventory.query("year >= 1950 and year <= 1960")
print("Pandas:", df_filtered[df_filtered['manufacturer'].str.startswith('f')])

print("=== OR - Alternative conditions ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' OR year = 1").df())
print("-----------------------------------")
print("Pandas:", df_students.query("major == 'Biology' or year == 1"))

print("=== OR with multiple conditions ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' OR name LIKE 'a%' OR year = 1").df())
print("-----------------------------------")
print("Pandas:", df_students.query("major == 'Biology' or name.str.startswith('a') or year == 1", engine='python'))

print("=== OR with IN ===")
print("SQL:", duckdb.sql("SELECT * FROM df_inventory WHERE ID BETWEEN 1 AND 3 OR manufacturer IN ('Jaguar', 'Ford')").df())
print("-----------------------------------")
print("Pandas:", df_inventory.query("(ID >= 1 and ID <= 3) or manufacturer in ['Jaguar', 'Ford']"))

print("=== NOT LIKE - Excluding patterns ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE name NOT LIKE 'a%'").df())
print("-----------------------------------")
print("Pandas:", df_students[~df_students['name'].str.startswith('a')])

print("=== NOT IN - Excluding options ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major NOT IN ('History', 'Physics')").df())
print("-----------------------------------")
print("Pandas:", df_students[~df_students['major'].isin(['History', 'Physics'])])

print("=== NOT BETWEEN - Excluding ranges ===")
print("SQL:", duckdb.sql("SELECT * FROM df_inventory WHERE year NOT BETWEEN 1950 AND 1970").df())
print("-----------------------------------")
print("Pandas:", df_inventory.query("year < 1950 or year > 1970"))

print("=== Complex AND combination ===")
print("SQL:", duckdb.sql("SELECT * FROM df_books WHERE genre = 'non-fiction' AND year < 2000").df())
print("-----------------------------------")
print("Pandas:", df_books.query("genre == 'non-fiction' and year < 2000"))

print("=== LIKE and IN with AND ===")
print("SQL:", duckdb.sql("SELECT * FROM df_books WHERE title LIKE '%a%' AND year IN (2001, 2003)").df())
print("-----------------------------------")
df_filtered_books = df_books[df_books['title'].str.contains('a')]
print("Pandas:", df_filtered_books[df_filtered_books['year'].isin([2001, 2003])])

print("=== IN vs OR equivalence ===")
print("SQL IN:", duckdb.sql("SELECT * FROM df_books WHERE year IN (1950, 2020)").df())
print("SQL OR:", duckdb.sql("SELECT * FROM df_books WHERE year = 1950 OR year = 2020").df())
print("-----------------------------------")
print("Pandas IN:", df_books[df_books['year'].isin([1950, 2020])])
print("Pandas OR:", df_books.query("year == 1950 or year == 2020"))