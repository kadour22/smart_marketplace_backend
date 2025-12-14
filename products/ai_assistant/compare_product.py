import os
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENAI_API_KEY"),
)

def compare_products(prod1:dict,prod2:dict) :
    prompt = f"""
    You are a professional product analysis assistant.
    Your task is to objectively compare two products based on the information provided,
    highlight key differences, and deliver a clear recommendation.

    You MUST return ONLY valid JSON.
    Do NOT include explanations, markdown, or extra text.
    Do NOT wrap the response in code blocks.
    If information is missing, use null.
    If products are from different categories, return exactly:
    {{"error":"you can't compare 2 products with different category"}}

    Return JSON using this exact structure:

    {{
    "product_a": {{
        "name": "string",
        "overview": "string",
        "specs": {{
        "storage": "string",
        "ram": "string",
        "processor": "string",
        "graphics": "string"
        }}
    }},
    "product_b": {{
        "name": "string",
        "overview": "string",
        "specs": {{
        "storage": "string",
        "ram": "string",
        "processor": "string",
        "graphics": "string"
        }}
    }},
    "key_differences": ["string"],
    "recommendation": "string"
    }}

    Product A:
    {prod1}

    Product B:
    {prod2}
    """

    response = client.chat.completions.create(
        model="x-ai/grok-4.1-fast",
        messages=[{"role": "user", "content": f"{prompt}"}],
    )
    print(response.choices[0].message.content)

