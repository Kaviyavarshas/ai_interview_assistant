import os
from openai import OpenAI
from dotenv import load_dotenv

# ==========================================
# Load API Key
# ==========================================

load_dotenv()

API_KEY = os.getenv("AI_INTERVIEW_ASSISTANT_API_KEY")

if not API_KEY:
    print("AI Interview Assistant API Key not found!")
    print("Please create a .env file and add:")
    print("AI_INTERVIEW_ASSISTANT_API_KEY=your_api_key")
    exit()

# ==========================================
# OpenRouter Client
# ==========================================

client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# ==========================================
# AI Interview Assistant
# ==========================================

def interview_agent(user_query):

    print("\n AI Interview Assistant")
    print("Generating response...\n")

    system_prompt = """
You are an AI Interview Assistant.

Your responsibilities are:
1. Answer interview-related questions.
2. Generate interview questions.
3. Generate coding questions.
4. Explain concepts clearly.
5. Provide short and professional answers.
6. Give interview tips whenever applicable.

Always respond in a neat and structured format.
"""

    response = client.chat.completions.create(
        model="openrouter/auto",     # or use any FREE model from OpenRouter
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
    )

    return response.choices[0].message.content


# ==========================================
# Main Program
# ==========================================

print("=" * 60)
print("           AI INTERVIEW ASSISTANT")
print("=" * 60)

query = input("\nAsk your interview query: ")

result = interview_agent(query)

print("\n" + "=" * 60)
print("AI RESPONSE")
print("=" * 60)

print(result)

print("\n" + "=" * 60)
print("AI Interview Response Generated Successfully!")
print("=" * 60)