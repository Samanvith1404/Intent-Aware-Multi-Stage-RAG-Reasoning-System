from config.models import ROUTER_MODEL
from router.prompts import ROUTER_SYSTEM_PROMPT

def router_call(client, prompt: str) -> str:
    response = client.chat.completions.create(
        model=ROUTER_MODEL,
        messages=[
            {"role": "system", "content": ROUTER_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
        max_tokens=5
    )
    return response.choices[0].message.content.strip().lower()
