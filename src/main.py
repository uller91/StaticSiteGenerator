import re

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


def main():
    text = "test ![text test](link/abc) ![text test 2](link/abc2)"
    print(extract_markdown_images(text))

    text2 = "test ![text test](link/abc) ![text test 2](link/abc2)"
    print(extract_markdown_links(text2))

    text3 = "test [text test](link/abc) [text test 2](link/abc2)"
    print(extract_markdown_links(text3))

    text4 = "test ![text test](link/abc) [text test 2](link/abc2)"
    print(extract_markdown_links(text4))
    
    text5 = "test ![text test](link/abc)[text test 2](link/abc2)"
    print(extract_markdown_links(text5))
    print(extract_markdown_images(text5))

    text6 = "test ![](link/ab@c)[](link/a@bc2)"
    print(extract_markdown_links(text6))
    print(extract_markdown_images(text6))


main()
