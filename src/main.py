from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from nodefuncs import *
from markdown_blocks import *

def main():
    teststring = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

```\nCode is here```

>This is a quote

1. Ordered 
2. List 
'''
    blocks = markdown_to_blocks(teststring)
    for block in blocks:
        print(block)
        print(block_to_block_type(block))

if __name__ == "__main__":
    main()