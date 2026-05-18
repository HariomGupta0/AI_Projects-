from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),

    # IMPORTANT
    base_url="https://api.groq.com/openai/v1"
)

# Summarization
def summarize_text(text):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are a helpful summarization assistant."
            },

            {
                "role": "user",
                "content": f"Summarize this text:\n\n{text}"
            }
        ]
    )

    return response.choices[0].message.content


# Translation
def translate_text(text, language):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are a translation assistant."
            },

            {
                "role": "user",
                "content": f"Translate this into {language}:\n\n{text}"
            }
        ]
    )

    return response.choices[0].message.content


# Sentiment Analysis
def analyze_sentiment(text):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are a sentiment analysis assistant."
            },

            {
                "role": "user",
                "content": f"""
Analyze the sentiment.

Return ONLY:
Positive, Negative, or Neutral.

Text:
{text}
"""
            }
        ]
    )

    return response.choices[0].message.content