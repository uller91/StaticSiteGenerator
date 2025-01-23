class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
        
    def props_to_html(self):
        if self.props is None:
            return ""
        
        props_line = ""
        for key, value in self.props.items():
            props_line += f' {key}="{value}"'
            #print(props_line)
        return props_line
        
    def __eq__(self, HTMLNode):
        if self.tag == HTMLNode.tag and self.value == HTMLNode.value and self.children == HTMLNode.children and self.props == HTMLNode.props:
            return True
        return False

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        
        elif self.tag == None:
            return self.value
        
        else:
            if self.props == None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                props = self.props_to_html()
                return f"<{self.tag} {props}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})"