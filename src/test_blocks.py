import unittest
from block_functions import markdown_to_blocks, block_to_block_type
from blocktype import Markdown
from markdown_to_html_node import markdown_to_html_node
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    extract_markdown_text
)   


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_block_basic(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        result = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            result,
        )

    def test_markdown_to_block_extra_spaces(self):
        md = """
This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line                  

    - This is a list
- with items            
"""

        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            blocks,
        )
        
    def test_markdown_to_block_newlines(self):
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


    def test_block_to_blocktype_heading(self):
        heading_block = "# Heading 1"
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, Markdown.HEADING)
    
    def test_block_to_blocktype_heading_six(self):
        heading_block = "###### Heading 6"
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, Markdown.HEADING)
    
    def test_block_to_blocktype_code(self):
        code_block = "```\nint code = 4;\n```"
        block_type = block_to_block_type(code_block)
        self.assertEqual(block_type, Markdown.CODE)
    
    def test_block_to_blocktype_quote(self):
        quote_block = "> This is a quote by \n> The great Gokul"
        block_type = block_to_block_type(quote_block)
        self.assertEqual(block_type, Markdown.QUOTE)
    
    def test_block_to_blocktype_UL(self):
        unordered_list = "- List Item 1\n- List Item 2"
        block_type = block_to_block_type(unordered_list)
        self.assertEqual(block_type, Markdown.UNORDERED_LIST)
    
    def test_block_to_blocktype_OL(self):
        ordered_list = "1. List Item 1\n2. List Item 2"
        block_type = block_to_block_type(ordered_list)
        print("--------------------------------------------------------------------------------------------------")
        print(block_type)
        print("--------------------------------------------------------------------------------------------------")
        self.assertEqual(block_type, Markdown.ORDERED_LIST)
    
        
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )