from htmlnode import LeafNode
from enum import Enum 

class TextType(Enum):
    NORMAL = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINKS = 5
    IMAGE = 6

class TextNode():

    def __init__(self, text, text_type, url=None):
        """
        __init__

        :param text:
        :param text_type:
        :param url:
        """
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other_node):
        """
        __eq__

        :param other_node:
        :return: 
        """
        return ((self.text == other_node.text) and (self.text_type == other_node.text_type) and (self.url == other_node.url))
    
    def __repr__(self):
        """
        __repr__

        :return:
        """
        return f"TextNode({self.text}, {self.text_type.name}, {self.url})"

def text_node_to_html_node(text_node):
    """
    text_node_to_html_node

    :param text_node:
    :return: 
    """
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINKS:
            return LeafNode('a', text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode('img', "", props={"src":text_node.url,"alt":text_node.text})
        case _:
            raise Exception("No Text of that type")