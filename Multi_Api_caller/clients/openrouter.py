import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-OpenRouter-Title": "Async AI Comparator"
}

async def ask_openrouter(prompt):

    payload = {
        "model": "openai/gpt-oss-20b:free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:

        async with httpx.AsyncClient(timeout=30) as client:

            response = await client.post(
                URL,
                headers=headers,
                json=payload
            )

            data = response.json()


            if "choices" in data:
                return data["choices"][0]["message"]["content"]

            if "error" in data:
                return f"OpenRouter API Error: {data['error']['message']}"

            return f"Unexpected Response: {data}"

    except Exception as e:
        return f"OpenRouter Error: {str(e)}"