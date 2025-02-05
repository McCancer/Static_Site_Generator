import unittest
from markdown_blocks import *


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        '''
        
        '''
        teststring = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
'''
        testList = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(markdown_to_blocks(teststring), testList)


    def test_block_to_block_type(self):
        '''
        
        '''
        teststring = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

```Code is here```

>This is a quote

1. Ordered 
2. List 
''' 
        blocklst = list()
        blocks = markdown_to_blocks(teststring)
        for block in blocks:
            blocklst.append(block_to_block_type(block))
        testlst = ['heading','paragraph','unordered_list','code','quote','ordered_list']
        self.assertEqual(testlst, blocklst)

    def test_block_to_block_types_two(self):
        '''
        
        '''
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()