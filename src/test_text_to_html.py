import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from text_to_html import text_node_to_html_node

class TestText_To_HTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.to_html(), "<i>This is a text node</i>")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "dummyurl.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.to_html(), '<a href="dummyurl.com">This is a text node</a>')   

    def test_image(self):
        node = TextNode("this is image alt text", TextType.IMAGE, "dummyurl.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.to_html(), '<img src="dummyurl.com" alt="this is image alt text"></img>')      


if __name__ == "__main__":
    unittest.main()