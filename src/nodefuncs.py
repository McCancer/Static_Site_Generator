from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter:str, text_type: TextType)-> list[TextNode]:
    """
    split_nodes_delimter takes a list of nodes that are normal text and returns normal text nodes and nodes of the given type in a list.

    :param old_nodes: List of Nodes to split 
    :param delimiter: Delimiter to split the text by
    :param text_type: The Text type that goes with the delimiter
    :return:
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

def extract_markdown_images(text:str)->list[tuple[str,str]]:
    """
    extract_markdown_image

    :param text: Given text you want to regex match off of.
    :return: returns all images in a list of tuples of alttext and url. 
    """
    altTextRegex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    altTextMatches = re.findall(altTextRegex, text)
    return altTextMatches

def extract_markdown_links(text:str)->list[tuple[str,str]]:
    """
    Extract_markdown_links

    :param text: Given text you want to regex match off of.
    :return: returns all the links in a list of tuples of alttext and url
    """
    regText = r"(?<!/!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    linkTextMatch = re.findall(regText, text)
    return linkTextMatch

def split_nodes_images(oldNodes:list[TextNode])->list[TextNode]:
    """
    split_nodes_images from a list of nodes it splits the images out of the text and puts the images as their own nodes

    :param oldNodes: List of Nodes you want to split
    :return: A list of new text nodes with the new image nodes added
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

def split_nodes_links(oldNodes:list[TextNode])->list[TextNode]:
    """
    split_nodes_links from a list of nodes it splits the links out of the text and puts the links as their own nodes

    :param oldNodes: List of Nodes you want to split
    :return: A list of new text nodes with the new links nodes added
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

def text_to_textnodes(text:str)->list[TextNode]:
    """
    text_to_textnodes turns markdown text into a list of text nodes

    :param text: plain text you want to turn into text nodes
    :return: the plain text is converted into a list of text nodes
    """
    node_List = [TextNode(text, TextType.NORMAL)]
    new_nodes = split_nodes_delimiter(node_List, '**', TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, '*', TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, '`', TextType.CODE)
    new_nodes = split_nodes_images(new_nodes)
    new_nodes = split_nodes_links(new_nodes)
    return new_nodes    