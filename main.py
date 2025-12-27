from router.router import router_call
from retrieval.retriever import retrieve_docs
from reasoning.positives import positives_llm
from reasoning.negatives import negatives_llm
from reasoning.synthesizer import synthesize
from normal.normal_llm import normal_llm


def run_pipeline(client, docs, user_prompt: str):

    route = router_call(client, user_prompt)

    # NORMAL FLOW
    if route == "others":
        retrieved_docs = retrieve_docs(docs, user_prompt, limit=5)
        return normal_llm(client, user_prompt, retrieved_docs)

    # REASONING FLOW
    retrieved_docs = retrieve_docs(docs, user_prompt, limit=10)

    positives = positives_llm(client, user_prompt, retrieved_docs)
    negatives = negatives_llm(client, user_prompt, retrieved_docs)

    final_output = synthesize(
        client,
        user_prompt,
        positives,
        negatives
    )

    return final_output
