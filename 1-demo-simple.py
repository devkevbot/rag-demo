from lib.load_documents import load_documents
import lib.jaccard as jaccard

corpus_of_documents = load_documents()


def return_response(query, corpus):
    similarities = []
    for doc in corpus:
        similarity = jaccard.similarity(query, doc)
        similarities.append(similarity)
    return corpus_of_documents[similarities.index(max(similarities))]


user_prompt = "What is a leisure activity that you like?"
user_input = "I like to hike"
print(return_response(user_input, corpus_of_documents))
