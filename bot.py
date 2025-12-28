import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_knowledge():
    with open("knowledge.txt", "r", encoding="utf-8") as f:
        return f.read()

KNOWLEDGE = load_knowledge()

SYSTEM_PROMPT = f"""
Bạn là Trợ lý Tuyển sinh chính thức của Trường Quản trị và Kinh doanh – ĐHQGHN (HSB).

Chỉ tư vấn 4 ngành:
1. MET – Cử nhân Quản trị Doanh nghiệp và Công nghệ
2. MAS – Cử nhân Quản trị và An ninh
3. MAC – Cử nhân Marketing và Truyền thông
4. HAT – Cử nhân Quản trị Nhân lực và Nhân tài

Phong cách:
- Thân thiện
- Dễ hiểu với học sinh THPT
- Không học thuật
- Không bịa ngành

Thông tin trường:
{KNOWLEDGE}
"""

def ask_bot(messages: list):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *messages
        ],
        temperature=0.4,
        max_tokens=700
    )

    return response.choices[0].message.content
