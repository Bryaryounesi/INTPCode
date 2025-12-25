# فایل شانزدهم آموزش پایتون - ارتباط با API
# ====================================================
print("lesson name : communicating with APIs")

# 🔥 ضروری: مقدمه و مفاهیم پایه API
print("=== Introduction to APIs ===")
print("API مانند پیشخدمت در رستوران عمل می‌کند:")
print("- مشتری (برنامه ما) سفارش می‌دهد")
print("- پیشخدمت (API) سفارش را به آشپزخانه (سرور) می‌برد") 
print("- آشپزخانه غذا را آماده می‌کند")
print("- پیشخدمت غذا را به مشتری برمی‌گرداند")

print("-------------------------")

# 🔥 ضروری: نصب و ایمپورت کتابخانه requests
import requests
print("✅ requests library imported successfully")

print("-------------------------")

# 🔥 ضروری: درخواست GET
print("=== GET Requests ===")
url_simple = "https://jsonplaceholder.typicode.com/posts/1"
response_simple = requests.get(url_simple)
print(f"Status Code: {response_simple.status_code}")
print(f"Response: {response_simple.json()}")

# GET با پارامتر
base_url = "https://jsonplaceholder.typicode.com/posts"
params = {'userId': 1}
response_separated = requests.get(base_url, params=params)
print(f"Full URL: {response_separated.url}")
print(f"Number of posts: {len(response_separated.json())}")

# GET با f-string
user_id = 1
url_fstring = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
response_fstring = requests.get(url_fstring)
print(f"Status Code: {response_fstring.status_code}")

print("-------------------------")

# 🔥 ضروری: بررسی پاسخ (Response)
print("=== Response Analysis ===")
test_url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(test_url)
print(f"response.json(): {response.json()}")
print(f"response.text[:100]: {response.text[:100]}...")
print(f"response.status_code: {response.status_code}")
print(f"response.ok: {response.ok}")
print(f"response.url: {response.url}")

if response.ok:
    print("✅ Request was successful")
else:
    print("❌ Request failed")

print("-------------------------")

# 🔥 ضروری: درخواست POST
print("=== POST Requests ===")
url_post = "https://jsonplaceholder.typicode.com/posts"
data_to_send = {
    "title": "My Python Post",
    "body": "This is a test post from Python",
    "userId": 1
}
response_post = requests.post(url_post, json=data_to_send)
print(f"Status Code: {response_post.status_code}")
print(f"Response: {response_post.json()}")

# تفاوت data و json
import json
response_data = requests.post(url_post, data=json.dumps(data_to_send),
                              headers={'Content-Type': 'application/json'})
print(f"With data - Content-Type: {response_data.request.headers.get('Content-Type')}")

print("-------------------------")

# ✅ تمرینی: PUT و PATCH
url_put = "https://jsonplaceholder.typicode.com/posts/1"
put_data = {"id": 1, "title": "Updated Title", "body": "Completely replaced", "userId": 1}
response_put = requests.put(url_put, json=put_data)
print(f"PUT response: {response_put.json()}")

url_patch = "https://jsonplaceholder.typicode.com/posts/1"
patch_data = {"title": "Partially Updated Title"}
response_patch = requests.patch(url_patch, json=patch_data)
print(f"PATCH response: {response_patch.json()}")

print("-------------------------")

# 🔥 ضروری: DELETE
url_delete = "https://jsonplaceholder.typicode.com/posts/1"
response_delete = requests.delete(url_delete)
print(f"DELETE response status: {response_delete.status_code}")

print("-------------------------")

# 🔥 ضروری: مدیریت خطاها در API
print("=== Error Handling ===")
def safe_api_call(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
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

result = safe_api_call("https://jsonplaceholder.typicode.com/users/1")
if result:
    print(f"✅ Safe call result: {result}")

print("-------------------------")

# ✅ تمرینی: مثال‌های کاربردی
print("=== Practical Examples ===")
users_url = "https://jsonplaceholder.typicode.com/users"
users_response = requests.get(users_url)
users_data = users_response.json()
print(f"First user: {users_data[0]['name']} - {users_data[0]['email']}")

new_post = {"title": "Learning Python APIs", "body": "Learning API communication", "userId": 1}
create_response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
if create_response.status_code == 201:
    created_post = create_response.json()
    print(f"✅ Post created with ID: {created_post['id']}")

update_data = {"title": "Updated: Learning Python APIs"}
update_response = requests.patch(f"https://jsonplaceholder.typicode.com/posts/{created_post['id']}", json=update_data)
if update_response.status_code == 200:
    print("✅ Post updated successfully")

delete_response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{created_post['id']}")
if delete_response.status_code == 200:
    print("✅ Post deleted successfully")

print("-------------------------")

# 🔥 ضروری: پروژه عملی سیستم مدیریت کاربران
print("=== User Management System ===")
class UserManager:
    def __init__(self, base_url):
        self.base_url = base_url
    def get_all_users(self):
        response = requests.get(f"{self.base_url}/users")
        return response.json() if response.ok else []
    def get_user(self, user_id):
        response = requests.get(f"{self.base_url}/users/{user_id}")
        return response.json() if response.ok else None
    def create_user(self, user_data):
        response = requests.post(f"{self.base_url}/users", json=user_data)
        return response.json() if response.status_code == 201 else None
    def update_user(self, user_id, update_data):
        response = requests.patch(f"{self.base_url}/users/{user_id}", json=update_data)
        return response.json() if response.ok else None
    def delete_user(self, user_id):
        response = requests.delete(f"{self.base_url}/users/{user_id}")
        return response.status_code == 200

user_manager = UserManager("https://jsonplaceholder.typicode.com")
users = user_manager.get_all_users()
print(f"Number of users: {len(users)}")
user_1 = user_manager.get_user(1)
if user_1:
    print(f"User 1: {user_1['name']}")

print("-------------------------")

# ⚠️ غیرضروری: نکات پیشرفته
print("=== Advanced Tips ===")
with requests.Session() as session:
    session.headers.update({'User-Agent': 'MyApp/1.0'})
    response1 = session.get("https://jsonplaceholder.typicode.com/users/1")
    response2 = session.get("https://jsonplaceholder.typicode.com/users/2")
    print(f"Session request 1: {response1.status_code}")
    print(f"Session request 2: {response2.status_code}")

try:
    response_timeout = requests.get("https://jsonplaceholder.typicode.com/users", timeout=(3.05, 10))
    print(f"Request with timeout: {response_timeout.status_code}")
except requests.exceptions.Timeout:
    print("Request timed out")

print("SSL verification can be disabled with verify=False")

print("==============================")
print("End of API communication training")
print("==============================")