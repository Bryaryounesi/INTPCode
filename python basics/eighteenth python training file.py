# فایل هجدهم آموزش پایتون - متغیرهای محیطی و APIهای خصوصی
# ====================================================

print("lesson name : environment variables and private APIs")

# ==============================
# متغیرهای محیطی (Environment Variables)
# ==============================

print("=== Environment Variables ===")

# ایمپورت ماژول os
import os
import requests
print("✅ os module imported successfully")

# روش نادرست: ذخیره اطلاعات حساس در کد
print("❌ Dangerous way - hardcoded secrets:")
dangerous_example = {
    "API_KEY": "12345-abcde-67890-fghij-12345",
    "SECRET_KEY": "mysecretkey"
}
print("Never do this in real projects!")
print("Example structure only:", dangerous_example)

print("-------------------------")

# روش صحیح: استفاده از متغیرهای محیطی
print("✅ Correct way - using environment variables:")

# روش 1: استفاده از os.getenv()
api_key = os.getenv("MY_API_KEY")
print(f"API Key using os.getenv(): {api_key}")

# روش 2: استفاده مستقیم از os.getenv در print
print(f"Direct os.getenv(): {os.getenv('MY_API_KEY')}")

print("-------------------------")

# ==============================
# کار با فایل‌های .env
# ==============================

print("=== Working with .env Files ===")

# استفاده از python-dotenv برای بارگذاری فایل‌های .env
try:
    import dotenv
    print("✅ dotenv module imported successfully")
    
    # بارگذاری متغیرها از فایل .env
    dotenv.load_dotenv()
    print("✅ .env file loaded successfully")
    
    # خواندن متغیرها پس از بارگذاری
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    debug_mode = os.getenv("DEBUG")
    
    print(f"Database User: {db_user}")
    print(f"Database Password: {db_pass}")
    print(f"Debug Mode: {debug_mode}")
    
except ImportError:
    print("❌ dotenv module not available")
    print("You can install it with: pip install python-dotenv")

print("-------------------------")

# ==============================
# دیکشنری os.environ
# ==============================

print("=== os.environ Dictionary ===")

# نمایش تمام متغیرهای محیطی
print("All environment variables (first 5):")
for i, (key, value) in enumerate(os.environ.items()):
    if i < 5:  # نمایش فقط 5 مورد اول
        print(f"  {key}: {value}")
    else:
        break

print("... and many more")

print("-------------------------")

# دسترسی به متغیر خاص با os.environ
try:
    python_path = os.environ["PYTHONPATH"]
    print(f"PYTHONPATH: {python_path}")
except KeyError:
    print("PYTHONPATH not found")

print("-------------------------")

# مقایسه os.getenv و os.environ
print("Comparison between os.getenv and os.environ:")

# با os.getenv (ایمن‌تر)
api_key_safe = os.getenv("MY_API_KEY", "default_key_here")
print(f"With os.getenv (safe): {api_key_safe}")

# با os.environ (ممکن است خطا دهد)
try:
    api_key_unsafe = os.environ["MY_API_KEY"]
    print(f"With os.environ: {api_key_unsafe}")
except KeyError:
    print("With os.environ: KeyError - Variable not found")

print("-------------------------")

# ==============================
# مدیریت خطا در متغیرهای محیطی
# ==============================

print("=== Error Handling for Environment Variables ===")

# تست متغیرهای موجود و ناموجود
test_variables = [
    "MY_API_KEY",
    "NON_EXISTENT_KEY", 
    "SECRET_KEY",
    "ANOTHER_MISSING_KEY"
]

for var_name in test_variables:
    # روش ایمن با مقدار پیش‌فرض
    value = os.getenv(var_name, "NOT_FOUND")
    print(f"{var_name}: {value}")

print("-------------------------")

# استفاده از os.environ.get() برای ایمنی بیشتر
safe_value = os.environ.get("MISSING_KEY", "default_value")
print(f"Safe access with os.environ.get(): {safe_value}")

print("-------------------------")

# ==============================
# APIهای خصوصی و احراز هویت
# ==============================

print("=== Private APIs and Authentication ===")

# مثال 1: ارسال API Key در هدر
print("Example 1 - API Key in headers:")
headers_with_key = {
    "api-key": "MY_SECRET_KEY",
    "Content-Type": "application/json"
}

print("Headers structure:")
for key, value in headers_with_key.items():
    print(f"  {key}: {value}")

print("-------------------------")

# مثال 2: درخواست GET با هدرهای سفارشی
print("Example 2 - GET request with custom headers:")
try:
    # این یک مثال است - در عمل نیاز به URL و API Key واقعی دارید
    example_headers = {
        "Authorization": "Bearer your_token_here",
        "User-Agent": "MyPythonApp/1.0",
        "Accept": "application/json"
    }
    
    print("Custom headers for GET request:")
    for key, value in example_headers.items():
        print(f"  {key}: {value}")
        
except Exception as e:
    print(f"Example demonstration only: {e}")

print("-------------------------")

# مثال 3: درخواست POST با هدر و بدنه
print("Example 3 - POST request with headers and body:")
post_headers = {
    "api-key": "MY_SECRET_KEY",
    "Content-Type": "application/json"
}

post_body = {
    "message": "I was here!",
    "user_id": 12345,
    "timestamp": "2024-01-15T10:30:00Z"
}

print("POST Headers:")
for key, value in post_headers.items():
    print(f"  {key}: {value}")

print("POST Body:")
for key, value in post_body.items():
    print(f"  {key}: {value}")

print("-------------------------")

# ==============================
# پارامترهای پرس‌وجو (Query Parameters)
# ==============================

print("=== Query Parameters ===")

# روش 1: ساخت URL دستی
print("Method 1 - Manual URL construction:")
base_url = "https://api.example.com/search"
manual_url = f"{base_url}?query=python&page=2&sort=asc"
print(f"Manual URL: {manual_url}")

print("-------------------------")

# روش 2: استفاده از پارامترهای دیکشنری
print("Method 2 - Using params dictionary:")
params_dict = {
    "query": "python",
    "page": 2,
    "sort": "asc",
    "limit": 10
}

print("Query parameters:")
for key, value in params_dict.items():
    print(f"  {key}: {value}")

# شبیه‌سازی درخواست با پارامترها
print("Simulated request with params:")
print("requests.get('https://api.example.com/search', params=params_dict)")

print("-------------------------")

# مثال صفحه‌بندی (Pagination)
print("Pagination example:")
pagination_params = {
    "page": 3,
    "per_page": 20
}

print("Pagination parameters:")
for key, value in pagination_params.items():
    print(f"  {key}: {value}")

print("-------------------------")

# ==============================
# مدیریت پاسخ‌های API
# ==============================

print("=== API Response Handling ===")

# شبیه‌سازی پاسخ API
print("Simulating API response handling:")

# مثال پاسخ JSON ساده
simple_response = {
    "status": "success",
    "data": {
        "user": {
            "id": 123,
            "name": "John Doe",
            "email": "john@example.com"
        }
    }
}

print("Simple JSON response structure:")
print(simple_response)

print("-------------------------")

# دسترسی به داده‌های تودرتو
print("Accessing nested data:")
try:
    user_name = simple_response["data"]["user"]["name"]
    user_email = simple_response["data"]["user"]["email"]
    print(f"User Name: {user_name}")
    print(f"User Email: {user_email}")
except KeyError as e:
    print(f"Key error: {e}")

print("-------------------------")

# استفاده از .get() برای دسترسی ایمن
print("Safe access with .get():")
safe_name = simple_response.get("data", {}).get("user", {}).get("name", "Unknown")
safe_phone = simple_response.get("data", {}).get("user", {}).get("phone", "Not provided")
print(f"Safe Name: {safe_name}")
print(f"Safe Phone: {safe_phone}")

print("-------------------------")

# ==============================
# کار با پاسخ‌های لیستی
# ==============================

print("=== Working with List Responses ===")

# شبیه‌سازی پاسخ لیستی از API
list_response = [
    {"id": 1, "name": "Bulbasaur", "type": "Grass/Poison"},
    {"id": 2, "name": "Ivysaur", "type": "Grass/Poison"},
    {"id": 3, "name": "Venusaur", "type": "Grass/Poison"},
    {"id": 4, "name": "Charmander", "type": "Fire"}
]

print("List response example (Pokemon):")

# دسترسی به آیتم خاص
print("Accessing specific item:")
first_pokemon = list_response[0]
print(f"First Pokemon: {first_pokemon['name']} (ID: {first_pokemon['id']})")

print("-------------------------")

# حلقه زدن through لیست
print("Looping through list:")
for pokemon in list_response:
    print(f"  {pokemon['id']}: {pokemon['name']} - {pokemon['type']}")

print("-------------------------")

# استفاده از .get() در لیست
print("Using .get() in list iteration:")
for pokemon in list_response:
    name = pokemon.get("name", "Unknown")
    ability = pokemon.get("ability", "Not specified")
    print(f"  {name} - Ability: {ability}")

print("-------------------------")

# ==============================
# پروژه عملی: سیستم مدیریت تنظیمات
# ==============================

print("=== Configuration Management System ===")

class Config:
    def __init__(self):
        self.load_environment_variables()
    
    def load_environment_variables(self):
        """بارگذاری متغیرهای محیطی از فایل .env"""
        try:
            import dotenv
            dotenv.load_dotenv()
            print("✅ Environment variables loaded from .env")
        except ImportError:
            print("⚠️ dotenv not available, using system environment variables")
        
        # بارگذاری تنظیمات
        self.database_url = os.getenv("DATABASE_URL", "sqlite:///default.db")
        self.api_key = os.getenv("API_KEY", "default_api_key")
        self.debug_mode = os.getenv("DEBUG", "False").lower() == "true"
        self.port = int(os.getenv("PORT", "8000"))
    
    def display_config(self):
        """نمایش تنظیمات (بدون نمایش اطلاعات حساس)"""
        print("🔧 Application Configuration:")
        print(f"  Database URL: {self.database_url}")
        print(f"  API Key: {'*' * len(self.api_key) if self.api_key else 'Not set'}")
        print(f"  Debug Mode: {self.debug_mode}")
        print(f"  Port: {self.port}")
    
    def make_authenticated_request(self, url, data=None):
        """ایجاد درخواست احراز هویت شده"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "MyApp/1.0"
        }
        
        try:
            if data:
                response = requests.post(url, headers=headers, json=data)
            else:
                response = requests.get(url, headers=headers)
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
            return None

# تست سیستم مدیریت تنظیمات
print("Testing configuration system:")
config = Config()
config.display_config()

print("-------------------------")

# ==============================
# مثال کامل: درخواست API با مدیریت خطا
# ==============================

print("=== Complete API Request Example ===")

def make_api_request(url, method="GET", headers=None, params=None, data=None):
    """
    تابع کامل برای ارسال درخواست API با مدیریت خطا
    """
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=10)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=data, timeout=10)
        else:
            return {"success": False, "error": f"Unsupported method: {method}"}
        
        # بررسی وضعیت پاسخ
        response.raise_for_status()
        
        # پردازش پاسخ JSON
        try:
            response_data = response.json()
            return {
                "success": True,
                "status_code": response.status_code,
                "data": response_data
            }
        except ValueError:
            return {
                "success": True,
                "status_code": response.status_code,
                "data": response.text
            }
            
    except requests.exceptions.HTTPError as e:
        return {
            "success": False,
            "error": f"HTTP Error: {e}",
            "status_code": response.status_code if 'response' in locals() else None
        }
    except requests.exceptions.ConnectionError as e:
        return {"success": False, "error": f"Connection Error: {e}"}
    except requests.exceptions.Timeout as e:
        return {"success": False, "error": f"Timeout Error: {e}"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": f"Request Error: {e}"}
    except Exception as e:
        return {"success": False, "error": f"Unexpected Error: {e}"}

# تست تابع
print("Testing complete API request function:")

# شبیه‌سازی درخواست
test_headers = {"Authorization": "Bearer test_token"}
test_params = {"page": 1, "limit": 10}

result = make_api_request(
    "https://httpbin.org/json",
    method="GET",
    headers=test_headers,
    params=test_params
)

if result["success"]:
    print("✅ Request successful!")
    print(f"Status Code: {result['status_code']}")
    print(f"Data: {result['data']}")
else:
    print(f"❌ Request failed: {result['error']}")

print("-------------------------")

# ==============================
# بهترین روش‌ها و نکات امنیتی
# ==============================

print("=== Best Practices and Security Tips ===")

print("1. 🚫 Never hardcode sensitive information")
print("2. 🔐 Use environment variables for secrets")
print("3. 📁 Use .env files for development (add to .gitignore)")
print("4. 🔒 Use HTTPS for API calls")
print("5. ⏱️ Always set timeouts for requests")
print("6. 🛡️ Validate and sanitize all inputs")
print("7. 📝 Use proper error handling")
print("8. 🔑 Rotate API keys regularly")
print("9. 📊 Monitor and log API usage")
print("10. 🧪 Test with different environments")

print("-------------------------")

# مثال فایل .env
print("Example .env file structure:")
env_example = """
# Database Configuration
DATABASE_URL=postgresql://user:pass@localhost/dbname
DB_HOST=localhost
DB_PORT=5432

# API Keys
API_KEY=your_secret_api_key_here
SECRET_KEY=your_secret_key_here

# Application Settings
DEBUG=True
PORT=8000
LOG_LEVEL=INFO

# External Services
WEATHER_API_KEY=weather_service_key
EMAIL_API_KEY=email_service_key
"""

print(env_example)

print("==============================")
print("End of environment variables and private APIs training")
print("==============================")