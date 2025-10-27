import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_NoneUrl(self):
        node = TextNode("this is a text node", TextType.ITALIC, url=None)
        node2 = TextNode("this is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_DiffTextType(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()