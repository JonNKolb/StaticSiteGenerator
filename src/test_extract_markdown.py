import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links, extract_title

class TestExtract_MD_image(unittest.TestCase):
    def test_exampe(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extract_markdown_images(text)
        result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), result)
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

class TestExtract_MD_link(unittest.TestCase):
    def test_exampe(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), result)

class TestExtract_Header(unittest.TestCase):
    def test_hello(self):
        markdown = """# Hello"""
        self.assertEqual(extract_title(markdown), "Hello")

    def test_hello_multiline(self):
        markdown = """# Hello\n## is it me\n### you're looking for?"""
        self.assertEqual(extract_title(markdown), "Hello")

    def test_noheader(self):
        markdown = """Hello"""
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()