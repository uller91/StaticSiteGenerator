import re

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


def main():
    text = "test ![text test](link/abc) ![text test 2](link/abc2)"
    print(extract_markdown_images(text))


main()
