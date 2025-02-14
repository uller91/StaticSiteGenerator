import re

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from block_markdown import markdown_to_blocks, block_to_block_type


def main():
    #print("hello")
    #text = "text\n\n \n\ntext2 \ntext3 \n\n* text4  \n\n\ntext5\n\n\n\ntext6"
    #list = markdown_to_blocks(text)
    #print(list)
    
    text_2 = "###### heading"
    print(block_to_block_type(text_2))

    text_3 = "> quote\n> quote\n> qq"
    print(block_to_block_type(text_3))

    text_4 = "``` code ```"
    print(block_to_block_type(text_4))

    text_5 = "* list\n* list"
    print(block_to_block_type(text_5))

    text_6 = "- list\n- list"
    print(block_to_block_type(text_6))

    text_7 = "1. list\n2. list"
    print(block_to_block_type(text_7))



main()
