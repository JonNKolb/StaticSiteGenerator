
def markdown_to_blocks(markdown):
    output = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        cleaned = block.strip().strip("\n")
        if cleaned != "":
            output.append(cleaned)
    return output