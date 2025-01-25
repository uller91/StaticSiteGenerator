import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):

    def test_text(self):
        print("\ntest 1")
        node = TextNode("text", TextType.TEXT)
        print(node.__repr__())
        leaf = text_node_to_html_node(node)
        print(leaf.__repr__())
        self.assertEqual(leaf.value, "text")

    def test_bold(self):
        print("\ntest 2")
        node = TextNode("text", TextType.BOLD)
        print(node.__repr__())
        leaf = text_node_to_html_node(node)
        print(leaf.__repr__())
        self.assertEqual(leaf.tag, "b")

    def test_italic(self):
        print("\ntest 3")
        node = TextNode("text", TextType.ITALIC)
        print(node.__repr__())
        leaf = text_node_to_html_node(node)
        print(leaf.__repr__())
        self.assertEqual(leaf.tag, "i")

    def test_code(self):
        print("\ntest 4")
        node = TextNode("Code", TextType.CODE)
        print(node.__repr__())
        leaf = text_node_to_html_node(node)
        print(leaf.__repr__())
        self.assertEqual(leaf.value, "Code")

    def test_image(self):
        print("\ntest 5")
        node = TextNode("Additional_text", TextType.IMAGE, "Url")
        print(node.__repr__())
        leaf = text_node_to_html_node(node)
        print(leaf.__repr__())
        print(leaf.props_to_html())
        self.assertEqual(leaf.props_to_html(), ' src="Url" alt="Additional_text"')

    def test_link(self):
        print("\ntest 6")
        node = TextNode("Link_text", TextType.LINK, "Url")
        print(node.__repr__())
        leaf = text_node_to_html_node(node)
        print(leaf.__repr__())
        self.assertEqual(leaf.value, 'Link_text')


if __name__ == "__main__":
    unittest.main()