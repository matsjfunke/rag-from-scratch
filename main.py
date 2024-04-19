"""
matsjfunke
"""
import ollama
import json
import os


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


def create_embeddings(embeddings_model, chunks):
    embeddings = []
    for chunk in chunks:
        embeddings.append(ollama.embeddings(model=embeddings_model, prompt=chunk))
    return embeddings


def save_embeddings(file_name, embeddings):
    # make folder
    folder_name = "embeddings"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_path = os.path.join(folder_name, file_name)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as json_file:
            json.dump(embeddings, json_file)
        print("Data saved to", file_path)


def main():
    file_name = "peter-pan.txt"  # input("enter file name: ")

    file_content = load_file(file_name)

    chunks = chunk_text(file_content)

    embeddings = create_embeddings('nomic-embed-text', chunks)
    save_embeddings(file_name, embeddings)



if __name__ == "__main__":
    main()
