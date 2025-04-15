import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a test node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT)
        node2 = TextNode("Different text", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_type(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a test node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        node2 = TextNode("Click here", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)

    def test_not_eq_different_url(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        node2 = TextNode("Click here", TextType.LINK, "https://different.com")
        self.assertNotEqual(node, node2)

    def test_textnode_attributes(self):
        node = TextNode("Example", TextType.NORMAL_TEXT)
        self.assertEqual(node.text, "Example")
        self.assertEqual(node.text_type, TextType.NORMAL_TEXT)
        self.assertIsNone(node.url)

    def test_repr(self):
        node = TextNode("Example", TextType.NORMAL_TEXT)
        expected = "TextNode(Example, normal, None)"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main()
