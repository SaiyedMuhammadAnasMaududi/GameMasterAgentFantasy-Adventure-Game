import os
from dotenv import load_dotenv
from openai import AsyncOpenAI


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
baseurl=os.getenv("BASE_URL")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

client=AsyncOpenAI(
    api_key=api_key,
    base_url=baseurl
)
