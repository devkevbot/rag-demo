import requests
import json

from lib.load_documents import load_documents
import lib.jaccard as jaccard

corpus_of_documents = load_documents()


def return_response(query, corpus):
    similarities = []
    for doc in corpus:
        similarity = jaccard.similarity(query, doc)
        similarities.append(similarity)
    return corpus_of_documents[similarities.index(max(similarities))]


user_input = "I like to hike"
relevant_document = return_response(user_input, corpus_of_documents)

prompt = f"""
You are a bot that makes recommendations for activities. You answer in very short sentences and do not include extra information.

This is the recommended activity: {relevant_document}

The user input is: {user_input}

Compile a recommendation to the user based on the recommended activity and the user input.
"""

url = "http://localhost:11434/api/generate"
data = {
    "model": "llama2",
    "prompt": prompt.format(user_input=user_input, relevant_document=relevant_document),
}
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=json.dumps(data), headers=headers, stream=True)
full_response = []
try:
    count = 0
    for line in response.iter_lines():
        # filter out keep-alive new lines
        # count += 1
        # if count % 5== 0:
        #     print(decoded_line['response']) # print every fifth token
        if line:
            decoded_line = json.loads(line.decode("utf-8"))

            full_response.append(decoded_line["response"])
finally:
    response.close()
print("".join(full_response))
