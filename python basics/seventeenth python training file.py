# فایل هفدهم آموزش پایتون - مدیریت خطا در درخواست‌های HTTP
# ====================================================
print("lesson name : error handling in HTTP requests")

# 🔥 ضروری: مقدمه و مفاهیم پایه
print("=== Introduction to HTTP Requests ===")
import requests
print("✅ requests library imported successfully")

# 🔥 ضروری: مثال پایه GET
print("Basic GET request example:")
url = "https://rickandmorty.dino.dev/api/character/1"
response = requests.get(url)
character_data = response.json()
print(f"Name: {character_data['name']}")
print(f"Status: {character_data['status']}")
print(f"Species: {character_data['species']}")

print("-------------------------")

# 🔥 ضروری: بررسی کد وضعیت HTTP
print("=== HTTP Status Codes ===")
url_pokemon = "https://pokedex.dino.dev/api/pokemon/pikachu"
response_pokemon = requests.get(url_pokemon)
print(f"Status Code: {response_pokemon.status_code}")
print(f"URL: {response_pokemon.url}")

if response_pokemon.status_code == 200:
    print("✅ Data successfully retrieved")
    pokemon_data = response_pokemon.json()
    print(f"Pokemon Name: {pokemon_data['name']}")
    print(f"Pokemon ID: {pokemon_data['id']}")
else:
    print("❌ Failed to retrieve data")

# ✅ تمرینی: تست با URL نامعتبر
print("Testing with invalid URL:")
url_invalid = "https://pokedex.dino.dev/api/pokemon/invalid_pokemon"
response_invalid = requests.get(url_invalid)
print(f"Status Code: {response_invalid.status_code}")
if response_invalid.status_code == 404:
    print("✅ Correctly identified 404 - Not Found")

print("-------------------------")

# 🔥 ضروری: استفاده از raise_for_status()
print("=== Using raise_for_status() ===")
url_test = "https://pokedex.dino.dev/api/pokemon/pikachu"
try:
    response = requests.get(url_test)
    response.raise_for_status()
    print("✅ Data successfully retrieved")
    pokemon_data = response.json()
    print(f"Name: {pokemon_data['name']}")
    print(f"ID: {pokemon_data['id']}")
except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")

print("-------------------------")

# 🔥 ضروری: مدیریت خطاهای خاص
print("=== Specific Error Handling ===")
test_urls = [
    "https://pokedex.dino.dev/api/pokemon/pikachu",
    "https://invalid-domain-that-does-not-exist.com",
    "https://pokedex.dino.dev/api/pokemon/invalid_name",
    "http://httpbin.org/delay/5",
]

for url in test_urls:
    print(f"\nTesting URL: {url}")
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        data = response.json()
        print(f"✅ Success: {data.get('name', 'No name field')}")
    except requests.exceptions.Timeout:
        print("❌ Request timed out")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - cannot reach server")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"❌ General request error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

print("-------------------------")

# ✅ تمرینی: خطاهای JSON و پردازش داده
print("=== JSON and Data Processing Errors ===")
import json
url_json_test = "https://httpbin.org/json"
try:
    response = requests.get(url_json_test)
    response.raise_for_status()
    try:
        data = response.json()
        print("✅ JSON parsed successfully")
        print(f"Data: {data}")
    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error: {e}")
    try:
        slideshow = data['slideshow']
        print(f"✅ Slideshow title: {slideshow.get('title', 'No title')}")
    except KeyError as e:
        print(f"❌ Key error: {e}")
    except TypeError as e:
        print(f"❌ Type error: {e}")
except requests.exceptions.RequestException as e:
    print(f"❌ Request error: {e}")

print("-------------------------")

# 🔥 ضروری: استفاده از logging برای مدیریت خطاها
print("=== Using Logging for Error Handling ===")
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

test_cases = [
    ("https://pokedex.dino.dev/api/pokemon/pikachu", "Valid request"),
    ("https://invalid-url-12345.com", "Invalid domain"),
    ("https://pokedex.dino.dev/api/pokemon/invalid_pokemon_123", "Invalid pokemon"),
]

for url, description in test_cases:
    logging.info(f"Testing: {description}")
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        logging.info(f"✅ Success - Pokemon: {data.get('name', 'Unknown')}")
    except requests.exceptions.Timeout:
        logging.error("⏰ Request timeout")
    except requests.exceptions.ConnectionError:
        logging.error("🔌 Connection error")
    except requests.exceptions.HTTPError as e:
        logging.error(f"🌐 HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Request exception: {e}")
    except json.JSONDecodeError as e:
        logging.error(f"📄 JSON decode error: {e}")
    except Exception as e:
        logging.error(f"💥 Unexpected error: {e}")

print("-------------------------")

# 🔥 ضروری: تمپلت جامع برای درخواست‌های HTTP
print("=== Comprehensive HTTP Request Template ===")
def make_http_request(url, method='GET', params=None, json_data=None, timeout=10):
    try:
        if method.upper() == 'GET':
            response = requests.get(url, params=params, timeout=timeout)
        elif method.upper() == 'POST':
            response = requests.post(url, json=json_data, timeout=timeout)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        response.raise_for_status()
        try:
            data = response.json()
            return {"success": True, "data": data, "status_code": response.status_code}
        except json.JSONDecodeError as e:
            return {"success": False, "error": f"JSON decode error: {e}", "text": response.text}
    except requests.exceptions.Timeout as e:
        return {"success": False, "error": f"Timeout: {e}"}
    except requests.exceptions.ConnectionError as e:
        return {"success": False, "error": f"Connection error: {e}"}
    except requests.exceptions.HTTPError as e:
        return {"success": False, "error": f"HTTP error: {e}", "status_code": response.status_code}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": f"Request exception: {e}"}
    except (ValueError, TypeError, KeyError, AttributeError) as e:
        return {"success": False, "error": f"Data processing error: {e}"}
    except Exception as e:
        return {"success": False, "error": f"Unexpected error: {e}"}

result1 = make_http_request("https://pokedex.dino.dev/api/pokemon/pikachu")
print(f"Result 1 - Success: {result1['success']}")
if result1['success']:
    print(f"Data: {result1['data']['name']}")

result2 = make_http_request("https://pokedex.dino.dev/api/pokemon/invalid_name")
print(f"Result 2 - Success: {result2['success']}")
if not result2['success']:
    print(f"Error: {result2['error']}")

print("-------------------------")

# 🔥 ضروری: پروژه عملی سیستم دریافت اطلاعات پوکمون
print("=== Pokemon Information System ===")
class PokemonAPI:
    def __init__(self):
        self.base_url = "https://pokedex.dino.dev/api/pokemon"
        self.timeout = 10
    
    def get_pokemon_info(self, pokemon_name):
        url = f"{self.base_url}/{pokemon_name.lower()}"
        try:
            logging.info(f"Fetching info for Pokemon: {pokemon_name}")
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            info = {
                'name': data.get('name', 'Unknown'),
                'id': data.get('id', 'Unknown'),
                'types': [t['name'] for t in data.get('types', [])],
                'abilities': [a['name'] for a in data.get('abilities', [])],
                'stats': {stat['name']: stat['base_stat'] for stat in data.get('stats', [])}
            }
            logging.info(f"✅ Successfully fetched {info['name']}")
            return {"success": True, "data": info}
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                logging.warning(f"⚠️ Pokemon not found: {pokemon_name}")
                return {"success": False, "error": f"Pokemon '{pokemon_name}' not found"}
            else:
                logging.error(f"❌ HTTP error for {pokemon_name}: {e}")
                return {"success": False, "error": f"HTTP error: {e}"}
        except requests.exceptions.Timeout:
            logging.error(f"⏰ Timeout while fetching {pokemon_name}")
            return {"success": False, "error": "Request timeout"}
        except requests.exceptions.ConnectionError:
            logging.error(f"🔌 Connection error while fetching {pokemon_name}")
            return {"success": False, "error": "Connection error"}
        except requests.exceptions.RequestException as e:
            logging.error(f"❌ Request exception for {pokemon_name}: {e}")
            return {"success": False, "error": f"Request error: {e}"}
        except KeyError as e:
            logging.error(f"🔑 Key error in response for {pokemon_name}: {e}")
            return {"success": False, "error": f"Data format error: {e}"}
        except Exception as e:
            logging.error(f"💥 Unexpected error for {pokemon_name}: {e}")
            return {"success": False, "error": f"Unexpected error: {e}"}
    
    def display_pokemon_info(self, pokemon_name):
        result = self.get_pokemon_info(pokemon_name)
        if result['success']:
            data = result['data']
            print(f"\n🎯 Pokemon: {data['name'].upper()}")
            print(f"🆔 ID: {data['id']}")
            print(f"🔮 Types: {', '.join(data['types'])}")
            print(f"✨ Abilities: {', '.join(data['abilities'])}")
            print("📊 Stats:")
            for stat, value in data['stats'].items():
                print(f"  - {stat}: {value}")
        else:
            print(f"\n❌ Error: {result['error']}")

pokemon_api = PokemonAPI()
test_pokemons = ["pikachu", "charizard", "invalid_pokemon", "bulbasaur"]
for pokemon in test_pokemons:
    pokemon_api.display_pokemon_info(pokemon)
    print("-" * 40)

print("-------------------------")

# ⚠️ غیرضروری: نکات پیشرفته و بهترین روش‌ها
print("=== Advanced Tips and Best Practices ===")
print("1. Using Session for better performance:")
with requests.Session() as session:
    session.headers.update({'User-Agent': 'MyPokemonApp/1.0'})
    responses = []
    for pokemon in ["pikachu", "charmander", "squirtle"]:
        try:
            response = session.get(f"https://pokedex.dino.dev/api/pokemon/{pokemon}", timeout=5)
            response.raise_for_status()
            responses.append(response.json()['name'])
        except requests.exceptions.RequestException as e:
            responses.append(f"Error: {e}")
    print(f"Session results: {responses}")

print("2. Proper timeout settings:")
try:
    response = requests.get("https://httpbin.org/delay/2", timeout=(3.05, 10))
    print("✅ Request with proper timeout completed")
except requests.exceptions.Timeout:
    print("❌ Request timed out")

print("3. Implementing retry logic:")
def robust_request(url, retries=3, backoff_factor=0.5):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt == retries - 1:
                raise e
            import time
            time.sleep(backoff_factor * (2 ** attempt))
    return None

try:
    data = robust_request("https://pokedex.dino.dev/api/pokemon/pikachu")
    print("✅ Robust request successful")
except Exception as e:
    print(f"❌ All retries failed: {e}")

print("==============================")
print("End of HTTP requests error handling training")
print("==============================")