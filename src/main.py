from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    dummy = TextNode("Text node", TextType.BOLD, "url")
    print(dummy.__repr__())

    dummy_2 = TextNode("Text node 2", TextType.CODE, )
    print(dummy_2.__repr__())

    dummy_3 = HTMLNode("p", "text", ["a", "b"], {"a1":"b1", "a2":"b2"})
    print(dummy_3.__repr__())

    line = ""
    line = dummy_3.props_to_html()
    print(line)

    node = HTMLNode(props=None)
    print(node.__repr__())
    print(node.props_to_html())

    node2 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    print(node2.__repr__())
    print(node2.props_to_html())

main()