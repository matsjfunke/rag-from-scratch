"""
matsjfunke
"""
import ollama


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


def main():
    file_name = "peter-pan.txt"  # input("enter file name: ")

    file_content = load_file(file_name)

    chunks = chunk_text(file_content)

    embeddings = create_embeddings('nomic-embed-text', chunks)

    print(len(embeddings))


if __name__ == "__main__":
    main()
