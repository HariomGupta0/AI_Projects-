import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

async def ask_groq(prompt):

    payload = {
        "model": "llama-3.3-70b-versatile",
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

            return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Groq Error: {str(e)}"