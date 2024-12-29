from textnode import TextNode, TextType

def main():
    dummy = TextNode("Text node", TextType.BOLD, "url")
    print(dummy.__repr__())

    dummy_2 = TextNode("Text node 2", TextType.CODE, )
    print(dummy_2.__repr__())

main()