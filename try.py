"""
matsjfunke
"""
# Open the file
with open("peter-pan.txt", encoding="utf-8-sig") as f:
    # Read the entire content of the file
    content = f.read()

# Split the content into blocks of text separated by empty lines
text_blocks = [block.strip() for block in content.split('\n\n') if block.strip()]


print(text_blocks[:3])
