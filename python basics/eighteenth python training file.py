# فایل هجدهم آموزش پایتون - متغیرهای محیطی و APIهای خصوصی
# ====================================================
print("lesson name : environment variables and private APIs")

# 🔥 ضروری: متغیرهای محیطی (Environment Variables)
print("=== Environment Variables ===")
import os
import requests
print("✅ os module imported successfully")

# ⚠️ غیرضروری: روش نادرست ذخیره اطلاعات حساس
print("❌ Dangerous way - hardcoded secrets:")
dangerous_example = {
    "API_KEY": "12345-abcde-67890-fghij-12345",
    "SECRET_KEY": "mysecretkey"
}
print("Never do this in real projects!")
print("Example structure only:", dangerous_example)

# 🔥 ضروری: روش صحیح با os.getenv()
print("-------------------------")
print("✅ Correct way - using environment variables:")
api_key = os.getenv("MY_API_KEY")
print(f"API Key using os.getenv(): {api_key}")
print(f"Direct os.getenv(): {os.getenv('MY_API_KEY')}")

# 🔥 ضروری: کار با فایل‌های .env
print("-------------------------")
print("=== Working with .env Files ===")
try:
    import dotenv
    print("✅ dotenv module imported successfully")
    dotenv.load_dotenv()
    print("✅ .env file loaded successfully")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    debug_mode = os.getenv("DEBUG")
    print(f"Database User: {db_user}")
    print(f"Database Password: {db_pass}")
    print(f"Debug Mode: {debug_mode}")
except ImportError:
    print("❌ dotenv module not available - pip install python-dotenv")

# 🔥 ضروری: دیکشنری os.environ
print("-------------------------")
print("=== os.environ Dictionary ===")
print("All environment variables (first 5):")
for i, (key, value) in enumerate(os.environ.items()):
    if i < 5:
        print(f"  {key}: {value}")
    else:
        break
print("... and many more")

# ✅ تمرینی: دسترسی امن به متغیر
try:
    python_path = os.environ["PYTHONPATH"]
    print(f"PYTHONPATH: {python_path}")
except KeyError:
    print("PYTHONPATH not found")

# 🔥 ضروری: مقایسه os.getenv و os.environ
print("-------------------------")
print("Comparison between os.getenv and os.environ:")
api_key_safe = os.getenv("MY_API_KEY", "default_key_here")
print(f"With os.getenv (safe): {api_key_safe}")
try:
    api_key_unsafe = os.environ["MY_API_KEY"]
    print(f"With os.environ: {api_key_unsafe}")
except KeyError:
    print("With os.environ: KeyError - Variable not found")

# 🔥 ضروری: مدیریت خطا در متغیرهای محیطی
print("-------------------------")
print("=== Error Handling for Environment Variables ===")
test_variables = ["MY_API_KEY","NON_EXISTENT_KEY","SECRET_KEY","ANOTHER_MISSING_KEY"]
for var_name in test_variables:
    value = os.getenv(var_name, "NOT_FOUND")
    print(f"{var_name}: {value}")
safe_value = os.environ.get("MISSING_KEY", "default_value")
print(f"Safe access with os.environ.get(): {safe_value}")

# 🔥 ضروری: APIهای خصوصی و احراز هویت
print("-------------------------")
print("=== Private APIs and Authentication ===")
print("Example 1 - API Key in headers:")
headers_with_key = {"api-key": "MY_SECRET_KEY","Content-Type": "application/json"}
for key, value in headers_with_key.items():
    print(f"  {key}: {value}")

# ✅ تمرینی: GET با هدر سفارشی
print("-------------------------")
print("Example 2 - GET request with custom headers:")
try:
    example_headers = {
        "Authorization": "Bearer your_token_here",
        "User-Agent": "MyPythonApp/1.0",
        "Accept": "application/json"
    }
    for key, value in example_headers.items():
        print(f"  {key}: {value}")
except Exception as e:
    print(f"Example demonstration only: {e}")

# ✅ تمرینی: POST با هدر و بدنه
print("-------------------------")
print("Example 3 - POST request with headers and body:")
post_headers = {"api-key": "MY_SECRET_KEY","Content-Type": "application/json"}
post_body = {"message": "I was here!","user_id": 12345,"timestamp": "2024-01-15T10:30:00Z"}
for key, value in post_headers.items():
    print(f"  {key}: {value}")
for key, value in post_body.items():
    print(f"  {key}: {value}")

# 🔥 ضروری: پارامترهای پرس‌وجو
print("-------------------------")
print("=== Query Parameters ===")
base_url = "https://api.example.com/search"
manual_url = f"{base_url}?query=python&page=2&sort=asc"
print(f"Manual URL: {manual_url}")
params_dict = {"query": "python","page": 2,"sort": "asc","limit": 10}
for key, value in params_dict.items():
    print(f"  {key}: {value}")
print("Simulated request with params:")
print("requests.get('https://api.example.com/search', params=params_dict)")
pagination_params = {"page": 3,"per_page": 20}
for key, value in pagination_params.items():
    print(f"  {key}: {value}")

# 🔥 ضروری: مدیریت پاسخ‌های API
print("-------------------------")
print("=== API Response Handling ===")
simple_response = {"status": "success","data":{"user":{"id":123,"name":"John Doe","email":"john@example.com"}}}
print(simple_response)
try:
    user_name = simple_response["data"]["user"]["name"]
    user_email = simple_response["data"]["user"]["email"]
    print(f"User Name: {user_name}")
    print(f"User Email: {user_email}")
except KeyError as e:
    print(f"Key error: {e}")
safe_name = simple_response.get("data", {}).get("user", {}).get("name", "Unknown")
safe_phone = simple_response.get("data", {}).get("user", {}).get("phone", "Not provided")
print(f"Safe Name: {safe_name}")
print(f"Safe Phone: {safe_phone}")

# 🔥 ضروری: کار با پاسخ‌های لیستی
print("-------------------------")
print("=== Working with List Responses ===")
list_response = [
    {"id": 1,"name": "Bulbasaur","type": "Grass/Poison"},
    {"id": 2,"name": "Ivysaur","type": "Grass/Poison"},
    {"id": 3,"name": "Venusaur","type": "Grass/Poison"},
    {"id": 4,"name": "Charmander","type": "Fire"}
]
first_pokemon = list_response[0]
print(f"First Pokemon: {first_pokemon['name']} (ID: {first_pokemon['id']})")
for pokemon in list_response:
    print(f"  {pokemon['id']}: {pokemon['name']} - {pokemon['type']}")
for pokemon in list_response:
    name = pokemon.get("name", "Unknown")
    ability = pokemon.get("ability", "Not specified")
    print(f"  {name} - Ability: {ability}")

# 🔥 ضروری: پروژه عملی سیستم مدیریت تنظیمات
print("-------------------------")
print("=== Configuration Management System ===")
class Config:
    def __init__(self):
        self.load_environment_variables()
    def load_environment_variables(self):
        try:
            import dotenv
            dotenv.load_dotenv()
            print("✅ Environment variables loaded from .env")
        except ImportError:
            print("⚠️ dotenv not available, using system environment variables")
        self.database_url = os.getenv("DATABASE_URL","sqlite:///default.db")
        self.api_key = os.getenv("API_KEY","default_api_key")
        self.debug_mode = os.getenv("DEBUG","False").lower()=="true"
        self.port = int(os.getenv("PORT","8000"))
    def display_config(self):
        print("🔧 Application Configuration:")
        print(f"  Database URL: {self.database_url}")
        print(f"  API Key: {'*'*len(self.api_key) if self.api_key else 'Not set'}")
        print(f"  Debug Mode: {self.debug_mode}")
        print(f"  Port: {self.port}")
    def make_authenticated_request(self,url,data=None):
        headers = {"Authorization": f"Bearer {self.api_key}","Content-Type": "application/json","User-Agent": "MyApp/1.0"}
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

print("Testing configuration system:")
config = Config()
config.display_config()

# 🔥 ضروری: مثال کامل API با مدیریت خطا
print("-------------------------")
print("=== Complete API Request Example ===")
def make_api_request(url, method="GET", headers=None, params=None, data=None):
    try:
        if method.upper()=="GET":
            response = requests.get(url, headers=headers, params=params, timeout=10)
        elif method.upper()=="POST":
            response = requests.post(url, headers=headers, json=data, timeout=10)
        else:
            return {"success": False,"error": f"Unsupported method: {method}"}
        response.raise_for_status()
        try:
            response_data = response.json()
            return {"success": True,"status_code": response.status_code,"data": response_data}
        except ValueError:
            return {"success": True,"status_code": response.status_code,"data": response.text}
    except requests.exceptions.HTTPError as e:
        return {"success": False,"error": f"HTTP Error: {e}","status_code": response.status_code if 'response' in locals() else None}
    except requests.exceptions.ConnectionError as e:
        return {"success": False,"error": f"Connection Error: {e}"}
    except requests.exceptions.Timeout as e:
        return {"success": False,"error": f"Timeout Error: {e}"}
    except requests.exceptions.RequestException as e:
        return {"success": False,"error": f"Request Error: {e}"}
    except Exception as e:
        return {"success": False,"error": f"Unexpected Error: {e}"}

test_headers = {"Authorization": "Bearer test_token"}
test_params = {"page": 1,"limit": 10}
result = make_api_request("https://httpbin.org/json", method="GET", headers=test_headers, params=test_params)
if result["success"]:
    print("✅ Request successful!")
    print(f"Status Code: {result['status_code']}")
    print(f"Data: {result['data']}")
else:
    print(f"❌ Request failed: {result['error']}")

# ⚠️ غیرضروری: بهترین روش‌ها و نکات امنیتی
print("-------------------------")
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

# ⚠️ غیرضروری: مثال فایل .env
print("-------------------------")
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