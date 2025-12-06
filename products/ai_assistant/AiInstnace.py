import os
from openai import OpenAI

api_key = "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"

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,  
)

