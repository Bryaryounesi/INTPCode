import duckdb
import pandas as pd
p = print
# Read all sheets from Excel file
file_path = r'e:\python\INTPCode\DuckDB with Pandas\database4.xlsx'
all_sheets = pd.read_excel(file_path, sheet_name=None)

df_contacts = all_sheets['contacts']
df_students = all_sheets['students']
df_ticket = all_sheets['ticket']
df_running_distance = all_sheets['running_distance']
df_wishlist = all_sheets['wishlist']
df_team = all_sheets['team']
df_orders = all_sheets['orders']
df_test = all_sheets['test']
df_user = all_sheets['user']
df_coffee = all_sheets['coffee']
df_project_time = all_sheets['project_time']
df_sales = all_sheets['sales']

p("=== ALIASING - Single column ===")
p("SQL:", duckdb.sql("SELECT first_name AS user FROM df_contacts").df())
p("-----------------------------------")
p("Pandas:", df_contacts[['first_name']].rename(columns={'first_name': 'user'}))

p("=== ALIASING - Multiple columns ===")
p("SQL:", duckdb.sql("SELECT first_name AS user, email AS contact FROM df_contacts").df())
p("-----------------------------------")
p("Pandas:", df_contacts[['first_name', 'email']].rename(columns={'first_name': 'user', 'email': 'contact'}))

p("=== ALIASING with WHERE ===")
p("SQL:", duckdb.sql("SELECT name AS student, score FROM df_students WHERE score = 9").df())
p("-----------------------------------")
p("Pandas:", df_students[['name', 'score']].rename(columns={'name': 'student'}).query("score == 9"))

p("=== MIN - Find minimum value ===")
p("SQL:", duckdb.sql("SELECT MIN(price) FROM df_ticket").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'min_price': [df_ticket['price'].min()]}))

p("=== MAX - Find maximum value ===")
p("SQL:", duckdb.sql("SELECT MAX(price) FROM df_ticket").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'max_price': [df_ticket['price'].max()]}))

p("=== MIN with ALIAS ===")
p("SQL:", duckdb.sql("SELECT MIN(km) AS shortest_distance FROM df_running_distance").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'shortest_distance': [df_running_distance['km'].min()]}))

p("=== AVG - Find average value ===")
p("SQL:", duckdb.sql("SELECT AVG(price) FROM df_ticket").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'avg_price': [df_ticket['price'].mean()]}))

p("=== AVG with ALIAS ===")
p("SQL:", duckdb.sql("SELECT AVG(price) AS average_price FROM df_ticket").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'average_price': [df_ticket['price'].mean()]}))

p("=== COUNT - Count all rows ===")
p("SQL:", duckdb.sql("SELECT COUNT(*) FROM df_wishlist").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'count': [len(df_wishlist)]}))

p("=== COUNT with ALIAS ===")
p("SQL:", duckdb.sql("SELECT COUNT(*) AS items FROM df_wishlist").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'items': [len(df_wishlist)]}))

p("=== COUNT specific column ===")
p("SQL:", duckdb.sql("SELECT COUNT(email) FROM df_orders").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'count_email': [df_orders['email'].count()]}))

p("=== COUNT DISTINCT ===")
p("SQL:", duckdb.sql("SELECT COUNT(DISTINCT item) FROM df_wishlist").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'distinct_items': [df_wishlist['item'].nunique()]}))

p("=== SUM - Sum values ===")
p("SQL:", duckdb.sql("SELECT SUM(price) FROM df_wishlist").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'total_price': [df_wishlist['price'].sum()]}))

p("=== SUM with ALIAS ===")
p("SQL:", duckdb.sql("SELECT SUM(price) AS total_price FROM df_wishlist").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'total_price': [df_wishlist['price'].sum()]}))

p("=== GROUP BY with COUNT ===")
p("SQL:", duckdb.sql("SELECT grade, COUNT(*) FROM df_test GROUP BY grade").df())
p("-----------------------------------")
p("Pandas:", df_test.groupby('grade').size().reset_index(name='count'))

p("=== GROUP BY with COUNT and ALIAS ===")
p("SQL:", duckdb.sql("SELECT grade, COUNT(*) AS students FROM df_test GROUP BY grade").df())
p("-----------------------------------")
p("Pandas:", df_test.groupby('grade').size().reset_index(name='students'))

p("=== GROUP BY multiple columns ===")
p("SQL:", duckdb.sql("SELECT country, city, COUNT(*) AS user_count FROM df_user GROUP BY country, city").df())
p("-----------------------------------")
p("Pandas:", df_user.groupby(['country', 'city']).size().reset_index(name='user_count'))

p("=== GROUP BY with AVG ===")
p("SQL:", duckdb.sql("SELECT country, AVG(age) AS average_age FROM df_user GROUP BY country").df())
p("-----------------------------------")
p("Pandas:", df_user.groupby('country')['age'].mean().reset_index(name='average_age'))

p("=== GROUP BY with SUM ===")
p("SQL:", duckdb.sql("SELECT category, SUM(amount) FROM df_sales GROUP BY category").df())
p("-----------------------------------")
p("Pandas:", df_sales.groupby('category')['amount'].sum().reset_index())

p("=== HAVING - Filter groups ===")
p("SQL:", duckdb.sql("SELECT grade, COUNT(*) AS students FROM df_test GROUP BY grade HAVING COUNT(*) > 1").df())
p("-----------------------------------")
grouped = df_test.groupby('grade').size().reset_index(name='students')
p("Pandas:", grouped[grouped['students'] > 1])

p("=== HAVING with column condition ===")
p("SQL:", duckdb.sql("SELECT grade, COUNT(*) AS students FROM df_test GROUP BY grade HAVING grade <> 'A'").df())
p("-----------------------------------")
grouped = df_test.groupby('grade').size().reset_index(name='students')
p("Pandas:", grouped[grouped['grade'] != 'A'])

p("=== HAVING with pattern matching ===")
p("SQL:", duckdb.sql("SELECT country, COUNT(*) AS users FROM df_user GROUP BY country HAVING country LIKE 'E%'").df())
p("-----------------------------------")
grouped = df_user.groupby('country').size().reset_index(name='users')
p("Pandas:", grouped[grouped['country'].str.startswith('E')])

p("=== WHERE with GROUP BY ===")
p("SQL:", duckdb.sql("SELECT category, COUNT(*) FROM df_wishlist WHERE category LIKE 's%' GROUP BY category").df())
p("-----------------------------------")
filtered = df_wishlist[df_wishlist['category'].str.startswith('s')]
p("Pandas:", filtered.groupby('category').size().reset_index(name='count'))

p("=== COUNT with WHERE ===")
p("SQL:", duckdb.sql("SELECT COUNT(country) FROM df_user WHERE country = 'England'").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'count': [df_user[df_user['country'] == 'England']['country'].count()]}))

p("=== MAX with ALIAS ===")
p("SQL:", duckdb.sql("SELECT MAX(price) AS max_price FROM df_coffee").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'max_price': [df_coffee['price'].max()]}))

p("=== SUM with ALIAS ===")
p("SQL:", duckdb.sql("SELECT SUM(hours) AS duration FROM df_project_time").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'duration': [df_project_time['hours'].sum()]}))

p("=== COUNT DISTINCT with ALIAS ===")
p("SQL:", duckdb.sql("SELECT COUNT(DISTINCT employee) AS unique_employees FROM df_project_time").df())
p("-----------------------------------")
p("Pandas:", pd.DataFrame({'unique_employees': [df_project_time['employee'].nunique()]}))