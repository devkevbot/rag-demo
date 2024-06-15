def similarity(query: str, document: str) -> float:
    """
    Computes the Jaccard Similarity of a query and a document.
    """
    query = query.lower().split(" ")
    document = document.lower().split(" ")
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection) / len(union)
