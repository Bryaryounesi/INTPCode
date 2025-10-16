# فایل شانزدهم آموزش پایتون - ارتباط با API
# ======================================

print("lesson name : communicating with APIs")

# ==============================
# مقدمه و مفاهیم پایه API
# ==============================

print("=== Introduction to APIs ===")

# مثال ساده برای درک مفهوم API
print("API مانند پیشخدمت در رستوران عمل می‌کند:")
print("- مشتری (برنامه ما) سفارش می‌دهد")
print("- پیشخدمت (API) سفارش را به آشپزخانه (سرور) می‌برد") 
print("- آشپزخانه غذا را آماده می‌کند")
print("- پیشخدمت غذا را به مشتری برمی‌گرداند")
print("-------------------------")

# ==============================
# نصب و ایمپورت کتابخانه requests
# ==============================

print("=== Installing and Importing Requests ===")

# ایمپورت کتابخانه requests
import requests

print("✅ requests library imported successfully")

print("-------------------------")

# ==============================
# درخواست GET - دریافت داده
# ==============================

print("=== GET Requests ===")

# روش اول: URL کامل
print("Method 1 - Complete URL:")
url_simple = "https://jsonplaceholder.typicode.com/posts/1"
response_simple = requests.get(url_simple)
print(f"Status Code: {response_simple.status_code}")
print(f"Response: {response_simple.json()}")

print("-------------------------")

# روش دوم: جدا کردن URL و پارامترها
print("Method 2 - Separated URL and Parameters:")
base_url = "https://jsonplaceholder.typicode.com/posts"
params = {
    'userId': 1
}

response_separated = requests.get(base_url, params=params)
print(f"Status Code: {response_separated.status_code}")
print(f"Full URL: {response_separated.url}")
print(f"Number of posts: {len(response_separated.json())}")

print("-------------------------")

# روش سوم: استفاده از f-string برای ساخت URL
print("Method 3 - Using f-string:")
user_id = 1
url_fstring = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
response_fstring = requests.get(url_fstring)
print(f"Status Code: {response_fstring.status_code}")

print("-------------------------")

# ==============================
# بررسی پاسخ (Response)
# ==============================

print("=== Response Analysis ===")

# ایجاد یک درخواست نمونه
test_url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(test_url)

print("Response Analysis Methods:")
print(f"1. response.json(): {response.json()}")
print(f"2. response.text: {response.text[:100]}...")  # نمایش 100 کاراکتر اول
print(f"3. response.status_code: {response.status_code}")
print(f"4. response.headers: {dict(response.headers)}")
print(f"5. response.ok: {response.ok}")
print(f"6. response.url: {response.url}")

print("-------------------------")

# بررسی وضعیت درخواست
if response.ok:
    print("✅ Request was successful")
else:
    print("❌ Request failed")

print("-------------------------")

# ==============================
# درخواست POST - ارسال داده
# ==============================

print("=== POST Requests ===")

# ارسال داده با json
print("POST with json parameter:")
url_post = "https://jsonplaceholder.typicode.com/posts"
data_to_send = {
    "title": "My Python Post",
    "body": "This is a test post from Python",
    "userId": 1
}

response_post = requests.post(url_post, json=data_to_send)
print(f"Status Code: {response_post.status_code}")
print(f"Response: {response_post.json()}")

print("-------------------------")

# تفاوت بین data و json
print("Difference between data and json:")
# با json (پایتون خودش تبدیل می‌کند)
response_json = requests.post(url_post, json=data_to_send)
print(f"With json - Content-Type: {response_json.request.headers.get('Content-Type')}")

# با data (ما باید خودمان تبدیل کنیم)
import json
response_data = requests.post(url_post, data=json.dumps(data_to_send), 
                             headers={'Content-Type': 'application/json'})
print(f"With data - Content-Type: {response_data.request.headers.get('Content-Type')}")

print("-------------------------")

# ==============================
# درخواست PUT - جایگزینی کامل
# ==============================

print("=== PUT Requests ===")

# جایگزینی کامل یک منبع
url_put = "https://jsonplaceholder.typicode.com/posts/1"
put_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "This post has been completely replaced",
    "userId": 1
}

response_put = requests.put(url_put, json=put_data)
print(f"Status Code: {response_put.status_code}")
print(f"Updated post: {response_put.json()}")

print("-------------------------")

# ==============================
# درخواست PATCH - به‌روزرسانی جزئی
# ==============================

print("=== PATCH Requests ===")

# به‌روزرسانی فقط برخی فیلدها
url_patch = "https://jsonplaceholder.typicode.com/posts/1"
patch_data = {
    "title": "Partially Updated Title"
}

response_patch = requests.patch(url_patch, json=patch_data)
print(f"Status Code: {response_patch.status_code}")
print(f"Partially updated post: {response_patch.json()}")

print("-------------------------")

# ==============================
# درخواست DELETE - حذف داده
# ==============================

print("=== DELETE Requests ===")

# حذف یک منبع
url_delete = "https://jsonplaceholder.typicode.com/posts/1"
response_delete = requests.delete(url_delete)
print(f"Status Code: {response_delete.status_code}")
print(f"Delete response: {response_delete.json()}")

print("-------------------------")

# ==============================
# کدهای وضعیت HTTP
# ==============================

print("=== HTTP Status Codes ===")

# نمایش کدهای وضعیت رایج
status_codes = {
    200: "OK - Success",
    201: "Created - Resource created",
    204: "No Content - Success but no content",
    400: "Bad Request - Client error",
    401: "Unauthorized - Authentication needed",
    403: "Forbidden - Access denied",
    404: "Not Found - Resource not found",
    500: "Internal Server Error - Server error"
}

print("Common HTTP Status Codes:")
for code, meaning in status_codes.items():
    print(f"{code}: {meaning}")

print("-------------------------")

# ==============================
# هدرها و احراز هویت
# ==============================

print("=== Headers and Authentication ===")

# ارسال هدرهای سفارشی
headers = {
    'User-Agent': 'MyPythonApp/1.0',
    'Accept': 'application/json',
    'Authorization': 'Bearer your_token_here'
}

url_with_headers = "https://jsonplaceholder.typicode.com/users/1"
response_headers = requests.get(url_with_headers, headers=headers)
print(f"Status with custom headers: {response_headers.status_code}")

print("-------------------------")

# احراز هویت پایه (Basic Auth)
from requests.auth import HTTPBasicAuth

# توجه: این یک مثال است و در عمل نیاز به credentials واقعی دارید
auth_example = HTTPBasicAuth('username', 'password')
print("Basic authentication setup complete")

print("-------------------------")

# ==============================
# مدیریت خطاها
# ==============================

print("=== Error Handling ===")

# مدیریت خطاهای مختلف
def safe_api_call(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # خطا برای کدهای 4xx/5xx
        return response.json()
    except requests.exceptions.Timeout:
        print("❌ Request timed out")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error")
    except requests.exceptions.HTTPError as err:
        print(f"❌ HTTP error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"❌ An error occurred: {err}")
    return None

# تست تابع مدیریت خطا
result = safe_api_call("https://jsonplaceholder.typicode.com/users/1")
if result:
    print(f"✅ Safe call result: {result}")

print("-------------------------")

# ==============================
# مثال‌های کاربردی واقعی
# ==============================

print("=== Practical Examples ===")

# مثال 1: دریافت اطلاعات کاربر
print("Example 1 - Get user information:")
users_url = "https://jsonplaceholder.typicode.com/users"
users_response = requests.get(users_url)
users_data = users_response.json()

print(f"First user: {users_data[0]['name']} - {users_data[0]['email']}")

print("-------------------------")

# مثال 2: ایجاد پست جدید
print("Example 2 - Create new post:")
new_post = {
    "title": "Learning Python APIs",
    "body": "This is a great way to learn about API communication",
    "userId": 1
}

create_response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
if create_response.status_code == 201:
    created_post = create_response.json()
    print(f"✅ Post created with ID: {created_post['id']}")

print("-------------------------")

# مثال 3: به‌روزرسانی پست
print("Example 3 - Update post:")
update_data = {
    "title": "Updated: Learning Python APIs"
}

update_response = requests.patch(
    f"https://jsonplaceholder.typicode.com/posts/{created_post['id']}", 
    json=update_data
)
if update_response.status_code == 200:
    print("✅ Post updated successfully")

print("-------------------------")

# مثال 4: حذف پست
print("Example 4 - Delete post:")
delete_response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{created_post['id']}")
if delete_response.status_code == 200:
    print("✅ Post deleted successfully")

print("-------------------------")

# ==============================
# پروژه عملی: سیستم مدیریت کاربران
# ==============================

print("=== User Management System ===")

class UserManager:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_all_users(self):
        """دریافت تمام کاربران"""
        response = requests.get(f"{self.base_url}/users")
        return response.json() if response.ok else []
    
    def get_user(self, user_id):
        """دریافت کاربر خاص"""
        response = requests.get(f"{self.base_url}/users/{user_id}")
        return response.json() if response.ok else None
    
    def create_user(self, user_data):
        """ایجاد کاربر جدید"""
        response = requests.post(f"{self.base_url}/users", json=user_data)
        return response.json() if response.status_code == 201 else None
    
    def update_user(self, user_id, update_data):
        """به‌روزرسانی کاربر"""
        response = requests.patch(f"{self.base_url}/users/{user_id}", json=update_data)
        return response.json() if response.ok else None
    
    def delete_user(self, user_id):
        """حذف کاربر"""
        response = requests.delete(f"{self.base_url}/users/{user_id}")
        return response.status_code == 200

# تست سیستم مدیریت کاربران
user_manager = UserManager("https://jsonplaceholder.typicode.com")

# دریافت کاربران
users = user_manager.get_all_users()
print(f"Number of users: {len(users)}")

# دریافت کاربر خاص
user_1 = user_manager.get_user(1)
if user_1:
    print(f"User 1: {user_1['name']}")

print("-------------------------")

# ==============================
# نکات پیشرفته
# ==============================

print("=== Advanced Tips ===")

# استفاده از Session برای حفظ connection
print("Using Session for multiple requests:")
with requests.Session() as session:
    session.headers.update({'User-Agent': 'MyApp/1.0'})
    
    # چند درخواست با همان session
    response1 = session.get("https://jsonplaceholder.typicode.com/users/1")
    response2 = session.get("https://jsonplaceholder.typicode.com/users/2")
    
    print(f"Session request 1: {response1.status_code}")
    print(f"Session request 2: {response2.status_code}")

print("-------------------------")

# تنظیم timeout برای درخواست‌ها
print("Setting timeout for requests:")
try:
    response_timeout = requests.get(
        "https://jsonplaceholder.typicode.com/users", 
        timeout=(3.05, 10)  # (connect timeout, read timeout)
    )
    print(f"Request with timeout: {response_timeout.status_code}")
except requests.exceptions.Timeout:
    print("Request timed out")

print("-------------------------")

# بررسی SSL verification
print("SSL verification (use with caution):")
# response_ssl = requests.get("https://example.com", verify=False)  # غیرفعال کردن verify
print("SSL verification can be disabled with verify=False")

print("==============================")
print("End of API communication training")
print("==============================")
