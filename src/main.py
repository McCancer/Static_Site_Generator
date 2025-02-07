import os
import shutil
from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from nodefuncs import *
from markdown_blocks import *

def main():
    copy_static('static','public')
    generate_page('content/index.md','template.html','public/index.html')
    
def copy_static(src, destination):
    '''
    copy_static

    :param src:
    :param destination: 
    '''
    if(not os.path.exists(src) or os.path.isfile(src)): raise Exception("Source doesn't exist or is a file")
    if(not os.path.exists(destination)): os.mkdir(destination)
    dir_content = os.listdir(destination)
    for item in dir_content:
        if(os.path.isfile(os.path.join(destination,item))): os.remove(os.path.join(destination,item))
        else: shutil.rmtree(os.path.join(destination,item))
    source_content = os.listdir(src)
    for item in source_content:
        if os.path.isfile(os.path.join(src, item)): 
            shutil.copy(os.path.join(src, item), destination)
        else:
            copy_static(os.path.join(src, item), os.path.join(destination, item))

def generate_page(from_path, template_path, dest_path):
    if not os.path.exists(from_path): raise Exception("From Path doesnt' exist")
    if not os.path.exists(template_path): raise Exception("template Path doesnt' exist")
    if not os.path.exists(os.path.dirname(dest_path)): os.makedirs(os.path.dirname(dest_path))
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    src_f = open(from_path, 'r')
    src_md = src_f.read()
    src_f.close()
    FileTitle = extract_title(src_md)
    template_f = open(template_path, 'r')
    template_html = template_f.read()
    template_f.close()
    srcNode = markdown_to_html_node(src_md)
    src_html = srcNode.to_html()
    template_html = template_html.replace("{{ Title }}", FileTitle)
    template_html = template_html.replace("{{ Content }}", src_html)
    final_html = open(dest_path, 'w')
    final_html.write(template_html)
    final_html.close()


if __name__ == "__main__":
    main()