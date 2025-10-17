import duckdb
import pandas as pd

# Read all sheets from Excel file
file_path = r'e:\python\INTPCode\DuckDB with Pandas\database2.xlsx'
all_sheets = pd.read_excel(file_path, sheet_name=None)

df_orders = all_sheets['orders']
df_reservation = all_sheets['reservation']
df_flights = all_sheets['flights']
df_songs = all_sheets['songs']
df_employees = all_sheets['employees']
df_students = all_sheets['students']

print("=== INSERT INTO - Add new data ===")
print("SQL: DuckDB not useful for INSERT")
print("Raw SQL: INSERT INTO orders (name, id, price) VALUES ('Teddy bear', 6574, 13)")
print("-----------------------------------")
df_orders.loc[len(df_orders)] = ['Teddy bear', 6574, 13]
print("Pandas:", df_orders.tail(1))
print()

print("=== DELETE with condition ===")
print("SQL: DuckDB not useful for DELETE")
print("Raw SQL: DELETE FROM orders WHERE price < 10")
print("-----------------------------------")
df_orders.query("price >= 10", inplace=True)
print("Pandas:", df_orders)
print()

print("=== UPDATE with condition ===")
print("SQL: DuckDB not useful for UPDATE")
print("Raw SQL: UPDATE reservation SET time = '19:00' WHERE name = 'Smith'")
print("-----------------------------------")
df_reservation.loc[df_reservation['name'] == 'Smith', 'time'] = '19:00'
print("Pandas:", df_reservation.query("name == 'Smith'"))
print()

print("=== UPDATE all rows ===")
print("SQL: DuckDB not useful for UPDATE")
print("Raw SQL: UPDATE employees SET salary = 5000")
print("-----------------------------------")
df_employees['salary'] = 5000
print("Pandas:", df_employees.head())
print()

print("=== SELECT with DISTINCT ===")
print("SQL:", duckdb.sql("SELECT DISTINCT major FROM df_students").df())
print("-----------------------------------")
print("Pandas:", df_students['major'].drop_duplicates())
print()

print("=== WHERE with AND ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' AND year = 1").df())
print("-----------------------------------")
print("Pandas:", df_students.query("major == 'Biology' and year == 1"))
print()

print("=== WHERE with OR ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' OR major = 'Math'").df())
print("-----------------------------------")
print("Pandas:", df_students.query("major == 'Biology' or major == 'Math'"))
print()

print("=== ORDER BY ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students ORDER BY score DESC").df())
print("-----------------------------------")
print("Pandas:", df_students.sort_values('score', ascending=False))
print()

print("=== LIMIT ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students LIMIT 3").df())
print("-----------------------------------")
print("Pandas:", df_students.head(3))
print()

print("=== WHERE with ORDER BY ===")
print("SQL:", duckdb.sql("SELECT * FROM df_students WHERE year = 1 ORDER BY score DESC").df())
print("-----------------------------------")
print("Pandas:", df_students.query("year == 1").sort_values('score', ascending=False))
print()

print("=== ALTER TABLE - ADD COLUMN ===")
print("SQL: DuckDB not useful for ALTER")
print("Raw SQL: ALTER TABLE orders ADD discount INT")
print("-----------------------------------")
df_orders['discount'] = None
print("Pandas - New column added")
print()

print("=== ALTER TABLE - RENAME COLUMN ===")
print("SQL: DuckDB not useful for ALTER")
print("Raw SQL: ALTER TABLE orders RENAME price TO bill")
print("-----------------------------------")
df_orders.rename(columns={'price': 'bill'}, inplace=True)
print("Pandas - Column renamed")
print()

print("=== ALTER TABLE - DROP COLUMN ===")
print("SQL: DuckDB not useful for ALTER")
print("Raw SQL: ALTER TABLE orders DROP COLUMN discount")
print("-----------------------------------")
df_orders.drop(columns=['discount'], inplace=True)
print("Pandas - Column dropped")
print()

print("=== CREATE TABLE ===")
print("SQL: DuckDB not useful for CREATE")
print("Raw SQL: CREATE TABLE directory (floor INTEGER, company TEXT)")
print("-----------------------------------")
new_table = pd.DataFrame({'floor': pd.Series(dtype='int'), 'company': pd.Series(dtype='str')})
print("Pandas - New table created")
print()

print("=== DROP TABLE ===")
print("SQL: DuckDB not useful for DROP")
print("Raw SQL: DROP TABLE past_events")
print("-----------------------------------")
print("Pandas: Tables not directly dropped in Pandas")
print()