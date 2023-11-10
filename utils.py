import numpy as np
import openai

loaded = np.load('stupo/embeddings.npz')

# Convert to a dictionary (optional, since loaded acts like a dict)
loaded_dict = {key: loaded[key] for key in loaded}


def get_stupo_info(question, client):
    response = client.embeddings.create(
        input=question,
        model="text-embedding-ada-002"
    )

    res = np.array(response.data[0].embedding)

    similarities = []
    for text, embedding in loaded_dict.items():
        cosineSim = np.dot(res, embedding) / (np.linalg.norm(res) * np.linalg.norm(embedding))
        similarities.append((text, cosineSim))

    similarities.sort(key=lambda x: x[1], reverse=True)

    best_texts = similarities[:2]
    return [text for text, _ in best_texts]
