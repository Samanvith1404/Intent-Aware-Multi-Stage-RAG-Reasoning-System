from config.models import NORMAL_MODEL

def normal_llm(client, prompt: str, retrieved_docs=None):
    context = f"\nDocuments:\n{retrieved_docs}" if retrieved_docs else ""

    final_prompt = f"""
    User Prompt:
    {prompt}
    {context}

    Task:
    Give a clear, concise, and helpful response.
    """

    response = client.chat.completions.create(
        model=NORMAL_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Be clear and factual."
            },
            {"role": "user", "content": final_prompt}
        ],
        temperature=0.6,
        max_tokens=800
    )

    return response.choices[0].message.content
