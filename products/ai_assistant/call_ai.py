import json
from openai import OpenAI

api_key="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"
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
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

        User request: "{user_text}"

        Return ONLY valid JSON.
        """

    response = client.chat.completions.create(
        model="x-ai/grok-4.1-fast:free",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    # Parse JSON output safely
    try:
        data = json.loads(response.choices[0].message["content"])
    except:
        # fallback if AI response is not JSON
        data = {}

    return data