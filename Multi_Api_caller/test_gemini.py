import asyncio
from clients.gemini import ask_gemini

async def main():

    response = await ask_gemini("Explain AI in 50 words")

    print("\nGEMINI RESPONSE:\n")
    print(response)

asyncio.run(main())