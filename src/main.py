import re

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link


def main():
    #text = "test ![text test](link/abc) ![text test 2](link/abc2)"
    #print(extract_markdown_images(text))
    
    node = TextNode("text", TextType.ITALIC)
    print(split_nodes_image([node]))

    node2 = TextNode("text", TextType.TEXT)
    print(split_nodes_image([node2]))

    node3 = TextNode("test lala![text test](link/abc) lala", TextType.TEXT)
    print(split_nodes_image([node3]))

    node4 = TextNode("test lala![text test](link/abc) ![text test 2](link/abc2) lala", TextType.TEXT)
    print(split_nodes_image([node4]))

    node5 = TextNode("![text test](link/abc) ![text test 2](link/abc2) lala", TextType.TEXT)
    print(split_nodes_image([node5]))

    node6 = TextNode("![text test](link/abc) ![text test 2](link/abc2)", TextType.TEXT)
    print(split_nodes_image([node6]))

    node7 = TextNode("![text test](link/abc)![text test 2](link/abc2)", TextType.TEXT)
    print(split_nodes_image([node7]))

    node8 = TextNode("[text test](link/abc)[text test 2](link/abc2)", TextType.TEXT)
    print(split_nodes_link([node8]))
    
    node9 = TextNode("[text test](link/abc) ![text test 2](link/abc2) **bold!**", TextType.TEXT)
    print(split_nodes_link([node9]))

    nodes10 = split_nodes_link([node9])
    print(split_nodes_image(nodes10))

    nodes11 = split_nodes_image(nodes10)
    print(split_nodes_delimiter(nodes11, "**", TextType.BOLD))

main()
