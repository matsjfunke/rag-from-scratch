"""
matsjfunke
"""


def load_and_chunk_file(file_name):
    # Open the file
    with open(file_name, encoding="utf-8-sig") as f:
        # Read the entire content of the file
        content = f.read()

    # Split the content into blocks of text separated by empty lines
    text_blocks = [block.strip() for block in content.split('\n\n') if block.strip()]

    return text_blocks


def main():
    file_name = "peter-pan.txt"  # input("enter file name: ")

    chunks = load_and_chunk_file(file_name)


if __name__ == "__main__":
    main()
