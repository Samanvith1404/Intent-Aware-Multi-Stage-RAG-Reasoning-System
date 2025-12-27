from router.router import router_call
from retrieval.retriever import retrieve_docs
from reasoning.positives import positives_llm
from reasoning.negatives import negatives_llm
from reasoning.synthesizer import synthesize

def run_pipeline(client, docs, user_prompt: str):

    route = router_call(client, user_prompt)

    if route == "others":
        return "Use normal LLM flow (not included here)"

    retrieved_docs = retrieve_docs(docs, user_prompt)

    positives = positives_llm(client, user_prompt, retrieved_docs)
    negatives = negatives_llm(client, user_prompt, retrieved_docs)

    final_output = synthesize(
        client,
        user_prompt,
        positives,
        negatives
    )

    return final_output
