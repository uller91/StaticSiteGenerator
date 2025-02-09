import re

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from block_markdown import markdown_to_blocks


def main():
    print("hello")
    text = "text\n\n \n\ntext2 \ntext3 \n\n* text4  \n\n\ntext5\n\n\n\ntext6"
    list = markdown_to_blocks(text)
    print(list)
    return

main()
