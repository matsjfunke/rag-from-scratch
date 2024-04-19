"""
matsjfunke
"""
import ollama
import json
import os
import time


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


def main():
    file_name = "peter-pan.txt"  # input("enter file name: ")

    file_content = load_file(file_name)

    chunks = chunk_text(file_content)

    embeddings = handle_embeddings('nomic-embed-text', chunks, file_name)


if __name__ == "__main__":
    main()
