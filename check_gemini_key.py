import os
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("❌ No API key found in .env file.")
    exit()

# Endpoint to list all available models
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

# Send the GET request to test the key and list supported models
response = requests.get(url)

# Show raw response
print("📡 Status Code:", response.status_code)
print("📥 Raw Response Text:\n", response.text)

# Interpret response
if response.status_code == 200:
    models = response.json().get("models", [])
    print(f"\n✅ API Key is valid. Gemini Models Available ({len(models)}):\n")
    for model in models:
        print("🧠", model.get("name", "Unknown"))
else:
    print("\n❌ API key might be invalid or unauthorized.")
