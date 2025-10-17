import duckdb
import pandas as pd
p = print
# Read all sheets from Excel file
file_path = r'e:\python\INTPCode\DuckDB with Pandas\database5.xlsx'
all_sheets = pd.read_excel(file_path, sheet_name=None)

df_student = all_sheets['student']
df_enrolled = all_sheets['enrolled']
df_artist = all_sheets['artist']
df_album = all_sheets['album']
df_courses = all_sheets['courses']
df_booking_requests = all_sheets['booking_requests']
df_hotels = all_sheets['hotels']
df_user = all_sheets['user']
df_blocked = all_sheets['blocked']
df_menu = all_sheets['menu']
df_unavailable_items = all_sheets['unavailable_items']
df_stores = all_sheets['stores']
df_production = all_sheets['production']
df_movie = all_sheets['movie']
df_director = all_sheets['director']
df_warehouses = all_sheets['warehouses']
df_ordered_books = all_sheets['ordered_books']
df_writers = all_sheets['writers']

p("-----------------------------------")
p("=== INNER JOIN - Basic join ===")
p("SQL:", duckdb.sql("SELECT * FROM df_student INNER JOIN df_enrolled ON df_student.id = df_enrolled.student_id").df())
p("-----------------------------------")
p("Pandas:", pd.merge(df_student, df_enrolled, left_on='id', right_on='student_id', how='inner'))

p("=== INNER JOIN - Different column names ===")
p("SQL:", duckdb.sql("SELECT * FROM df_artist INNER JOIN df_album ON df_artist.id = df_album.artist_id").df())
p("-----------------------------------")
p("Pandas:", pd.merge(df_artist, df_album, left_on='id', right_on='artist_id', how='inner'))

p("=== INNER JOIN - Select specific columns ===")
p("SQL:", duckdb.sql("SELECT df_student.name, df_enrolled.class FROM df_student INNER JOIN df_enrolled ON df_student.id = df_enrolled.student_id").df())
p("-----------------------------------")
result = pd.merge(df_student, df_enrolled, left_on='id', right_on='student_id', how='inner')
p("Pandas:", result[['name', 'class']])

p("=== INNER JOIN - Multiple columns selection ===")
p("SQL:", duckdb.sql("SELECT df_artist.id, df_artist.name, df_album.title FROM df_artist INNER JOIN df_album ON df_artist.id = df_album.artist_id").df())
p("-----------------------------------")
result = pd.merge(df_artist, df_album, left_on='id', right_on='artist_id', how='inner')
p("Pandas:", result[['id', 'name', 'title']])

p("=== INNER JOIN - Column aliasing ===")
p("SQL:", duckdb.sql("SELECT df_student.name AS student, df_enrolled.class FROM df_student INNER JOIN df_enrolled ON df_student.id = df_enrolled.student_id").df())
p("-----------------------------------")
result = pd.merge(df_student, df_enrolled, left_on='id', right_on='student_id', how='inner')
p("Pandas:", result[['name', 'class']].rename(columns={'name': 'student'}))

p("=== INNER JOIN - Table aliasing ===")
p("SQL:", duckdb.sql("SELECT s.name, e.class FROM df_student AS s INNER JOIN df_enrolled AS e ON s.id = e.student_id").df())
p("-----------------------------------")
result = pd.merge(df_student, df_enrolled, left_on='id', right_on='student_id', how='inner')
p("Pandas:", result[['name', 'class']])

p("=== INNER JOIN - Table and column aliasing ===")
p("SQL:", duckdb.sql("SELECT art.name AS artist, alb.title AS album FROM df_artist AS art INNER JOIN df_album AS alb ON art.id = alb.artist_id").df())
p("-----------------------------------")
result = pd.merge(df_artist, df_album, left_on='id', right_on='artist_id', how='inner')
p("Pandas:", result[['name', 'title']].rename(columns={'name': 'artist', 'title': 'album'}))

p("=== LEFT JOIN - Basic left join ===")
p("SQL:", duckdb.sql("SELECT * FROM df_student LEFT JOIN df_enrolled ON df_student.id = df_enrolled.student_id").df())
p("-----------------------------------")
p("Pandas:", pd.merge(df_student, df_enrolled, left_on='id', right_on='student_id', how='left'))

p("=== LEFT JOIN - Select specific columns ===")
p("SQL:", duckdb.sql("SELECT df_student.name, df_enrolled.class FROM df_student LEFT JOIN df_enrolled ON df_student.id = df_enrolled.student_id").df())
p("-----------------------------------")
result = pd.merge(df_student, df_enrolled, left_on='id', right_on='student_id', how='left')
p("Pandas:", result[['name', 'class']])

p("=== LEFT JOIN - With table aliasing ===")
p("SQL:", duckdb.sql("SELECT s.name, e.class FROM df_student AS s LEFT JOIN df_enrolled AS e ON s.id = e.student_id").df())
p("-----------------------------------")
result = pd.merge(df_student, df_enrolled, left_on='id', right_on='student_id', how='left')
p("Pandas:", result[['name', 'class']])

p("=== LEFT JOIN - Artist and album example ===")
p("SQL:", duckdb.sql("SELECT a.name AS artist, alb.title AS album FROM df_artist AS a LEFT JOIN df_album AS alb ON a.id = alb.artist_id").df())
p("-----------------------------------")
result = pd.merge(df_artist, df_album, left_on='id', right_on='artist_id', how='left')
p("Pandas:", result[['name', 'title']].rename(columns={'name': 'artist', 'title': 'album'}))

p("=== RIGHT JOIN - Basic right join ===")
p("SQL:", duckdb.sql("SELECT * FROM df_courses RIGHT JOIN df_student ON df_student.course_id = df_courses.student_id").df())
p("-----------------------------------")
p("Pandas:", pd.merge(df_courses, df_student, left_on='student_id', right_on='course_id', how='right'))

p("=== RIGHT JOIN - Hotels and booking example ===")
p("SQL:", duckdb.sql("SELECT * FROM df_booking_requests RIGHT JOIN df_hotels ON df_hotels.location = df_booking_requests.client_destination").df())
p("-----------------------------------")
p("Pandas:", pd.merge(df_booking_requests, df_hotels, left_on='client_destination', right_on='location', how='right'))

p("=== FULL OUTER JOIN - Basic full join ===")
p("SQL:", duckdb.sql("SELECT * FROM df_user FULL OUTER JOIN df_blocked ON df_blocked.id = df_user.id").df())
p("-----------------------------------")
p("Pandas:", pd.merge(df_user, df_blocked, left_on='id', right_on='id', how='outer'))

p("=== FULL OUTER JOIN - Menu example ===")
p("SQL:", duckdb.sql("SELECT * FROM df_menu FULL OUTER JOIN df_unavailable_items ON df_menu.name = df_unavailable_items.name").df())
p("-----------------------------------")
p("Pandas:", pd.merge(df_menu, df_unavailable_items, left_on='name', right_on='name', how='outer'))

p("=== FULL OUTER JOIN - Stores and production ===")
p("SQL:", duckdb.sql("SELECT * FROM df_stores FULL OUTER JOIN df_production ON df_stores.id = df_production.store_id").df())
p("-----------------------------------")
p("Pandas:", pd.merge(df_stores, df_production, left_on='id', right_on='store_id', how='outer'))

p("=== INNER JOIN - Movie and director ===")
p("SQL:", duckdb.sql("SELECT m.title, d.name FROM df_movie AS m INNER JOIN df_director AS d ON m.director_id = d.id").df())
p("-----------------------------------")
result = pd.merge(df_movie, df_director, left_on='director_id', right_on='id', how='inner')
p("Pandas:", result[['title', 'name']])

p("=== RIGHT JOIN - Warehouses and stores ===")
p("SQL:", duckdb.sql("SELECT * FROM df_warehouses RIGHT JOIN df_stores ON df_stores.location = df_warehouses.location").df())
p("-----------------------------------")
p("Pandas:", pd.merge(df_warehouses, df_stores, left_on='location', right_on='location', how='right'))

p("=== LEFT JOIN - Ordered books and writers ===")
p("SQL:", duckdb.sql("SELECT * FROM df_ordered_books LEFT JOIN df_writers ON df_writers.name = df_ordered_books.author").df())
p("-----------------------------------")
p("Pandas:", pd.merge(df_ordered_books, df_writers, left_on='author', right_on='name', how='left'))

p("=== FULL OUTER JOIN - Ordered books first ===")
p("SQL:", duckdb.sql("SELECT * FROM df_ordered_books FULL OUTER JOIN df_writers ON df_writers.name = df_ordered_books.author").df())
p("-----------------------------------")
p("Pandas:", pd.merge(df_ordered_books, df_writers, left_on='author', right_on='name', how='outer'))