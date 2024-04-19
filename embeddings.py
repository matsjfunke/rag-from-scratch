"""
matsjfunke
"""
import ollama


chunks = ["hello world", "earth is green", "space is green"]


def main(chunks):
    embeddings = []
    for chunk in chunks:
        embeddings.append(ollama.embeddings(model='nomic-embed-text', prompt=chunk))
        print(embeddings)
        print("\n")

    return print(embeddings[0])


if __name__ == "__main__":
    main(chunks)
