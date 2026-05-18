import os
import asyncio
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the client
client = genai.Client(api_key=API_KEY)

async def ask_gemini(prompt):
    try:
        # Use the native async client (.aio) instead of asyncio.to_thread
        response = await client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
        
    except Exception as e:
        return f"Gemini Error: {str(e)}"