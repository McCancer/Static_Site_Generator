import unittest
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        """
        """
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_full(self):
        """
        """
        node = TextNode("This is a text node", TextType.BOLD, url="This is a test")
        node2 = TextNode("This is a text node", TextType.BOLD, url="This is a test")
        self.assertEqual(node, node2)

    def test_neq_one(self):
        """
        """
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Alternate Text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_two(self):
        """
        """
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_three(self):
        """
        """
        node = TextNode("This is a text node", TextType.BOLD, url="This is a test")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

class TestTextToLeafNode(unittest.TestCase):
    def test_NormalTN_to_Leaf(self):
        """
        """
        TestNode = TextNode("Test", TextType.NORMAL)
        funcNode = text_node_to_html_node(TestNode)
        test_string = "Test"
        self.assertEqual(funcNode.to_html(), test_string)
    
    def test_BoldTN_to_Leaf(self):
        """
        """
        TestNode = TextNode("Test", TextType.BOLD)
        funcNode = text_node_to_html_node(TestNode)
        test_string = "<b>Test</b>"
        self.assertEqual(funcNode.to_html(), test_string)

    def test_ItalicTN_to_Leaf(self):
        """
        """
        TestNode = TextNode("Test", TextType.ITALIC)
        funcNode = text_node_to_html_node(TestNode)
        test_string = "<i>Test</i>"
        self.assertEqual(funcNode.to_html(), test_string)

    def test_CodeTN_to_Leaf(self):
        """
        """
        TestNode = TextNode("Test", TextType.CODE)
        funcNode = text_node_to_html_node(TestNode)
        test_string = "<code>Test</code>"
        self.assertEqual(funcNode.to_html(), test_string)

    def test_LinksTN_to_Leaf(self):
        """
        """
        TestNode = TextNode("Test", TextType.LINKS, "URLLink")
        funcNode = text_node_to_html_node(TestNode)
        test_string = "<a href=\"URLLink\">Test</a>"
        self.assertEqual(funcNode.to_html(), test_string)

    def test_ImageTN_to_Leaf(self):
        """
        """
        TestNode = TextNode("Test", TextType.IMAGE, "URLLink")
        funcNode = text_node_to_html_node(TestNode)
        test_string = "<img src=\"URLLink\" alt=\"Test\"></img>"
        self.assertEqual(funcNode.to_html(), test_string)

if __name__ == "__main__":
    unittest.main()