from textnode import *

def main():
    dummy = TextNode("Text node", "Bold", "url")
    print(dummy.__repr__())

    dummy_2 = TextNode("Text node 2", "Code", )
    print(dummy_2.__repr__())

main()