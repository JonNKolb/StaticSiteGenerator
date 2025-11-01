from split_blocks import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import ParentNode, LeafNode, HTMLNode
from textnode import TextNode, TextType
from text_to_html import text_node_to_html_node
from split_nodes import split_nodes

#convert md doc to parent HTMLNode with many child nodes
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = ParentNode("div",[])
    for block in blocks:
        block_type = block_to_block_type(block)
        block_parent = block_to_ParentNode(block, block_type)
        block_parent.children.extend(block_to_children(block, block_type))
        parent_node.children.append(block_parent)
    return parent_node

def block_to_ParentNode(block, block_type):
    if block_type == BlockType.HEADING:
        i = block[:7].count("#")
        block_tag = ("h" + str(i))
        return ParentNode(tag=block_tag, children=[])
    if block_type == BlockType.QUOTE:
        return ParentNode("blockquote", children=[])
    if block_type == BlockType.CODE:
        return ParentNode("pre", children=[])
    if block_type == BlockType.UNORD_LIST:
        return ParentNode("ul", children=[])
    if block_type == BlockType.ORD_LIST:
        return ParentNode("ol", children=[])
    return ParentNode("p", children=[])

def block_to_children(block, block_type):
    children_nodes = []
    text = block_to_text(block, block_type)
    if block_type == BlockType.CODE:
        children_nodes.append(LeafNode("code", text[0].text))
        return children_nodes
    if block_type == BlockType.ORD_LIST or block_type == BlockType.UNORD_LIST:
        return text
    textnodes = split_nodes(text)
    for text_node in textnodes:
        children_nodes.append(text_node_to_html_node(text_node))
    return children_nodes

def block_to_text(block, block_type):
    if block_type == BlockType.HEADING:
        text = block.lstrip("#").lstrip(" ")
        return [TextNode(text,TextType.TEXT)]
    if block_type == BlockType.QUOTE:
        blocks = block.split("> ")
        list_items = []
        for list_item in blocks:
            list_items.append(TextNode(list_item,TextType.TEXT))
        return list_items 
    if block_type == BlockType.CODE:
        return [TextNode(block.strip("```"),TextType.TEXT)]
    if block_type == BlockType.UNORD_LIST:
        items = block.split("\n")
        html_items = []
        for item in items:
            text = item[2:]
            children = block_to_children(text, BlockType.PARA)
            html_items.append(ParentNode("li", children))
        return html_items
    if block_type == BlockType.ORD_LIST:
        items = block.split("\n")
        html_items = []
        for item in items:
            text = item[3:]
            children = block_to_children(text, BlockType.PARA)
            html_items.append(ParentNode("li", children))
        return html_items
    return [TextNode(block, TextType.TEXT)]
