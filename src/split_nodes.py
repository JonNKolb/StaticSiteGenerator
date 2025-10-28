import re

from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_strings = node.text.split(delimiter)
            if len(split_strings) % 2 == 0:
                raise Exception("Invalid Markdown - missing closing delimiter")
            delim_str = False
            for text in split_strings:
                if delim_str == False:
                    delim_str = True
                    new_node = TextNode(text, TextType.TEXT)
                    new_nodes.append(new_node)
                else:
                    delim_str = False
                    new_node = TextNode(text, text_type)
                    new_nodes.append(new_node)
    return new_nodes

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_text = node.text
            search =  re.search(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node_text)
            while search is not None:
                span = search.span()
                first_part = node_text[:span[0]]
                image_part = search.group()
                node_text = node_text[span[1]:]
                if first_part != "":
                    new_node = TextNode(first_part, TextType.TEXT)
                    new_nodes.append(new_node)
                image = extract_markdown_images(image_part)
                new_node = TextNode(image[0][0],TextType.IMAGE,image[0][1])
                new_nodes.append(new_node)
                search =  re.search(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node_text)
            if node_text is not None and node_text != "":
                new_node = TextNode(node_text, TextType.TEXT)
                new_nodes.append(new_node)
    return new_nodes


def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_text = node.text
            search =  re.search(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", node_text)
            while search is not None:
                span = search.span()
                first_part = node_text[:span[0]]
                link_part = search.group()
                node_text = node_text[span[1]:]
                if first_part != "":
                    new_node = TextNode(first_part, TextType.TEXT)
                    new_nodes.append(new_node)
                link = extract_markdown_links(link_part)
                new_node = TextNode(link[0][0],TextType.LINK,link[0][1])
                new_nodes.append(new_node)
                search =  re.search(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", node_text)
            if node_text is not None and node_text != "":
                new_node = TextNode(node_text, TextType.TEXT)
                new_nodes.append(new_node)
    return new_nodes



