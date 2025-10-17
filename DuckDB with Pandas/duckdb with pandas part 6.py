import duckdb
import pandas as pd
p = print
# Read all sheets from Excel file
file_path = r'e:\python\INTPCode\DuckDB with Pandas\database6.xlsx'
all_sheets = pd.read_excel(file_path, sheet_name=None)

df_customers = all_sheets['customers']
df_employees = all_sheets['employees']
df_orders = all_sheets['orders']
df_products = all_sheets['products']
df_departments = all_sheets['departments']
df_students = all_sheets['students']
df_mario_games = all_sheets['mario_games']
df_snack = all_sheets['snack']
df_macros = all_sheets['macros']

p("----------------------------------------")
p("=== Scalar Subquery - Customers older than average ===")
p("SQL:", duckdb.sql("SELECT first_name, last_name, email FROM df_customers WHERE age > (SELECT AVG(age) FROM df_customers)").df())
p("-----------------------------------")
avg_age = df_customers['age'].mean()
p("Pandas:", df_customers[df_customers['age'] > avg_age][['first_name', 'last_name', 'email']])

p("----------------------------------------")
p("=== Scalar Subquery - Employees with minimum salary ===")
p("SQL:", duckdb.sql("SELECT employee_name FROM df_employees WHERE salary = (SELECT MIN(salary) FROM df_employees)").df())
p("-----------------------------------")
min_salary = df_employees['salary'].min()
p("Pandas:", df_employees[df_employees['salary'] == min_salary][['employee_name']])

p("----------------------------------------")
p("=== Scalar Subquery - Orders above average amount ===")
p("SQL:", duckdb.sql("SELECT order_id, total_amount FROM df_orders WHERE total_amount > (SELECT AVG(total_amount) FROM df_orders)").df())
p("-----------------------------------")
avg_amount = df_orders['total_amount'].mean()
p("Pandas:", df_orders[df_orders['total_amount'] > avg_amount][['order_id', 'total_amount']])

p("----------------------------------------")
p("=== Scalar Subquery - Products with maximum price ===")
p("SQL:", duckdb.sql("SELECT product_name, price FROM df_products WHERE price = (SELECT MAX(price) FROM df_products)").df())
p("-----------------------------------")
max_price = df_products['price'].max()
p("Pandas:", df_products[df_products['price'] == max_price][['product_name', 'price']])

p("----------------------------------------")
p("=== Subquery with IN - Customers with orders ===")
p("SQL:", duckdb.sql("SELECT first_name, last_name FROM df_customers WHERE id IN (SELECT customer_id FROM df_orders)").df())
p("-----------------------------------")
customers_with_orders = df_customers[df_customers['id'].isin(df_orders['customer_id'])][['first_name', 'last_name']]
p("Pandas:", customers_with_orders)

p("----------------------------------------")
p("=== Subquery with IN - Employees in high budget departments ===")
p("SQL:", duckdb.sql("SELECT * FROM df_employees WHERE department_id IN (SELECT department_id FROM df_departments WHERE budget > 2000)").df())
p("-----------------------------------")
high_budget_depts = df_departments[df_departments['budget'] > 2000]['department_id']
employees_high_budget = df_employees[df_employees['department_id'].isin(high_budget_depts)]
p("Pandas:", employees_high_budget)

p("----------------------------------------")
p("=== Scalar Subquery - Latest Mario game ===")
p("SQL:", duckdb.sql("SELECT name FROM df_mario_games WHERE release = (SELECT MAX(release) FROM df_mario_games)").df())
p("-----------------------------------")
latest_release = df_mario_games['release'].max()
p("Pandas:", df_mario_games[df_mario_games['release'] == latest_release][['name']])

p("----------------------------------------")
p("=== Scalar Subquery - Oldest Mario game ===")
p("SQL:", duckdb.sql("SELECT name FROM df_mario_games WHERE release = (SELECT MIN(release) FROM df_mario_games)").df())
p("-----------------------------------")
oldest_release = df_mario_games['release'].min()
p("Pandas:", df_mario_games[df_mario_games['release'] == oldest_release][['name']])

p("----------------------------------------")
p("=== Scalar Subquery - Games released after average ===")
p("SQL:", duckdb.sql("SELECT name FROM df_mario_games WHERE release > (SELECT AVG(release) FROM df_mario_games)").df())
p("-----------------------------------")
avg_release = df_mario_games['release'].mean()
p("Pandas:", df_mario_games[df_mario_games['release'] > avg_release][['name']])

p("----------------------------------------")
p("=== Subquery from different table - Apple macros ===")
p("SQL:", duckdb.sql("SELECT * FROM df_macros WHERE id = (SELECT id FROM df_snack WHERE name = 'apple')").df())
p("-----------------------------------")
apple_id = df_snack[df_snack['name'] == 'apple']['id'].iloc[0] if not df_snack[df_snack['name'] == 'apple'].empty else None
if apple_id:
    apple_macros = df_macros[df_macros['id'] == apple_id]
    p("Pandas:", apple_macros)
else:
    p("Pandas: Apple not found")

p("----------------------------------------")
p("=== Subquery with IN - Employees in Marketing or Sales ===")
p("SQL:", duckdb.sql("SELECT * FROM df_employees WHERE department_id IN (SELECT department_id FROM df_departments WHERE department_name = 'Marketing' OR department_name = 'Sales')").df())
p("-----------------------------------")
marketing_sales_depts = df_departments[
    (df_departments['department_name'] == 'Marketing') | 
    (df_departments['department_name'] == 'Sales')
]['department_id']
employees_marketing_sales = df_employees[df_employees['department_id'].isin(marketing_sales_depts)]
p("Pandas:", employees_marketing_sales)

p("----------------------------------------")
p("=== Subquery with NOT IN - Employees without department ===")
p("SQL:", duckdb.sql("SELECT * FROM df_employees WHERE department_id NOT IN (SELECT department_id FROM df_departments)").df())
p("-----------------------------------")
all_dept_ids = df_departments['department_id']
employees_no_dept = df_employees[~df_employees['department_id'].isin(all_dept_ids)]
p("Pandas:", employees_no_dept)