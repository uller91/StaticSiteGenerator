from textnode import TextNode, TextType


def markdown_to_blocks(markdown):
    print(markdown)
    split_markdown = markdown.split("\n\n")
    return_list = []
    for item in split_markdown:
        item = item.strip()
        if item != "":
            return_list.append(item)
    return return_list

def block_to_block_type(block):
    if block[:2] == "# ":
        return "heading 1"
    elif block[:3] == "## ":
        return "heading 2"
    elif block[:4] == "### ":
        return "heading 3"
    elif block[:5] == "#### ":
        return "heading 4"
    elif block[:6] == "##### ":
        return "heading 5"
    elif block[:7] == "###### ":
        return "heading 6"
    elif block[:3] == "```" and block[-3:] == "```":
        return "code"
    
    lines = block.split("\n")
    counter = 0
    if lines[0][0] == ">":
        for line in lines:
            if line[0] == ">":
                counter += 1
        if counter == len(lines):
            return "quote"    
        
    if lines[0][:2] == "* ":
        for line in lines:
            if line[:2] == "* ":
                counter += 1
        if counter == len(lines):
            return "unordered_list"    
    if lines[0][:2] == "- ":
        for line in lines:
            if line[:2] == "- ":
                counter += 1
        if counter == len(lines):
            return "unordered_list"    
        
    if lines[0][:3] == "1. ":
        i = 1
        for line in lines:
            if line[:3] == f"{i}. ":
                counter += 1
                i += 1
        if counter == len(lines):
            return "ordered_list"    
    
    return "normal"

    
    
    
    