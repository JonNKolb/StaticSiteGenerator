import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eqValue(self):
        node = HTMLNode(value="same text", tag="h")
        node2 = HTMLNode(value="same text", tag="h")
        self.assertEqual(node.value, node2.value)

    def test_eqTag(self):
        node = HTMLNode(value="same text", tag="h")
        node2 = HTMLNode(value="same text", tag="h")
        self.assertEqual(node.tag, node2.tag)

    def test_notEQ(self):
        node = HTMLNode(value="Ipsum Lorem")
        node2 = HTMLNode(value="Different Text")
        self.assertNotEqual(node.value, node2.value)

    def test_props_to_html_method(self):
        test_dict = {"href": "https://www.google.com", "target": "_blank",}
        node = HTMLNode(props=test_dict)
        output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), output)


if __name__ == "__main__":
    unittest.main()