import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a", props={"href": "https://example.com", "target": "_blank"}
        )
        result = node.props_to_html()
        self.assertIn('href="https://example.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.startswith(" "))

    def test_props_to_html_empty(self):
        node = HTMLNode()
        with self.assertRaises(Exception) as context:
            node.props_to_html()
        self.assertEqual(str(context.exception), "Props is empty")

    def test_repr(self):
        node = HTMLNode(
            tag="p", value="Hello", children=[], props={"class": "greeting"}
        )
        expected_repr = (
            "Tag=[p]\nValue=[Hello]\nChildren=[[]]\nProps=[{'class': 'greeting'}]"
        )
        self.assertEqual(repr(node), expected_repr)

    def test_to_html_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
