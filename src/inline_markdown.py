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