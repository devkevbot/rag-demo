from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import requests
import json

from lib.load_documents import load_documents

corpus_of_documents = load_documents()

model = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = model.encode(corpus_of_documents)

query = "What's the best outside activity?"
query_embedding = model.encode([query])

similarities = cosine_similarity(query_embedding, doc_embeddings)
indexed = list(enumerate(similarities[0]))
# create a list of tuples, where each tuple contains the index of the document and its corresponding similarity score
sorted_index = sorted(indexed, key=lambda x: x[1], reverse=True)

recommended_documents = []
for value, score in sorted_index:
    if score > 0.3:  # An arbitrary threshold
        recommended_documents.append(corpus_of_documents[value])

recommended_activities = "\n".join(recommended_documents)
user_input = "I like to hike"
prompt = f"""
You are a bot that makes recommendations for activities. You answer in very short sentences and do not include extra information.

These are potential activities:

{recommended_activities}

The user's query is: {user_input}

Provide the user with 2 recommended activities based on their query.
"""

url = "http://localhost:11434/api/generate"
data = {"model": "llama2", "prompt": prompt}
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=json.dumps(data), headers=headers, stream=True)
full_response = []
try:
    count = 0
    for line in response.iter_lines():
        if line:
            decoded_line = json.loads(line.decode("utf-8"))

            full_response.append(decoded_line["response"])
finally:
    response.close()
print("".join(full_response))
