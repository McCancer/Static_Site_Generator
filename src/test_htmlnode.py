import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_propstohtmlTest_one(self):
        test_string = ""
        node = HTMLNode()
        prop_string = node.props_to_html()
        self.assertEqual(test_string, prop_string)

    def test_propstohtmlTest_two(self):
        test_Dict = {"href":"https://www.google.com", "target":"_blank"}
        test_string = 'href="https://www.google.com" target="_blank"'
        node = HTMLNode(props=test_Dict)
        prop_string = node.props_to_html()
        self.assertEqual(test_string, prop_string)

    def test_propstohtmlTest_three(self):
        test_Dict = {"href":"https://www.google.com"}
        test_string = 'href="https://www.google.com"'
        node = HTMLNode(props=test_Dict)
        prop_string = node.props_to_html()
        self.assertEqual(test_string, prop_string)
