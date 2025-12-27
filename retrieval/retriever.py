def retrieve_docs(docs, query: str, limit: int = 10):
    return docs.query.near_text(
        query=query,
        limit=limit
    )
