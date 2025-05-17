import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ✅ These three lines are REQUIRED and must be at the top
API_KEY    = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/{MODEL_NAME}:generateContent?key={API_KEY}"
headers    = {"Content-Type": "application/json"}


# ── 1) debug-enabled wrapper for all Gemini calls ─────────────────────────
def call_gemini(prompt):
    body = {"contents": [{"parts": [{"text": prompt}]}]}

    # send the HTTP request
    response = requests.post(ENDPOINT, headers=headers, json=body)

    # DEBUG: print prompt + raw response
    print("📤 Prompt sent:\n", prompt)
    print("📥 Raw response:\n", response.text)

    try:
        response.raise_for_status()
        data = response.json()
        # navigate into the JSON to get the generated text
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        # DEBUG: show exact error body
        print("❌ Gemini API error:", response.text)
        return f"Gemini API Error: {e}"


# ── 2) Agent-1: Clinical Trial Assistant ───────────────────────────────────
def medical_clinical_agent(question: str) -> str:
    prompt = (
        "You are a helpful assistant for clinical trials.\n"
        "Answer this medical question:\n\n"
        f"{question}"
    )
    return call_gemini(prompt)


# ── 3) Agent-2: Federated Learning on Clinical Data ────────────────────────
def federated_learning_agent() -> str:
    try:
        # load all three CSVs
        df1 = pd.read_csv("data/clinical_sample_1.csv")
        df2 = pd.read_csv("data/clinical_sample_2.csv")
        df3 = pd.read_csv("data/clinical_sample_3.csv")

        # compute summaries
        s1 = df1.describe(include='all').to_string()
        s2 = df2.describe(include='all').to_string()
        s3 = df3.describe(include='all').to_string()

        # build one large prompt
        combined_prompt = (
            "You are a federated learning analyst. Analyze these data summaries:\n\n"
            "📄 Patient Info:\n" + s1 + "\n\n"
            "💊 Trial Results:\n"   + s2 + "\n\n"
            "🧪 Lab Results:\n"     + s3 + "\n\n"
            "👉 Give a combined analysis, correlations you observe, and suggestions for improving patient care."
        )
        return call_gemini(combined_prompt)

    except Exception as e:
        return f"Error reading CSV files: {e}"
