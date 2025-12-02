import os
from openai import OpenAI
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,  
)
