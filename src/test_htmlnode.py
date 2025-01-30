import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_propstohtmlTest_one(self):
        test_string = ""
        node = HTMLNode()
        prop_string = node.props_to_html()
        self.assertEqual(test_string, prop_string)

    def test_propstohtmlTest_two(self):
        test_Dict = {"href":"https://www.google.com", "target":"_blank"}
        test_string = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(props=test_Dict)
        prop_string = node.props_to_html()
        self.assertEqual(test_string, prop_string)

    def test_propstohtmlTest_three(self):
        test_Dict = {"href":"https://www.google.com"}
        test_string = ' href="https://www.google.com"'
        node = HTMLNode(props=test_Dict)
        prop_string = node.props_to_html()
        self.assertEqual(test_string, prop_string)

    def test_values(self):
        node = HTMLNode("div", "This is a div")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is a div")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


    def test_values_two(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node1.tag, 'p')
        self.assertEqual(node1.value, "This is a paragraph of text.")
        self.assertEqual(node1.props, None)
        node2 = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node2.tag, 'a')
        self.assertEqual(node2.value, "Click me!")
        self.assertEqual(node2.props, {"href": "https://www.google.com"})
    
    def test_to_string(self):
        node = HTMLNode('TagTest', "TestVal", None, {"TestKey": "TestValue"})
        TestString = "HTML Node \nTag: TagTest\nValue: TestVal\nChildren: NONE\nProps: {'TestKey': 'TestValue'}"
        self.assertEqual(node.__repr__(), TestString)

    def test_tohtml_one(self):
        node = LeafNode("p", "This is a paragraph of text.")
        return_string = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), return_string)
    
    def test_tohtml_two(self):
        node =  LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        return_string = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), return_string)

    def test_parent_tohtml_one(self):
        node = ParentNode("p",[
                            LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text"),
                            LeafNode("i", "italic text", props={"Italian": "Latin"}),
                            LeafNode(None, "Normal text"),
                            ],)
        test_string = "<p><b>Bold text</b>Normal text<i Italian=\"Latin\">italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), test_string)
    
    def test_parent_tohtml_two(self):
        #Test a parent node in a parent node
        node1 = ParentNode("p",[LeafNode("i", "Inner1")])
        node2 = ParentNode("p",[
                                LeafNode("o","Outer1"),
                                node1,
                                LeafNode("o", "Outer2")],
                                )
        test_string = "<p><o>Outer1</o><p><i>Inner1</i></p><o>Outer2</o></p>"
        self.assertEqual(node2.to_html(), test_string)

    def test_parent_tohtml_three(self):
        #Test a parent node with no children
        node = ParentNode("p",[]) 
        test_string = "<p></p>"
        self.assertEqual(node.to_html(), test_string)

if __name__ == "__main__":
    unittest.main()