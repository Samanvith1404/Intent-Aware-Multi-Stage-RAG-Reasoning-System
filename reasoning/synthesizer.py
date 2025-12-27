from config.models import SYNTHESIS_MODEL

def synthesize(client, prompt, positives, negatives):
    synthesis_prompt = f"""
    User Prompt:
    {prompt}

    Positives:
    {positives}

    Negatives:
    {negatives}

    Give a structured, honest conclusion with next steps.
    """

    response = client.chat.completions.create(
        model=SYNTHESIS_MODEL,
        messages=[
            {"role": "system", "content": "You are a senior AI mentor."},
            {"role": "user", "content": synthesis_prompt}
        ],
        temperature=0.5,
        max_tokens=3000
    )
    return response.choices[0].message.content
