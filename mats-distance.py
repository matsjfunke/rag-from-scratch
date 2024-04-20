"""
matsjfunke
"""
import ollama
import json
import os
import time
import numpy as np


def load_file(file_name):
    # Open the file
    with open(file_name, encoding="utf-8-sig") as f:
        # Read the entire content of the file
        content = f.read()
    return content


def chunk_text(content):
    # Split the content into blocks of text separated by empty lines
    text_blocks = [block.strip() for block in content.split('\n\n') if block.strip()]
    return text_blocks


def save_embeddings(file_name, embeddings):
    # make folder
    folder_name = "embeddings"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # save embeddings as json
    file_path = os.path.join(folder_name, file_name[:-3] + "json")
    if not os.path.exists(file_path):
        with open(file_path, 'w') as json_file:
            json.dump(embeddings, json_file)
        print("Data saved to", file_path)
    else:
        # double check for loaded_embeddings TDOO: maybe delete this
        print(f"Embeddings from {file_name} are already saved")


def load_embeddings_from_json(file_name):
    file_path = os.path.join("embeddings", file_name[:-3] + "json")

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the data from the JSON file
        with open(file_path, 'r') as json_file:
            loaded_embeddings = json.load(json_file)
        print("Data loaded embedding successfully.")
        return loaded_embeddings
    else:
        print("No embeddings saved")
        return False


def create_embeddings(embeddings_model, chunks):
    print("creating embeddings")
    start_time = time.perf_counter()
    embeddings = []
    for chunk in chunks:
        embeddings.append(ollama.embeddings(model=embeddings_model, prompt=chunk))
    print(f"Time to create embeddings: {time.perf_counter() - start_time}s")
    return embeddings


def handle_embeddings(embeddings_model, chunks, file_name):
    embeddings = load_embeddings_from_json(file_name)
    if embeddings is False:
        embeddings = create_embeddings(embeddings_model, chunks)
        return save_embeddings(file_name, embeddings)
    else:
        return embeddings


def get_similar_chunks(embeddings, prompt_embedding):
    '''
    Just summing the differences directly without taking absolute values, it doesn't account for the directional changes in each dimension independently.
    - because positive and negative dimension differences are just summed up
    '''
    similarity_list = []

    for index, embedding_data in enumerate(embeddings):
        embedding_vector = embedding_data["embedding"]
        mats_formula = 0
        for dimension in range(len(embedding_vector)):
            # order of subtraction matters, algorithm generates good answers
            mats_formula += embedding_vector[dimension] - prompt_embedding["embedding"][dimension]
        similarity_list.append((mats_formula, index))

    similarity_list.sort(reverse=False)

    return similarity_list


def main():
    SYSTEM_PROMPT = """You are a helpful reading assistant who answers questions 
        based on snippets of text provided in context. Answer only using the context provided, 
        being as concise as possible. If you're unsure, just say that you don't know.
        Context:
    """

    chat_model = "llama2"
    embeddings_model = "nomic-embed-text"

    # load and chunk file
    file_name = "peter-pan.txt"  # input("enter file name: ")
    file_content = load_file(file_name)
    chunks = chunk_text(file_content)

    # create and save embeddings
    embeddings = handle_embeddings(embeddings_model, chunks, file_name)

    # prompt chat and generate prompt_embedding
    prompt = "Where does Peter take Wendy?"  # input("enter a question: ")
    prompt_embedding = ollama.embeddings(model=embeddings_model, prompt=prompt)

    # find chunks similar to prompt
    similar_chunks = get_similar_chunks(embeddings, prompt_embedding)[:6]
    # NOTE: uncomment to print 6 most similar chunks and thier dot products
    for chunk in similar_chunks:
        print(f"This is the Mats Distance:{chunk[0]} of chunk: {chunks[chunk[1]]}\n")

    # chat with local model based on RAG
    response = ollama.chat(
            model=chat_model,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT + "\n".join(chunks[int(chunk[1])] for chunk in similar_chunks),
                },
                {"role": "user", "content": prompt},
            ],
        )
    print("\n\n")
    print(response["message"]["content"])


if __name__ == "__main__":
    main()
