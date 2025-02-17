import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import *
from block_markdown import *


class BlockDivision(unittest.TestCase):

    def test_to_blocks(self):
        markdown = "text\n\ntext2"
        blocks = markdown_to_blocks(markdown)

        self.assertListEqual(
            ["text", "text2"], blocks)
        
    def test_to_blocks_2(self):
        markdown = "text\ntext2"
        blocks = markdown_to_blocks(markdown)

        self.assertListEqual(
            ["text\ntext2"], blocks)
        
    def test_to_blocks_3(self):
        markdown = "text\n\n\ntext2"
        blocks = markdown_to_blocks(markdown)

        self.assertListEqual(
            ["text", "text2"], blocks)
        
    def test_to_blocks_4(self):
        markdown = "text \n\n\n text2"
        blocks = markdown_to_blocks(markdown)

        self.assertListEqual(
            ["text", "text2"], blocks)
        

class BlockToBlockType(unittest.TestCase):

    def test_to_heading(self):
        markdown = "###### heading"
        type = block_to_block_type(markdown)

        self.assertEqual("heading", type)
        
    def test_to_heading_2(self):
        markdown = "### heading"
        type = block_to_block_type(markdown)

        self.assertEqual("heading", type)

    def test_to_heading_3(self):
        markdown = "####### heading"
        type = block_to_block_type(markdown)

        self.assertNotEqual("heading", type)
        self.assertEqual("paragraph", type)

    def test_to_code(self):
        markdown = "``` code ```"
        type = block_to_block_type(markdown)

        self.assertEqual("code", type)

    def test_to_code_2(self):
        markdown = "```\ncode\n```"
        type = block_to_block_type(markdown)

        self.assertEqual("code", type)

    def test_to_code_3(self):
        markdown = "``\ncode\n`"
        type = block_to_block_type(markdown)

        self.assertNotEqual("code", type)
        self.assertEqual("paragraph", type)

    def test_to_quote(self):
        markdown = "> quote\n> quote\n> qq"
        type = block_to_block_type(markdown)

        self.assertEqual("quote", type)

    def test_to_quote_2(self):
        markdown = "> quote\n> quote\nqq"
        type = block_to_block_type(markdown)

        self.assertNotEqual("quote", type)
        self.assertEqual("paragraph", type)

    def test_to_un_list(self):
        markdown = "* list\n* list"
        type = block_to_block_type(markdown)

        self.assertEqual("unordered_list", type)

    def test_to_un_list_2(self):
        markdown = "- list\n- list"
        type = block_to_block_type(markdown)

        self.assertEqual("unordered_list", type)

    def test_to_or_list(self):
        markdown = "1. list\n2. list"
        type = block_to_block_type(markdown)

        self.assertEqual("ordered_list", type)

    def test_to_or_list_2(self):
        markdown = "1. list\n3. list"
        type = block_to_block_type(markdown)
        self.assertNotEqual("ordered_list", type)
        self.assertEqual("paragraph", type)

    def test_to_paragraph(self):
        markdown = "it is just text with a **bunch** of stuff in it"
        type = block_to_block_type(markdown)
        self.assertEqual("paragraph", type)


class BlockToHtmlNode(unittest.TestCase):

    def test_case(self):
        md = """
        ## heading\n\nblock of text\n\n> with a quote\n> and one more
        """

        node = markdown_to_html_node(md)

        self.assertEqual(
            ParentNode("div", [
                ParentNode("h2", [LeafNode(None, "heading")]),
                ParentNode("p", [LeafNode(None, "block of text")]),
                ParentNode("blockquote", [LeafNode(None, "with a quote and one more")])
            ]), node)

    def test_case_2(self):
        md = """
        ## heading\n\n```\bwith a code\n```
        """

        node = markdown_to_html_node(md)

        self.assertEqual(
            ParentNode("div", [
                ParentNode("h2", [LeafNode(None, "heading")]),
                ParentNode("pre", [ParentNode("code", [LeafNode(None, "with a code\n")])])
            ]), node)
        
    def test_case_3(self):
        md = """
        ![image](link)\n\n* unordered\n* list
        """

        node = markdown_to_html_node(md)

        self.assertEqual(
            ParentNode("div", [
                ParentNode("p", [LeafNode("img", "", {"src": "link", "alt": "image"})]),
                ParentNode("li", [ParentNode("ul", [LeafNode(None, "unordered")]), ParentNode("ul", [LeafNode(None, "list")])])
            ]), node)


    def test_case_4(self):
        md = """
        1. one\n2. two\n3. three\n\n- unordered\n- list
        """

        node = markdown_to_html_node(md)

        self.assertEqual(
            ParentNode("div", [
                ParentNode("li", [ParentNode("ol", [LeafNode(None, "one")]), ParentNode("ol", [LeafNode(None, "two")]), ParentNode("ol", [LeafNode(None, "three")])]),
                ParentNode("li", [ParentNode("ul", [LeafNode(None, "unordered")]), ParentNode("ul", [LeafNode(None, "list")])])
            ]), node)


class ExtractTItle(unittest.TestCase):

    def test_case_1(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")


    def test_case_2(self):
        markdown = "# Hello World \n"
        self.assertEqual(extract_title(markdown), "Hello World")


    def test_case_3(self):
        markdown = "# Hello World \nand no more\n"
        self.assertEqual(extract_title(markdown), "Hello World \nand no more")