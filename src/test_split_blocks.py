import unittest
from split_blocks import markdown_to_blocks, BlockType, block_to_block_type


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_BlockType_Heading0(self):
        block = """# this is a heading"""
        self.assertEqual(BlockType.HEADING, block_to_block_type(block))

    def test_BlockType_Heading1(self):
        block = """###### this is a heading"""
        self.assertEqual(BlockType.HEADING, block_to_block_type(block))

    def test_BlockType_Heading2(self):
        block = """#this is not a heading"""
        self.assertNotEqual(BlockType.HEADING, block_to_block_type(block))

    def test_BlockType_Heading3(self):
        block = """####### this is not a heading"""
        self.assertNotEqual(BlockType.HEADING, block_to_block_type(block))
    def test_BlockType_Heading0(self):
        block = """# this is a heading"""
        self.assertEqual(BlockType.HEADING, block_to_block_type(block))

    def test_BlockType_Code0(self):
        block = """```this is a code block```"""
        self.assertEqual(BlockType.CODE, block_to_block_type(block))

    def test_BlockType_Code1(self):
        block = """```this is not a code block"""
        self.assertNotEqual(BlockType.CODE, block_to_block_type(block))

    def test_BlockType_Quote0(self):
        block = """> This is a blockquote.
> It can span multiple lines."""
        self.assertEqual(BlockType.QUOTE, block_to_block_type(block))

    def test_BlockType_Quote1(self):
        block = """> This is not a blockquote.
 It's not formatted correctly."""
        self.assertNotEqual(BlockType.QUOTE, block_to_block_type(block))

    def test_BlockType_Quote2(self):
        block = """> This is the first paragraph of a blockquote.
>
> This is the second paragraph."""
        self.assertEqual(BlockType.QUOTE, block_to_block_type(block))

    def test_BlockType_UnordList0(self):
        block = """- This is a unordered list.
- It can span multiple lines."""
        self.assertEqual(BlockType.UNORD_LIST, block_to_block_type(block))

    def test_BlockType_UnordList1(self):
        block = """- This is not an unordered list.
 It's not formatted correctly.
 - So it shouldn't count as one"""
        self.assertNotEqual(BlockType.UNORD_LIST, block_to_block_type(block))

    def test_BlockType_OrddList0(self):
        block = """1. This is an ordered list.
2. It can span multiple lines."""
        self.assertEqual(BlockType.ORD_LIST, block_to_block_type(block))

    def test_BlockType_OrdList1(self):
        block = """1. This is not an ordered list.
 It's not formatted correctly.
 2. So it shouldn't count as one"""
        self.assertNotEqual(BlockType.ORD_LIST, block_to_block_type(block))

    def test_BlockType_OrdList2(self):
        block = """1. This is not an ordered list.
 3. The numbers are not in order.
 4. So it shouldn't count as one"""
        self.assertNotEqual(BlockType.ORD_LIST, block_to_block_type(block))

    def test_BlockType_OrdList3(self):
        block = """1. This is an ordered list that goes up to two digits.\n2. \n3. \n4. \n5. \n6. \n7. \n8. \n9. \n10. \n11."""
        self.assertEqual(BlockType.ORD_LIST, block_to_block_type(block))


if __name__ == "__main__":
    unittest.main()
