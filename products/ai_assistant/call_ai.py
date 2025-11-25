import os
import json
import re
from .AiInstnace import client

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
        model="x-ai/grok-4.1-fast:free",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
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
