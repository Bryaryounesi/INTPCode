from typing import Any

# ============================================================
# duckdb.pyi — DuckDB SQL Queries with Pandas Equivalents
# راهنما: همه توابع زیر فقط برای هاور موس هستند.
# فرم درست: duckdb.sql("کوئری SQL")
# ============================================================

def sql(query: str) -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df")
    📌 پارامترها: query = کوئری SQL به صورت رشته
    """
    ...

# ============================================================
# ۱. SELECT — انتخاب ستون‌ها
# ============================================================

def sql_select_one_column() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT name FROM df_users")
    📌 Pandas: df_users[['name']]
    """
    ...

def sql_select_multiple_columns() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT name, email FROM df_users")
    📌 Pandas: df_users[['name', 'email']]
    """
    ...

def sql_select_all() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_users")
    📌 Pandas: df_users
    """
    ...

def sql_distinct() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT DISTINCT type FROM df_membership")
    📌 Pandas: df_membership[['type']].drop_duplicates()
    """
    ...

# ============================================================
# ۲. ORDER BY — مرتب‌سازی
# ============================================================

def sql_order_by_asc() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_patients ORDER BY name")
    📌 Pandas: df_patients.sort_values('name')
    """
    ...

def sql_order_by_desc() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_patients ORDER BY age DESC")
    📌 Pandas: df_patients.sort_values('age', ascending=False)
    """
    ...

def sql_order_by_multiple() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students ORDER BY major, score DESC")
    📌 Pandas: df_students.sort_values(['major', 'score'], ascending=[True, False])
    """
    ...

# ============================================================
# ۳. WHERE — فیلتر کردن
# ============================================================

def sql_where_text() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology'")
    📌 Pandas: df_students.query("major == 'Biology'")
    """
    ...

def sql_where_number() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students WHERE year = 1")
    📌 Pandas: df_students.query("year == 1")
    """
    ...

def sql_where_not_equal() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students WHERE major <> 'Biology'")
    📌 Pandas: df_students.query("major != 'Biology'")
    """
    ...

def sql_where_less_than() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_chocolate WHERE price < 2")
    📌 Pandas: df_chocolate.query("price < 2")
    """
    ...

def sql_where_greater_than() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_chocolate WHERE price > 2")
    📌 Pandas: df_chocolate.query("price > 2")
    """
    ...

def sql_where_less_equal() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_chocolate WHERE price <= 2")
    📌 Pandas: df_chocolate.query("price <= 2")
    """
    ...

def sql_where_greater_equal() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_chocolate WHERE price >= 2")
    📌 Pandas: df_chocolate.query("price >= 2")
    """
    ...

def sql_where_select_columns() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT name, score FROM df_students WHERE year = 1")
    📌 Pandas: df_students.query("year == 1")[['name', 'score']]
    """
    ...

# ============================================================
# ۴. BETWEEN — فیلتر بازه‌ای
# ============================================================

def sql_between() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_movies WHERE rating BETWEEN 9 AND 10")
    📌 Pandas: df_movies.query("rating >= 9 and rating <= 10")
    """
    ...

def sql_between_age() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_patients WHERE age BETWEEN 20 AND 30")
    📌 Pandas: df_patients.query("age >= 20 and age <= 30")
    """
    ...

def sql_not_between() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_inventory WHERE year NOT BETWEEN 1950 AND 1970")
    📌 Pandas: df_inventory.query("year < 1950 or year > 1970")
    """
    ...

# ============================================================
# ۵. LIKE — تطبیق الگو
# ============================================================

def sql_like_starts_with() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_writers WHERE first_name LIKE 'a%'")
    📌 Pandas: df_writers[df_writers['first_name'].str.startswith('a')]
    """
    ...

def sql_like_ends_with() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_users WHERE email LIKE '%.uk'")
    📌 Pandas: df_users[df_users['email'].str.endswith('.uk')]
    """
    ...

def sql_like_contains() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_users WHERE email LIKE '%gmail%'")
    📌 Pandas: df_users[df_users['email'].str.contains('gmail')]
    """
    ...

def sql_not_like() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students WHERE name NOT LIKE 'a%'")
    📌 Pandas: df_students[~df_students['name'].str.startswith('a')]
    """
    ...

# ============================================================
# ۶. IN — فیلتر با گزینه‌ها
# ============================================================

def sql_in_text() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_customers WHERE country IN ('France', 'Germany')")
    📌 Pandas: df_customers[df_customers['country'].isin(['France', 'Germany'])]
    """
    ...

def sql_in_number() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_restaurants WHERE rating IN (3, 5)")
    📌 Pandas: df_restaurants[df_restaurants['rating'].isin([3, 5])]
    """
    ...

def sql_not_in() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students WHERE major NOT IN ('History', 'Physics')")
    📌 Pandas: df_students[~df_students['major'].isin(['History', 'Physics'])]
    """
    ...

# ============================================================
# ۷. AND / OR — ترکیب شرط‌ها
# ============================================================

def sql_and() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' AND year = 1")
    📌 Pandas: df_students.query("major == 'Biology' and year == 1")
    """
    ...

def sql_or() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' OR major = 'Math'")
    📌 Pandas: df_students.query("major == 'Biology' or major == 'Math'")
    """
    ...

def sql_and_between() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students WHERE major = 'Biology' AND year BETWEEN 2 AND 4")
    📌 Pandas: df_students.query("major == 'Biology' and year >= 2 and year <= 4")
    """
    ...

def sql_and_like() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_inventory WHERE year BETWEEN 1950 AND 1960 AND manufacturer LIKE 'f%'")
    📌 Pandas: df_filtered = df_inventory.query("year >= 1950 and year <= 1960")
              df_filtered[df_filtered['manufacturer'].str.startswith('f')]
    """
    ...

def sql_or_in() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_inventory WHERE ID BETWEEN 1 AND 3 OR manufacturer IN ('Jaguar', 'Ford')")
    📌 Pandas: df_inventory.query("(ID >= 1 and ID <= 3) or manufacturer in ['Jaguar', 'Ford']")
    """
    ...

def sql_complex_condition() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students WHERE (major = 'Biology' AND score > 80) OR (major = 'Math' AND score > 90)")
    📌 Pandas: df_students.query("(major == 'Biology' and score > 80) or (major == 'Math' and score > 90)")
    """
    ...

# ============================================================
# ۸. AS — تغییر نام ستون
# ============================================================

def sql_as_single() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT name AS student_name, major AS field FROM df_students")
    📌 Pandas: df_students[['name', 'major']].rename(columns={'name': 'student_name', 'major': 'field'})
    """
    ...

def sql_as_with_where() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT name AS student, score FROM df_students WHERE score = 9")
    📌 Pandas: df_students[['name', 'score']].rename(columns={'name': 'student'}).query("score == 9")
    """
    ...

# ============================================================
# ۹. LIMIT — محدود کردن نتایج
# ============================================================

def sql_limit_with_order() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students ORDER BY score DESC LIMIT 2")
    📌 Pandas: df_students.nlargest(2, 'score')
    """
    ...

def sql_limit_simple() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students LIMIT 3")
    📌 Pandas: df_students.head(3)
    """
    ...

def sql_where_order_by() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_students WHERE year = 1 ORDER BY score DESC")
    📌 Pandas: df_students.query("year == 1").sort_values('score', ascending=False)
    """
    ...

# ============================================================
# ۱۰. توابع تجمعی — MIN, MAX, AVG, COUNT, SUM
# ============================================================

def sql_min() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT MIN(price) FROM df_ticket")
    📌 Pandas: df_ticket['price'].min()
    """
    ...

def sql_max() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT MAX(price) FROM df_ticket")
    📌 Pandas: df_ticket['price'].max()
    """
    ...

def sql_avg() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT AVG(price) FROM df_ticket")
    📌 Pandas: df_ticket['price'].mean()
    """
    ...

def sql_count() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT COUNT(*) FROM df_wishlist")
    📌 Pandas: len(df_wishlist)
    """
    ...

def sql_count_column() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT COUNT(email) FROM df_orders")
    📌 Pandas: df_orders['email'].count()
    """
    ...

def sql_count_distinct() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT COUNT(DISTINCT item) FROM df_wishlist")
    📌 Pandas: df_wishlist['item'].nunique()
    """
    ...

def sql_sum() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT SUM(price) FROM df_wishlist")
    📌 Pandas: df_wishlist['price'].sum()
    """
    ...

# ============================================================
# ۱۱. GROUP BY — گروه‌بندی
# ============================================================

def sql_group_by_count() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT grade, COUNT(*) FROM df_test GROUP BY grade")
    📌 Pandas: df_test.groupby('grade').size().reset_index(name='count')
    """
    ...

def sql_group_by_avg() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT country, AVG(age) AS average_age FROM df_user GROUP BY country")
    📌 Pandas: df_user.groupby('country')['age'].mean().reset_index(name='average_age')
    """
    ...

def sql_group_by_multiple() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT country, city, COUNT(*) AS user_count FROM df_user GROUP BY country, city")
    📌 Pandas: df_user.groupby(['country', 'city']).size().reset_index(name='user_count')
    """
    ...

def sql_group_by_sum() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT category, SUM(amount) FROM df_sales GROUP BY category")
    📌 Pandas: df_sales.groupby('category')['amount'].sum().reset_index()
    """
    ...

# ============================================================
# ۱۲. HAVING — فیلتر گروه‌ها
# ============================================================

def sql_having_count() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT grade, COUNT(*) AS students FROM df_test GROUP BY grade HAVING COUNT(*) > 1")
    📌 Pandas: grouped = df_test.groupby('grade').size().reset_index(name='students')
              grouped[grouped['students'] > 1]
    """
    ...

def sql_having_column() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT grade, COUNT(*) AS students FROM df_test GROUP BY grade HAVING grade <> 'A'")
    📌 Pandas: grouped = df_test.groupby('grade').size().reset_index(name='students')
              grouped[grouped['grade'] != 'A']
    """
    ...

def sql_having_like() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT country, COUNT(*) AS users FROM df_user GROUP BY country HAVING country LIKE 'E%'")
    📌 Pandas: grouped = df_user.groupby('country').size().reset_index(name='users')
              grouped[grouped['country'].str.startswith('E')]
    """
    ...

def sql_where_group_by() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT category, COUNT(*) FROM df_wishlist WHERE category LIKE 's%' GROUP BY category")
    📌 Pandas: filtered = df_wishlist[df_wishlist['category'].str.startswith('s')]
              filtered.groupby('category').size().reset_index(name='count')
    """
    ...

# ============================================================
# ۱۳. JOIN — اتصال جداول
# ============================================================

def sql_inner_join() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_student INNER JOIN df_enrolled ON df_student.id = df_enrolled.student_id")
    📌 Pandas: pd.merge(df_student, df_enrolled, left_on='id', right_on='student_id', how='inner')
    """
    ...

def sql_inner_join_columns() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT df_student.name, df_enrolled.class FROM df_student INNER JOIN df_enrolled ON df_student.id = df_enrolled.student_id")
    📌 Pandas: result = pd.merge(df_student, df_enrolled, left_on='id', right_on='student_id', how='inner')
              result[['name', 'class']]
    """
    ...

def sql_inner_join_alias() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT s.name, e.class FROM df_student AS s INNER JOIN df_enrolled AS e ON s.id = e.student_id")
    📌 Pandas: result = pd.merge(df_student, df_enrolled, left_on='id', right_on='student_id', how='inner')
              result[['name', 'class']]
    """
    ...

def sql_inner_join_column_alias() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT art.name AS artist, alb.title AS album FROM df_artist AS art INNER JOIN df_album AS alb ON art.id = alb.artist_id")
    📌 Pandas: result = pd.merge(df_artist, df_album, left_on='id', right_on='artist_id', how='inner')
              result[['name', 'title']].rename(columns={'name': 'artist', 'title': 'album'})
    """
    ...

def sql_left_join() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_student LEFT JOIN df_enrolled ON df_student.id = df_enrolled.student_id")
    📌 Pandas: pd.merge(df_student, df_enrolled, left_on='id', right_on='student_id', how='left')
    """
    ...

def sql_left_join_columns() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT df_student.name, df_enrolled.class FROM df_student LEFT JOIN df_enrolled ON df_student.id = df_enrolled.student_id")
    📌 Pandas: result = pd.merge(df_student, df_enrolled, left_on='id', right_on='student_id', how='left')
              result[['name', 'class']]
    """
    ...

def sql_left_join_alias() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT a.name AS artist, alb.title AS album FROM df_artist AS a LEFT JOIN df_album AS alb ON a.id = alb.artist_id")
    📌 Pandas: result = pd.merge(df_artist, df_album, left_on='id', right_on='artist_id', how='left')
              result[['name', 'title']].rename(columns={'name': 'artist', 'title': 'album'})
    """
    ...

def sql_right_join() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_courses RIGHT JOIN df_student ON df_student.course_id = df_courses.student_id")
    📌 Pandas: pd.merge(df_courses, df_student, left_on='student_id', right_on='course_id', how='right')
    """
    ...

def sql_right_join_hotels() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_booking_requests RIGHT JOIN df_hotels ON df_hotels.location = df_booking_requests.client_destination")
    📌 Pandas: pd.merge(df_booking_requests, df_hotels, left_on='client_destination', right_on='location', how='right')
    """
    ...

def sql_full_outer_join() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_user FULL OUTER JOIN df_blocked ON df_blocked.id = df_user.id")
    📌 Pandas: pd.merge(df_user, df_blocked, left_on='id', right_on='id', how='outer')
    """
    ...

def sql_full_outer_join_menu() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_menu FULL OUTER JOIN df_unavailable_items ON df_menu.name = df_unavailable_items.name")
    📌 Pandas: pd.merge(df_menu, df_unavailable_items, left_on='name', right_on='name', how='outer')
    """
    ...

# ============================================================
# ۱۴. Subquery — زیرکوئری
# ============================================================

def sql_subquery_scalar_avg() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT first_name, last_name, email FROM df_customers WHERE age > (SELECT AVG(age) FROM df_customers)")
    📌 Pandas: avg_age = df_customers['age'].mean()
              df_customers[df_customers['age'] > avg_age][['first_name', 'last_name', 'email']]
    """
    ...

def sql_subquery_scalar_min() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT employee_name FROM df_employees WHERE salary = (SELECT MIN(salary) FROM df_employees)")
    📌 Pandas: min_salary = df_employees['salary'].min()
              df_employees[df_employees['salary'] == min_salary][['employee_name']]
    """
    ...

def sql_subquery_scalar_max() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT product_name, price FROM df_products WHERE price = (SELECT MAX(price) FROM df_products)")
    📌 Pandas: max_price = df_products['price'].max()
              df_products[df_products['price'] == max_price][['product_name', 'price']]
    """
    ...

def sql_subquery_in() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT first_name, last_name FROM df_customers WHERE id IN (SELECT customer_id FROM df_orders)")
    📌 Pandas: df_customers[df_customers['id'].isin(df_orders['customer_id'])][['first_name', 'last_name']]
    """
    ...

def sql_subquery_not_in() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_employees WHERE department_id NOT IN (SELECT department_id FROM df_departments)")
    📌 Pandas: all_dept_ids = df_departments['department_id']
              df_employees[~df_employees['department_id'].isin(all_dept_ids)]
    """
    ...

def sql_subquery_cross_table() -> Any:
    """
    📌 فرم درست: duckdb.sql("SELECT * FROM df_macros WHERE id = (SELECT id FROM df_snack WHERE name = 'apple')")
    📌 Pandas: apple_id = df_snack[df_snack['name'] == 'apple']['id'].iloc[0]
              df_macros[df_macros['id'] == apple_id]
    """
    ...

# ============================================================
# ۱۵. INSERT / UPDATE / DELETE
# ============================================================

def sql_insert() -> Any:
    """
    📌 SQL:    INSERT INTO orders (name, id, price) VALUES ('Teddy bear', 6574, 13)
    📌 Pandas: df_orders.loc[len(df_orders)] = ['Teddy bear', 6574, 13]
    ⚠️ DuckDB از INSERT پشتیبانی نمی‌کند. فقط با Pandas.
    """
    ...

def sql_update_where() -> Any:
    """
    📌 SQL:    UPDATE reservation SET time = '19:00' WHERE name = 'Smith'
    📌 Pandas: df_reservation.loc[df_reservation['name'] == 'Smith', 'time'] = '19:00'
    ⚠️ DuckDB از UPDATE پشتیبانی نمی‌کند. فقط با Pandas.
    """
    ...

def sql_update_all() -> Any:
    """
    📌 SQL:    UPDATE employees SET salary = 5000
    📌 Pandas: df_employees['salary'] = 5000
    ⚠️ DuckDB از UPDATE پشتیبانی نمی‌کند. فقط با Pandas.
    """
    ...

def sql_delete() -> Any:
    """
    📌 SQL:    DELETE FROM orders WHERE price < 10
    📌 Pandas: df_orders.query("price >= 10", inplace=True)
    ⚠️ DuckDB از DELETE پشتیبانی نمی‌کند. فقط با Pandas.
    """
    ...

# ============================================================
# ۱۶. ALTER TABLE
# ============================================================

def sql_alter_add_column() -> Any:
    """
    📌 SQL:    ALTER TABLE orders ADD discount INT
    📌 Pandas: df_orders['discount'] = None
    ⚠️ DuckDB از ALTER پشتیبانی نمی‌کند. فقط با Pandas.
    """
    ...

def sql_alter_rename_column() -> Any:
    """
    📌 SQL:    ALTER TABLE orders RENAME price TO bill
    📌 Pandas: df_orders.rename(columns={'price': 'bill'}, inplace=True)
    ⚠️ DuckDB از ALTER پشتیبانی نمی‌کند. فقط با Pandas.
    """
    ...

def sql_alter_drop_column() -> Any:
    """
    📌 SQL:    ALTER TABLE orders DROP COLUMN discount
    📌 Pandas: df_orders.drop(columns=['discount'], inplace=True)
    ⚠️ DuckDB از ALTER پشتیبانی نمی‌کند. فقط با Pandas.
    """
    ...

# ============================================================
# ۱۷. CREATE / DROP TABLE
# ============================================================

def sql_create_table() -> Any:
    """
    📌 SQL:    CREATE TABLE directory (floor INTEGER, company TEXT)
    📌 Pandas: new_table = pd.DataFrame({'floor': pd.Series(dtype='int'), 'company': pd.Series(dtype='str')})
    ⚠️ DuckDB از CREATE پشتیبانی نمی‌کند. فقط با Pandas.
    """
    ...

def sql_drop_table() -> Any:
    """
    📌 SQL:    DROP TABLE past_events
    📌 Pandas: # Tables not directly dropped in Pandas
    ⚠️ DuckDB از DROP پشتیبانی نمی‌کند. فقط با Pandas.
    """
    ...