import re
from htmlnode import *
from nodefuncs import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def extract_title(markdown):
    mdf = markdown.split('\n')
    title = None
    for line in mdf:
        cleanline = line.strip()
        if(cleanline[0:2] == "# "):
            title = cleanline.lstrip("# ")
            break
    if title == None: raise Exception("No h1 heading (title) in markdown file")
    return title

def markdown_to_blocks(markdown):
    '''
    markdown_to_blocks

    :param markdown: 
    :return: 
    '''
    blocks = list()
    lines = markdown.split("\n\n")
    for line in lines:
        if line == "":
            continue
        line = line.strip()
        blocks.append(line)
    return blocks

def block_to_block_type(block):
    '''
    block_to_block_type

    :param block:
    :return: 
    '''
    headingregex = r"^(#{1,6} )"
    coderegex =r"^```(\n)*(.*?)(\n)*```$"
    quoteregex =r"^>(.*)"
    unorderedregex = r"^(\s*)[-+*]\s+(.+)" #1. ^(\s*)[-+*]\s+(.+) 2.^\s*[-*]\s+.*$"
    orderedregex = r"^\s*\d+\.\s+.*$"
    if(len(re.findall(headingregex, block)) > 0): return block_type_heading
    elif(len(re.findall(coderegex, block)) > 0): return block_type_code
    elif(len(re.findall(quoteregex, block, re.MULTILINE)) == len(block.split('\n')) ): return block_type_quote
    elif(len(re.findall(unorderedregex, block, re.MULTILINE)) >0): return block_type_ulist
    elif(len(re.findall(orderedregex, block, re.MULTILINE)) > 0): return block_type_olist
    else: return block_type_paragraph

def markdown_to_html_node(markdown):
    '''
    markdown_to_html_node

    :param markdown:
    :return: 
    '''
    children_nodes = list()
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            children_nodes.append(heading_block_to_html_Node(block))
        elif block_type == block_type_code:
            children_nodes.append(code_block_to_html_node(block))
        elif block_type == block_type_quote:
            children_nodes.append(quote_block_to_html_node(block))
        elif block_type == block_type_ulist:
            children_nodes.append(ulist_block_to_html_node(block))
        elif block_type == block_type_olist:
            children_nodes.append(olist_block_to_html_node(block))
        elif block_type == block_type_paragraph:
            children_nodes.append(paragraph_block_to_html_node(block))
        else:
            raise ValueError("Invalid type of block.")
    return ParentNode("div", children_nodes)
    
def heading_block_to_html_Node(block):
    '''
    heading_block_to_html_Node Headings should be surrounded by a <h1> to <h6> tag, depending on the number of # characters

    :param block:
    :return:
    '''
    tag = ''
    if '###### ' in block:
        tag = 'h6'
        block = block.strip('###### ')
    elif '##### ' in block:
        tag = 'h5'
        block = block.strip('##### ')
    elif '#### ' in block:
        tag = 'h4'
        block = block.strip('#### ')
    elif '### ' in block:
        tag = 'h3'
        block = block.strip('### ')
    elif '## ' in block:
        tag = 'h2'
        block = block.strip('## ')
    else:
        tag = 'h1'
        block = block.strip('# ')
    return LeafNode(tag, block)

def code_block_to_html_node(block):
    '''
    code_block_to_html_node Code blocks should be surrounded by a <code> tag nested inside a <pre> tag.

    :param block:
    :return:
    '''
    children_nodes = list()
    text_nodes = text_to_textnodes(block)
    for text_node in text_nodes:
        children_nodes.append(text_node_to_html_node(text_node))
    return ParentNode('pre', children_nodes)

def quote_block_to_html_node(block):
    '''
    quote_block_to_html_no Quote blocks should be surrounded by a <blockquote> tag.

    :param block:
    :return:
    '''
    children_nodes = list()
    lines = list()
    for line in block.split('\n'):
        clean_line = line.lstrip("> ")
        lines.append(clean_line.strip())
    content = " ".join(lines)
    text_nodes = text_to_textnodes(content)
    for text_node in text_nodes:
        children_nodes.append(text_node_to_html_node(text_node))
    return ParentNode('blockquote', children_nodes)

def ulist_block_to_html_node(block):
    '''
    ulist_block_to_html_node

    :param block:
    :return:
    '''
    children_nodes = list()
    for line in block.split('\n'):
        sub_children_nodes = list()
        clean_line = line[2:]
        text_nodes = text_to_textnodes(clean_line)
        for text_node in text_nodes:
            sub_children_nodes.append(text_node_to_html_node(text_node))
        children_nodes.append(ParentNode('li', sub_children_nodes))
    return ParentNode('ul', children_nodes)

def olist_block_to_html_node(block):
    '''
    olist_block_to_html_node Ordered list blocks should be surrounded by a <ol> tag, and each list item should be surrounded by a <li> tag.

    :param block:
    :return:
    '''
    children_nodes = list()
    for line in block.split('\n'):
        sub_children_nodes = list()
        clean_line = line[3:]
        text_nodes = text_to_textnodes(clean_line)
        for text_node in text_nodes:
            sub_children_nodes.append(text_node_to_html_node(text_node))
        children_nodes.append(ParentNode('li', sub_children_nodes))
    return ParentNode('ol', children_nodes)

def paragraph_block_to_html_node(block):
    '''
    paragraph_block_to_html_node

    :param block:
    :return:
    '''
    children_nodes = list()
    new_lines = list()
    for line in block.split('\n'):
        new_lines.append(line.strip())
    content = " ".join(new_lines)
    text_nodes = text_to_textnodes(content)
    for text_node in text_nodes:
        children_nodes.append(text_node_to_html_node(text_node))
    return ParentNode('p', children_nodes)