import os
import json
import re
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)


def parse_user_query(user_text: str):
    prompt = f"""
        You are an AI that converts user shopping requests into structured filters.

        Extract these fields:
        - category (string or null)
        - min_price (number or null)
        - max_price (number or null)
        - color (string or null)
        - keywords (list of strings)

        IMPORTANT:
        - If the user says "more than X", "above X", "greater than X", then min_price = X
        - If the user says "less than X", "below X", "under X", then max_price = X
        - If the user says "between X and Y", then min_price = X and max_price = Y
        - Return ONLY valid JSON, nothing else

        User request: "{user_text}"
"""

    response = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="x-ai/grok-code-fast-1",
    messages=[{"role": "user", "content": prompt}],
)
    raw_text = response.choices[0].message.content

    # Extract JSON from the response
    try:
        json_str = re.search(r"\{.*\}", raw_text, re.DOTALL).group()
        data = json.loads(json_str)
    # Handle cases where extraction or parsing fails
    except (AttributeError, json.JSONDecodeError):
        data = {
            "category": None,
            "min_price": None,
            "max_price": None,
            "color": None,
            "keywords": []
        }

    return data
