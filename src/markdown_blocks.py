import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

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