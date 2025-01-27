import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_not_eq_enum(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node3)

    def test_not_eq_link(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.BOLD, "http")
        self.assertNotEqual(node, node4)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node5 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node5)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node6 = TextNode("This is another text node", TextType.LINK, "what?")
        self.assertNotEqual(node, node6)


class TestTextToHtmlNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("text", TextType.TEXT)
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.value, "text")
        self.assertEqual(leaf.tag, None)

    def test_bold(self):
        node = TextNode("text", TextType.BOLD)
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.value, "text")
        self.assertEqual(leaf.tag, "b")

    def test_italic(self):
        node = TextNode("text", TextType.ITALIC)
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.value, "text")
        self.assertEqual(leaf.tag, "i")

    def test_code(self):
        node = TextNode("Code", TextType.CODE)
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.value, "Code")
        self.assertEqual(leaf.tag, "code")

    def test_image(self):
        node = TextNode("Additional_text", TextType.IMAGE, "Url")
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.props_to_html(), ' src="Url" alt="Additional_text"')

    def test_link(self):
        node = TextNode("Link_text", TextType.LINK, "Url")
        leaf = text_node_to_html_node(node)
        self.assertEqual(leaf.value, 'Link_text')


if __name__ == "__main__":
    unittest.main()