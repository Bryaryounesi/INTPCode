import duckdb
import pandas as pd
p = print
# Read all sheets from Excel file
file_path = r'e:\python\INTPCode\DuckDB with Pandas\database2.xlsx'
all_sheets = pd.read_excel(file_path, sheet_name=None)

df_orders = all_sheets['orders']
df_reservation = all_sheets['reservation']
df_flights = all_sheets['flights']
df_songs = all_sheets['songs']
df_employees = all_sheets['employees']
df_students = all_sheets['students']

p("=== INSERT INTO - Add new data ===")
p("SQL: DuckDB not useful for INSERT")
p("Raw SQL: INSERT INTO orders (name, id, price) VALUES ('Teddy bear', 6574, 13)")
p("-----------------------------------")
df_orders.loc[len(df_orders)] = ['Teddy bear', 6574, 13]
p("Pandas:", df_orders.tail(1))
p()

p("=== DELETE with condition ===")
p("SQL: DuckDB not useful for DELETE")
p("Raw SQL: DELETE FROM orders WHERE price < 10")
p("-----------------------------------")
df_orders.query("price >= 10", inplace=True)
p("Pandas:", df_orders)
p()

p("=== UPDATE with condition ===")
p("SQL: DuckDB not useful for UPDATE")
p("Raw SQL: UPDATE reservation SET time = '19:00' WHERE name = 'Smith'")
p("-----------------------------------")
df_reservation.loc[df_reservation['name'] == 'Smith', 'time'] = '19:00'
p("Pandas:", df_reservation.query("name == 'Smith'"))
p()

p("=== UPDATE all rows ===")
p("SQL: DuckDB not useful for UPDATE")
p("Raw SQL: UPDATE employees SET salary = 5000")
p("-----------------------------------")
df_employees['salary'] = 5000
p("Pandas:", df_employees.head())
p()

p("=== SELECT with DISTINCT ===")
p("SQL:", duckdb.sql("SELECT DISTINCT major FROM df_students").df())
p("-----------------------------------")
p("Pandas:", df_students['major'].drop_duplicates())
p()

p("=== WHERE with AND ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' AND year = 1").df())
p("-----------------------------------")
p("Pandas:", df_students.query("major == 'Biology' and year == 1"))
p()

p("=== WHERE with OR ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' OR major = 'Math'").df())
p("-----------------------------------")
p("Pandas:", df_students.query("major == 'Biology' or major == 'Math'"))
p()

p("=== ORDER BY ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students ORDER BY score DESC").df())
p("-----------------------------------")
p("Pandas:", df_students.sort_values('score', ascending=False))
p()

p("=== LIMIT ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students LIMIT 3").df())
p("-----------------------------------")
p("Pandas:", df_students.head(3))
p()

p("=== WHERE with ORDER BY ===")
p("SQL:", duckdb.sql("SELECT * FROM df_students WHERE year = 1 ORDER BY score DESC").df())
p("-----------------------------------")
p("Pandas:", df_students.query("year == 1").sort_values('score', ascending=False))
p()

p("=== ALTER TABLE - ADD COLUMN ===")
p("SQL: DuckDB not useful for ALTER")
p("Raw SQL: ALTER TABLE orders ADD discount INT")
p("-----------------------------------")
df_orders['discount'] = None
p("Pandas - New column added")
p()

p("=== ALTER TABLE - RENAME COLUMN ===")
p("SQL: DuckDB not useful for ALTER")
p("Raw SQL: ALTER TABLE orders RENAME price TO bill")
p("-----------------------------------")
df_orders.rename(columns={'price': 'bill'}, inplace=True)
p("Pandas - Column renamed")
p()

p("=== ALTER TABLE - DROP COLUMN ===")
p("SQL: DuckDB not useful for ALTER")
p("Raw SQL: ALTER TABLE orders DROP COLUMN discount")
p("-----------------------------------")
df_orders.drop(columns=['discount'], inplace=True)
p("Pandas - Column dropped")
p()

p("=== CREATE TABLE ===")
p("SQL: DuckDB not useful for CREATE")
p("Raw SQL: CREATE TABLE directory (floor INTEGER, company TEXT)")
p("-----------------------------------")
new_table = pd.DataFrame({'floor': pd.Series(dtype='int'), 'company': pd.Series(dtype='str')})
p("Pandas - New table created")
p()

p("=== DROP TABLE ===")
p("SQL: DuckDB not useful for DROP")
p("Raw SQL: DROP TABLE past_events")
p("-----------------------------------")
p("Pandas: Tables not directly dropped in Pandas")
p()