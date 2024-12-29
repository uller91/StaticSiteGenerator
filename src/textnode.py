from enum import Enum

class TextType(Enum):
    NORMAL_TEXTTYPE = "Normal"
    BOLD_TEXTTYPE = "Bold"
    ITALIC_TEXTTYPE = "Italic"
    CODE_TEXTTYPE = "Code"
    LINK_TEXTTYPE = "Link"
    IMAGE_TEXTTYPE = "Image"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, TextNode):
        if self.text == TextNode.text and self.text_type == TextNode.texttype and self.url == TextNode.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"