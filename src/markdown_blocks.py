import re

def markdown_to_blocks(markdown):
    blocks = list()
    lines = markdown.split("\n\n")
    for line in lines:
        if line == "":
            continue
        line = line.strip()
        blocks.append(line)
    return blocks

def block_to_block_type(block):
    headingregex = r"^(#{1,6} )"
    coderegex =r"^```(\n)*(.*?)(\n)*```$"
    quoteregex =r"^>(.*)"
    unorderedregex = r"^[\s]*[-+*][\s]*+(.+)"
    orderedregex = r"^\s*\d+\.\s"
    if(len(re.findall(headingregex, block)) > 0): return "heading"
    elif(len(re.findall(coderegex, block)) > 0): return "code"
    elif(len(re.findall(quoteregex, block)) > 0): return "quote" 
    elif(len(re.findall(unorderedregex, block)) >0): return "unordered_list"
    elif(len(re.findall(orderedregex, block)) > 0): return "ordered_list"
    else: return "paragraph"