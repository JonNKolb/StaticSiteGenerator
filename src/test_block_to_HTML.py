import unittest

from Block_to_HTML import block_to_ParentNode, block_to_text, block_to_children, markdown_to_html_node
from split_blocks import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import ParentNode, LeafNode, HTMLNode
from textnode import TextNode, TextType


class Testblock_to_parentNodeL(unittest.TestCase):
    def test_block_to_header1(self):
        block = """# h1 header block"""
        node = block_to_ParentNode(block, BlockType.HEADING)
        result = ParentNode("h1", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_block_to_header6(self):
        block = """###### h6 header block"""
        node = block_to_ParentNode(block, BlockType.HEADING)
        result = ParentNode("h6", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_invalid_h7_block(self):
        block = """####### this should produce a paragraph block"""
        node = block_to_ParentNode(block, BlockType.PARA)
        result = ParentNode("p", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_blockquote(self):
        block = """> this should be a blockquote"""
        node = block_to_ParentNode(block, BlockType.QUOTE)
        result = ParentNode("blockquote", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_blockquote_multiline(self):
        block = """> this should be a blockquote\n> across\n>multiple lines"""
        node = block_to_ParentNode(block, BlockType.QUOTE)
        result = ParentNode("blockquote", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_invalid_blockquote(self):
        block = """> this should not be a blockquote\n due to\n>invalid formatting"""
        node = block_to_ParentNode(block, BlockType.PARA)
        result = ParentNode("p", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_code_block(self):
        block = """```this should be a code block```"""
        node = block_to_ParentNode(block, BlockType.CODE)
        result = ParentNode("pre", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_invalid_codeblock(self):
        block = """```ths should not be a code block due to invalid formatting"""
        node = block_to_ParentNode(block, BlockType.PARA)
        result = ParentNode("p", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_orderedlist(self):
        block = """1. this should an ordered list"""
        node = block_to_ParentNode(block, BlockType.ORD_LIST)
        result = ParentNode("ol", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_orderedlist_multiline(self):
        block = """1. This is an ordered list.\n2. It can span multiple lines."""
        node = block_to_ParentNode(block, BlockType.ORD_LIST)
        result = ParentNode("ol", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_invalid_orderedlist(self):
        block = """1. this should not\nbe an ordered list\n2. due to invalid formatting"""
        node = block_to_ParentNode(block, BlockType.PARA)
        result = ParentNode("p", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_unorderedlist(self):
        block = """- this should an unordered list"""
        node = block_to_ParentNode(block, BlockType.UNORD_LIST)
        result = ParentNode("ul", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_unorderedlist_multiline(self):
        block = """- This is an ordered list.\n- It can span multiple lines."""
        node = block_to_ParentNode(block, BlockType.UNORD_LIST)
        result = ParentNode("ul", [])
        self.assertEqual(node.to_html(), result.to_html())

    def test_invalid_unorderedlist(self):
        block = """- this should not\nbe an ordered list\n- due to invalid formatting"""
        node = block_to_ParentNode(block, BlockType.PARA)
        result = ParentNode("p", [])
        self.assertEqual(node.to_html(), result.to_html())

class Testblock_to_text(unittest.TestCase):
    def test_header_to_text0(self):
        block = """# h1 header block"""
        text = block_to_text(block, BlockType.HEADING)
        result = TextNode("h1 header block", TextType.TEXT)
        self.assertTrue(text[0] == result)

    def test_header_to_text1(self):
        block = """###### h6 header block"""
        text = block_to_text(block, BlockType.HEADING)
        result = TextNode("h6 header block", TextType.TEXT)
        self.assertTrue(text[0] == result)

    def test_ordlist_to_text0(self):
        block = """1. This is an ordered list.\n2. It can span multiple lines."""
        text = block_to_text(block, BlockType.ORD_LIST)
        result = [LeafNode(None,"This is an ordered list."), LeafNode(None, "It can span multiple lines.")]
        self.assertEqual(text[0].children[0].to_html(), result[0].to_html())

    def test_ordlist_to_text1(self):
        block = """1. This is an ordered list."""
        text = block_to_text(block, BlockType.ORD_LIST)
        result = TextNode("This is an ordered list.", TextType.TEXT)
        self.assertTrue(text[0].children[0].to_html() == result.text)

    def test_unordlist_to_text0(self):
        block = """- This is an unordered list.\n- It can span multiple lines."""
        text = block_to_text(block, BlockType.UNORD_LIST)
        result = TextNode("This is an unordered list.", TextType.TEXT)
        self.assertTrue(text[0].children[0].to_html() == result.text)

    def test_unordlist_to_text1(self):
        block = """- This is an unordered list."""
        text = block_to_text(block, BlockType.UNORD_LIST)
        result = TextNode("This is an unordered list.", TextType.TEXT)
        self.assertTrue(text[0].children[0].to_html() == result.text)

    def test_para_to_text1(self):
        block = """This is just a line of text\nthat needs to be converted"""
        text = block_to_text(block, BlockType.PARA)
        result = TextNode("This is just a line of text\nthat needs to be converted", TextType.TEXT)
        self.assertTrue(text[0].text == result.text)

class Testblock_to_children(unittest.TestCase):
    def test_Heading(self):
        block = """# h1 header block"""
        child = block_to_children(block, BlockType.HEADING)
        result = LeafNode(None, value="h1 header block")
        self.assertEqual(result.to_html(), child[0].to_html())

    def test_list(self):
        block = """1. This is an ordered list.
2. It can span multiple lines."""
        child = block_to_children(block, BlockType.ORD_LIST)
        result = LeafNode(None, "This is an ordered list.")
        self.assertEqual(result.to_html(), child[0].children[0].to_html())

    def test_list_bold(self):
        block = """1. This is a **bolded** ordered list.
2. It can span multiple lines."""
        child = block_to_children(block, BlockType.ORD_LIST)
        result = [LeafNode(None, "This is a "), LeafNode("b","bolded"), LeafNode(None,"ordered list.")]
        self.assertEqual(result[0].to_html(), child[0].children[0].to_html())

    def test_unord_list_bold0(self):
        block = """- This is a **bolded** unordered list.
- It can span multiple lines."""
        child = block_to_children(block, BlockType.UNORD_LIST)
        result = [LeafNode(None, "This is a "), LeafNode("b", "bolded"), LeafNode(None, " unordered list.")]
        self.assertEqual(result[0].to_html(), child[0].children[0].to_html())

    def test_unord_list_bold1(self):
        block = """- This is a **bolded** unordered list.
- It can span multiple lines."""
        child = block_to_children(block, BlockType.UNORD_LIST)
        result = [LeafNode(None, "This is a "), LeafNode("b", "bolded"), LeafNode(None, " unordered list.")]
        self.assertEqual(result[1].to_html(), child[0].children[1].to_html())
        
    def test_inline(self):
        block = """This is **bold** _italic_ text"""
        child = block_to_children(block, BlockType.PARA)
        result = LeafNode("b", value="bold")
        self.assertEqual(result.to_html(), child[1].to_html())

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph text in a p tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """```This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )