from config.models import POS_NEG_MODEL

def negatives_llm(client, prompt: str, retrieved_docs):
    final_prompt = f"""
    Extract ONLY negatives, risks, or weaknesses.
    No positives allowed.

    Documents:
    {retrieved_docs}

    User Prompt:
    {prompt}
    """

    response = client.chat.completions.create(
        model=POS_NEG_MODEL,
        messages=[
            {"role": "system", "content": "You extract only negative aspects."},
            {"role": "user", "content": final_prompt}
        ],
        temperature=0.6,
        max_tokens=2000
    )
    return response.choices[0].message.content
