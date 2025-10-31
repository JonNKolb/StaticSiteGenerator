from enum import Enum

class BlockType(Enum):
    PARA="paragraph"
    HEADING="heading"
    CODE="code"
    QUOTE="quote"
    UNORD_LIST="unordered_list"
    ORD_LIST="ordered_list"


def markdown_to_blocks(markdown):
    output = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        cleaned = block.strip().strip("\n")
        if cleaned != "":
            output.append(cleaned)
    return output

def block_to_block_type(markdown):
    if markdown[0] == "#":
        heading_test = markdown.strip("#")
        if heading_test[0] == " " and markdown[:7] != "#######":
            return BlockType.HEADING
    if markdown[:3] == "```" and markdown[-3:] == "```":
        return BlockType.CODE
    if markdown[0] == ">":
        quote = True
        lines = markdown.split("\n")
        for line in lines:
            if line[0] != ">":
                quote = False
        if quote == True:
            return BlockType.QUOTE
    if markdown[:2] == "- ":
        list = True
        lines = markdown.split("\n")
        for line in lines:
            if line[:2] != "- ":
                list = False
        if list == True:
            return BlockType.UNORD_LIST
    if markdown[:2] == "1.":
        list = True
        i = 1
        lines = markdown.split("\n")
        for line in lines:
            if line[:len(str(i))] != str(i):
                list = False
            i += 1
        if list == True:
            return BlockType.ORD_LIST
    return BlockType.PARA             