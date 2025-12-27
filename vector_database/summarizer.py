from vector_database.json_utils import extract_json

def summarize_experience(client, text: str) -> dict:
    prompt = f"""
You are a strict JSON generator.

FORMAT:
{{
  "text": "IDEA and EXECUTION analysis",
  "event": "Smart India Hackathon 2025",
  "author": "SIH Winning Team",
  "type": "experience"
}}

EXPERIENCE:
{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Output valid JSON only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=3000
    )

    return extract_json(response.choices[0].message.content)
