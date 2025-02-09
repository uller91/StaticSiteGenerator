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