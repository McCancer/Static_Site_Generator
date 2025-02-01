from textnode import TextNode, TextType
from nodefuncs import *
import unittest


class TestNodeFuncs(unittest.TestCase):
    def test_splitnodes_one(self):
        """Single Split"""
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
                                    TextNode("This is text with a ", TextType.NORMAL),
                                    TextNode("code block", TextType.CODE),
                                    TextNode(" word", TextType.NORMAL)
                                    ])

    def test_splitnodes_two(self):
        """More then one"""
        node = TextNode("This is text with a `code block` word with another `code block.`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
                                    TextNode("This is text with a ", TextType.NORMAL),
                                    TextNode("code block", TextType.CODE),
                                    TextNode(" word with another ", TextType.NORMAL),
                                    TextNode("code block.", TextType.CODE),
                                    ])

    def test_splitnodes_three(self):
        """Double split one after another"""
        node = TextNode("This text is **Bold** and *italic*", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        test_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertEqual(test_nodes, [
                                    TextNode("This text is ", TextType.NORMAL),
                                    TextNode("Bold", TextType.BOLD),
                                    TextNode(" and ", TextType.NORMAL),
                                    TextNode("italic", TextType.ITALIC),
                                    ])

    def test_splitnodes_four(self):
        """Test Bold"""
        node = TextNode("This text is **bold**", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
                                    TextNode("This text is ", TextType.NORMAL),
                                    TextNode("bold", TextType.BOLD),
                                    ])

    def test_splitnodes_five(self):
        """Test Italic"""
        node = TextNode("This text is *italic*", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [
                                    TextNode("This text is ", TextType.NORMAL),
                                    TextNode("italic", TextType.ITALIC),
                                    ])
        
    def test_extract_images_one(self):
        """Single link"""
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        test_list = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')]
        self.assertEqual(extract_markdown_images(text), test_list)

    def test_extract_images_two(self):
        """Double Link"""
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        test_list = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(extract_markdown_images(text), test_list)

    def test_extract_links_one(self):
        """Double Link"""
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        test_list = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), test_list)

    def test_extract_links_two(self):
        """Single link"""
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        test_list = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(extract_markdown_links(text), test_list)

    def test_split_nodes_images_one(self):
        """Single image"""
        node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) only one.",
                        TextType.NORMAL,
                        )
        test_nodes = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" only one.", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_images([node]),test_nodes)

    def test_split_nodes_images_two(self):
        """double image"""
        node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.NORMAL,
                        )
        test_nodes = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(split_nodes_images([node]),test_nodes)

    def test_split_nodes_link_one(self):
        """Single link"""
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) only one.",
                        TextType.NORMAL,
                        )
        test_nodes = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" only one.", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_links([node]),test_nodes)

    def test_split_nodes_link_two(self):
        """Double links"""
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                        TextType.NORMAL,
                        )
        test_nodes = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(split_nodes_links([node]),test_nodes)

if __name__ == "__main__":
    unittest.main()