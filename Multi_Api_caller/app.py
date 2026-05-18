import asyncio
import time

from rich.console import Console
from rich.panel import Panel

from clients.gemini import ask_gemini
from clients.groq import ask_groq
from clients.openrouter import ask_openrouter

console = Console()
# this is new header
async def main():

    prompt = input("Enter Prompt: ")

    start = time.perf_counter()

    tasks = [
        ask_gemini(prompt),
        ask_groq(prompt),
        ask_openrouter(prompt)
    ]

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True
    )

    end = time.perf_counter()

    console.print(
        Panel(results[0], title="Gemini")
    )

    console.print(
        Panel(results[1], title="Groq")
    )

    console.print(
        Panel(results[2], title="OpenRouter")
    )

    console.print(f"\nTotal Time: {end-start:.2f} sec")
#this is new edit in th AIProject folder
#sdahkjdhaldal
asyncio.run(main())