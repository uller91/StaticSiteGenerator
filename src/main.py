from block_markdown import *


def main():

    text_7 = "## heading"
    #print(markdown_to_html_node(text_7))

    text_8 = "## heading \n\n aaa \n\n bbb *ccc*"
    #print(markdown_to_html_node(text_8))
    
    text_9 = "```\n1code code2\n```"
    #print(markdown_to_html_node(text_9))

    text_10 = "> start\n> *middle*\n> end"
    #print(markdown_to_html_node(text_10))

    text_12 = "> start\n> middle\n> end"
    #print(markdown_to_html_node(text_12))

    text_13 = "test\ntext"
    #print(markdown_to_html_node(text_13))

main()
