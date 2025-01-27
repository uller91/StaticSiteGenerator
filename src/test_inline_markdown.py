import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import split_nodes_delimiter


class TestDelimeter(unittest.TestCase):
    
    
    def test_not_TEXT(self):
        node = TextNode("text", TextType.ITALIC)
        node_list = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertListEqual(
            [
                TextNode("text", TextType.ITALIC)
            ], node_list)

    def test_bold(self):
        node3 = TextNode("test text **bold???**, yes", TextType.TEXT)
        node_list3 = split_nodes_delimiter([node3], "**", TextType.BOLD)

        self.assertListEqual(
            [
                TextNode("test text ", TextType.TEXT),
                TextNode("bold???", TextType.BOLD),
                TextNode(", yes", TextType.TEXT)
            ], node_list3)

    def test_italic(self):
        node4 = TextNode("*italic!* test text, yes", TextType.TEXT)
        node_list4 = split_nodes_delimiter([node4], "*", TextType.ITALIC)

        self.assertListEqual(
            [
                TextNode("italic!", TextType.ITALIC),
                TextNode(" test text, yes", TextType.TEXT)
            ], node_list4)

    def test_code(self):
        node5 = TextNode("test text `some code` **bold???**, yes", TextType.TEXT)
        node_list5 = split_nodes_delimiter([node5], "`", TextType.CODE)

        self.assertListEqual(
            [
                TextNode("test text ", TextType.TEXT),
                TextNode("some code", TextType.CODE),
                TextNode(" **bold???**, yes", TextType.TEXT)
            ], node_list5)
        
    def test_combination(self):
        node6 = TextNode("**bold text** more text *italic* **more bold** even more text `code`", TextType.TEXT)
        node_list6 = split_nodes_delimiter([node6], "**", TextType.BOLD)
        node_list7 = split_nodes_delimiter(node_list6, "*", TextType.ITALIC)
        node_list8 = split_nodes_delimiter(node_list7, "`", TextType.CODE)

        self.assertListEqual(
            [
                TextNode("bold text", TextType.BOLD),
                TextNode(" more text *italic* ", TextType.TEXT),
                TextNode("more bold", TextType.BOLD),
                TextNode(" even more text `code`", TextType.TEXT)
            ], node_list6)
        
        self.assertListEqual(
            [
                TextNode("bold text", TextType.BOLD),
                TextNode(" more text ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("more bold", TextType.BOLD),
                TextNode(" even more text `code`", TextType.TEXT)
            ], node_list7)
        
        self.assertListEqual(
            [
                TextNode("bold text", TextType.BOLD),
                TextNode(" more text ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("more bold", TextType.BOLD),
                TextNode(" even more text ", TextType.TEXT),
                TextNode("code", TextType.CODE)
            ], node_list8)


    

if __name__ == "__main__":
    unittest.main()