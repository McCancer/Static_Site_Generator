from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from nodefuncs import *
from markdown_blocks import *

def main():
    teststring = '1. ordered\n2. list'
    node = olist_block_to_html_node(teststring)
    print(node)
    

if __name__ == "__main__":
    main()