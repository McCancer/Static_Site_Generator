from textnode import TextNode, TextType
import pdb
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    """
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
    """
    """
    altTextRegex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    altTextMatches = re.findall(altTextRegex, text)
    return altTextMatches

def extract_markdown_links(text):
    """
    Extract_markdown_links

    :param text:
    :return: 
    """
    regText = r"(?<!/!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    linkTextMatch = re.findall(regText, text)
    return linkTextMatch

def split_nodes_images(oldNodes):
    """
    split_nodes_images

    :param oldNodes:
    :return:
    """
    new_node_lst = list()
    for node in oldNodes:
        if node.text == "": continue
        if node.text_type != TextType.NORMAL:
            new_node_lst.append(node)
            continue
        links = extract_markdown_images(node.text)
        if len(links) == 0: 
            new_node_lst.append(node)
            continue
        srcText = (links[0])[0]
        urlText = (links[0])[1]
        splitText = node.text.split(f"![{srcText}]({urlText})",1)
        tempList = [
            TextNode(splitText[0], TextType.NORMAL),
            TextNode(srcText, TextType.IMAGE, urlText),
            TextNode(splitText[1], TextType.NORMAL)
        ]
        new_node_lst.extend(split_nodes_images(tempList))
    return new_node_lst

def split_nodes_links(oldNodes):
    """
    split_nodes_links

    :param oldNodes:
    :return:
    """
    new_node_lst = list()
    for node in oldNodes:
        if node.text == "": continue
        if node.text_type != TextType.NORMAL:
            new_node_lst.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0: 
            new_node_lst.append(node)
            continue
        altText = (links[0])[0]
        urlText = (links[0])[1]
        splitText = node.text.split(f"[{altText}]({urlText})",1)
        tempList = [
            TextNode(splitText[0], TextType.NORMAL),
            TextNode(altText, TextType.LINKS, urlText),
            TextNode(splitText[1], TextType.NORMAL)
        ]
        new_node_lst.extend(split_nodes_links(tempList))
    return new_node_lst