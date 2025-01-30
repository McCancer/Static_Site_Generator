

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        '''
        param: tag: A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        param: value: A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        param: children: A list of HTMLNode objects representing the children of this node
        param: props:  A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        '''
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None: return ""
        return_string = ""
        for key in self.props:
            return_string = f"{return_string} {key}=\"{self.props[key]}\""
        return return_string.rstrip()

    def __repr__(self):
        return_string = "HTML Node \n"
        #Tag
        if self.tag == None: return_string = f"{return_string}Tag: NONE\n"
        else: return_string = f"{return_string}Tag: {self.tag}\n"
        #Value
        if self.value == None: return_string = f"{return_string}Value: NONE\n"
        else: return_string = f"{return_string}Value: {self.value}\n"
        #Children
        if self.children == None: return_string = f"{return_string}Children: NONE\n"
        else: return_string = f"{return_string}Children: {self.children}\n"
        #Props
        if self.props == None: return_string = f"{return_string}Props: NONE"
        else: return_string = f"{return_string}Props: {self.props}"
        return return_string

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)
    
    def to_html(self):
        if self.value == None: raise ValueError("All leaf nodes must have a value")
        if self.tag == None: return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return_string = "Leaf Node \n"
        #Tag
        if self.tag == None: return_string = f"{return_string}Tag: NONE\n"
        else: return_string = f"{return_string}Tag: {self.tag}\n"
        #Value
        if self.value == None: return_string = f"{return_string}Value: NONE\n"
        else: return_string = f"{return_string}Value: {self.value}\n"
        #Props
        if self.props == None: return_string = f"{return_string}Props: NONE"
        else: return_string = f"{return_string}Props: {self.props}"
        return return_string

    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None: raise ValueError("No Tag on parent Node")
        if self.children == None: raise ValueError("Parent Node Children List set to None")
        return_string = f"<{self.tag}>"
        for node in self.children:
            return_string += node.to_html()
        return_string += f"</{self.tag}>"
        return return_string
    
    def __repr__(self):
        return_string = "Parent Node \n"
        #Tag
        if self.tag == None: return_string = f"{return_string}Tag: NONE\n"
        else: return_string = f"{return_string}Tag: {self.tag}\n"
        #Children
        if self.children == None: return_string = f"{return_string}Children: NONE\n"
        else: return_string = f"{return_string}Children: {self.children}\n"
        #Props
        if self.props == None: return_string = f"{return_string}Props: NONE"
        else: return_string = f"{return_string}Props: {self.props}"
        return return_string
