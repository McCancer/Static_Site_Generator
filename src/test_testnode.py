import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_full(self):
        node = TextNode("This is a text node", TextType.BOLD, url="This is a test")
        node2 = TextNode("This is a text node", TextType.BOLD, url="This is a test")
        self.assertEqual(node, node2)

    def test_neq_one(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Alternate Text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_two(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_three(self):
        node = TextNode("This is a text node", TextType.BOLD, url="This is a test")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()