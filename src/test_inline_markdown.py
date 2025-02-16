import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes


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


class TestExtractLinkAndImage(unittest.TestCase):

    def test_single_image(self):
        text = "test ![text test](link/abc)"
        result = extract_markdown_images(text)
        self.assertListEqual([("text test", "link/abc")], result)

    def test_double_image(self):
        text = "test ![text test](link/abc) ![text test 2](link/abc2)"
        result = extract_markdown_images(text)
        self.assertListEqual([("text test", "link/abc"), ("text test 2", "link/abc2")], result)

    def test_no_link(self):
        text = "test ![text test](link/abc) ![text test 2](link/abc2)"
        result = extract_markdown_links(text)
        self.assertListEqual([], result)

    def test_single_link(self):
        text = "test [text test](link/abc)"
        result = extract_markdown_links(text)
        self.assertListEqual([("text test", "link/abc")], result)

    def test_double_link(self):
        text = "test [text test](link/abc) [text test 2](link/abc2)"
        result = extract_markdown_links(text)
        self.assertListEqual([("text test", "link/abc"), ("text test 2", "link/abc2")], result)
         
    def test_link_no_image(self):
        text = "test ![text test](link/abc) [text test 2](link/abc2)"
        result = extract_markdown_links(text)
        self.assertListEqual([("text test 2", "link/abc2")], result)

    def test_link_and_image(self):
        text = "test ![text test](link/abc)[text test 2](link/abc2)"
        result = extract_markdown_images(text)
        result_2 = extract_markdown_links(text)
        self.assertListEqual([("text test", "link/abc")], result)
        self.assertListEqual([("text test 2", "link/abc2")], result_2)

    def test_link_and_image_no_text(self):
        text = "test ![](link@/abc)[](link@/abc2)"
        result = extract_markdown_images(text)
        result_2 = extract_markdown_links(text)
        self.assertListEqual([("", "link@/abc")], result)
        self.assertListEqual([("", "link@/abc2")], result_2)

    def test_link_and_image_no_link(self):
        text = "test ![text]()[text2]()"
        result = extract_markdown_images(text)
        result_2 = extract_markdown_links(text)
        self.assertListEqual([("text", "")], result)
        self.assertListEqual([("text2", "")], result_2)


class TestSplitImageAndLink(unittest.TestCase):

    def test_no_image(self):
        node = TextNode("text", TextType.ITALIC)
        lst = split_nodes_image([node])

        node2 = TextNode("text", TextType.TEXT)
        lst2 = split_nodes_image([node2])

        self.assertListEqual([TextNode("text", TextType.ITALIC)], lst)
        self.assertListEqual([TextNode("text", TextType.TEXT)], lst2)

    def test_image(self):
        node3 = TextNode("test lala![text test](link/abc) lala", TextType.TEXT)
        lst3 = split_nodes_image([node3])

        node4 = TextNode("test lala![text test](link/abc) ![text test 2](link/abc2) lala", TextType.TEXT)
        lst4 = split_nodes_image([node4])

        node5 = TextNode("![text test](link/abc) ![text test 2](link/abc2) lala", TextType.TEXT)
        lst5 = split_nodes_image([node5])

        node6 = TextNode("![text test](link/abc) ![text test 2](link/abc2)", TextType.TEXT)
        lst6 = split_nodes_image([node6])

        node7 = TextNode("![text test](link/abc)![text test 2](link/abc2)", TextType.TEXT)
        lst7 = split_nodes_image([node7])
    
        self.assertListEqual([TextNode("test lala", TextType.TEXT),
                              TextNode("text test", TextType.IMAGE, "link/abc"),
                              TextNode(" lala", TextType.TEXT)], lst3)
        
        self.assertListEqual([TextNode("test lala", TextType.TEXT),
                              TextNode("text test", TextType.IMAGE, "link/abc"),
                              TextNode(" ", TextType.TEXT),
                              TextNode("text test 2", TextType.IMAGE, "link/abc2"),
                              TextNode(" lala", TextType.TEXT)], lst4)
        
        self.assertListEqual([TextNode("text test", TextType.IMAGE, "link/abc"),
                              TextNode(" ", TextType.TEXT),
                              TextNode("text test 2", TextType.IMAGE, "link/abc2"),
                              TextNode(" lala", TextType.TEXT)], lst5)
        
        self.assertListEqual([TextNode("text test", TextType.IMAGE, "link/abc"),
                              TextNode(" ", TextType.TEXT),
                              TextNode("text test 2", TextType.IMAGE, "link/abc2")], lst6)
        
        self.assertListEqual([TextNode("text test", TextType.IMAGE, "link/abc"),
                              TextNode("text test 2", TextType.IMAGE, "link/abc2")], lst7)
    
    def test_image(self):
        node8 = TextNode("[text test](link/abc)[text test 2](link/abc2)", TextType.TEXT)
        lst8 = split_nodes_link([node8])
    
        self.assertListEqual([TextNode("text test", TextType.LINK, "link/abc"),
                              TextNode("text test 2", TextType.LINK, "link/abc2")], lst8)
        
    def test_link_to_image_to_bold(self):
        node9 = TextNode("[text test](link/abc) ![text test 2](link/abc2) **bold!**", TextType.TEXT)
        nodes10 = split_nodes_link([node9])
        nodes11 = split_nodes_image(nodes10)
        lst9 = split_nodes_delimiter(nodes11, "**", TextType.BOLD)
    
        self.assertListEqual([TextNode("text test", TextType.LINK, "link/abc"),
                              TextNode(" ", TextType.TEXT),
                              TextNode("text test 2", TextType.IMAGE, "link/abc2"),
                              TextNode(" ", TextType.TEXT),
                              TextNode("bold!", TextType.BOLD)], lst9)


class TestTextToTextnodes(unittest.TestCase):
    
    def test_text_to_textnode(self):
        text1 = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        lst = text_to_textnodes(text1)
        self.assertListEqual([TextNode("This is ", TextType.TEXT),
                              TextNode("text", TextType.BOLD),
                              TextNode(" with an ", TextType.TEXT),
                              TextNode("italic", TextType.ITALIC),
                              TextNode(" word and a ", TextType.TEXT),
                              TextNode("code block", TextType.CODE),
                              TextNode(" and an ", TextType.TEXT),
                              TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                              TextNode(" and a ", TextType.TEXT),
                              TextNode("link", TextType.LINK, "https://boot.dev")], lst)


if __name__ == "__main__":
    unittest.main()