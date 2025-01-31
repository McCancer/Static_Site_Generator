from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        text_split = old_node.text.split(delimiter)
        if(len(text_split) % 2 == 0):
            raise Exception("Invalid Markdown Syntax!")
        for i in range(len(text_split)):
            if text_split[i] == "": continue
            if(i % 2 == 0):
                new_nodes.append(TextNode(text_split[i], TextType.NORMAL))
            else:
                new_nodes.append(TextNode(text_split[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    altTextRegex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    altTextMatches = re.findall(altTextRegex, text)
    return altTextMatches

def extract_markdown_links(text):
    regText = r"(?<!/!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    linkTextMatch = re.findall(regText, text)
    return linkTextMatch