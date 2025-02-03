import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:    
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        #if old_node.text.find(delimiter) == -1:
        #    raise ValueError("delimeter is not found in the sting")

        split_nodes = []
        sub_nodes = old_node.text.split(delimiter)
        if len(sub_nodes) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for k in range(len(sub_nodes)):
            if sub_nodes[k] == "":
                continue
            if k % 2 == 0:
                split_nodes.append(TextNode(sub_nodes[k], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sub_nodes[k], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:    
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        #check if there is an image(s)
        images = extract_markdown_images(old_node.text)
        if images == []:
            new_nodes.append(old_node)
            continue

        index_text = old_node.text.index(images[0][0])
        index_link = old_node.text.index(images[0][1])
        
        #position tests
        #print(index_text)
        #print(index_link + len(images[0][1]))
        #print(old_node.text[:index_text - 2])
        #print(old_node.text[index_link + len(images[0][1]) + 1:])

        if len(old_node.text[:index_text - 2]) != 0:
            new_nodes.append(TextNode(old_node.text[:index_text - 2], TextType.TEXT))
        new_nodes.append(TextNode(images[0][0], TextType.IMAGE, images[0][1]))
        if len(old_node.text[index_link + len(images[0][1]) + 1:]) != 0:
            new_nodes.append(TextNode(old_node.text[index_link + len(images[0][1]) + 1:], TextType.TEXT))

        if len(images) > 1:
            current_node = new_nodes.pop()
            new_nodes.extend(split_nodes_image([current_node]))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:    
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        #check if there is an image(s)
        links = extract_markdown_links(old_node.text)
        if links == []:
            new_nodes.append(old_node)
            continue

        index_text = old_node.text.index(links[0][0])
        index_link = old_node.text.index(links[0][1])
        
        if len(old_node.text[:index_text - 1]) != 0:
            new_nodes.append(TextNode(old_node.text[:index_text - 1], TextType.TEXT))
        new_nodes.append(TextNode(links[0][0], TextType.LINK, links[0][1]))
        if len(old_node.text[index_link + len(links[0][1]) + 1:]) != 0:
            new_nodes.append(TextNode(old_node.text[index_link + len(links[0][1]) + 1:], TextType.TEXT))

        if len(links) > 1:
            current_node = new_nodes.pop()
            new_nodes.extend(split_nodes_link([current_node]))

    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    node_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    node_italic = split_nodes_delimiter(node_bold, "*", TextType.ITALIC)
    node_code = split_nodes_delimiter(node_italic, "`", TextType.CODE)
    node_image = split_nodes_image(node_code)
    node_link = split_nodes_link(node_image)
    return node_link