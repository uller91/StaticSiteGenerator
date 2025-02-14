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
            raise ValueError("value is missing")
        
        elif self.tag == None:
            return self.value
        
        else:
            if self.props == None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                props = self.props_to_html()
                return f"<{self.tag} {props}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag is missing")
        
        elif self.children == None:
            raise ValueError("children are missing")
        
        else:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
                #print(children_html)
            
            if self.props == None:
                return f"<{self.tag}>{children_html}</{self.tag}>"
            else:
                props = self.props_to_html()
                return f"<{self.tag} {props}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"