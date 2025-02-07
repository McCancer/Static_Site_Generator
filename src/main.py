import os
import shutil
from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from nodefuncs import *
from markdown_blocks import *

def main():
    copy_static('static','public')
    generate_pages_recursive('content','template.html','public')
    
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
    '''
    generate_page

    :param from_page:
    :param template_path:
    :param dest_path: 
    '''
    if not os.path.exists(from_path): raise Exception("From Path doesnt' exist")
    if not os.path.exists(template_path): raise Exception("template Path doesnt' exist")
    if not os.path.exists(os.path.dirname(dest_path)): os.makedirs(os.path.dirname(dest_path))
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    #Open source File and read content
    src_f = open(from_path, 'r')
    src_md = src_f.read()
    src_f.close()
    #Open Tempalte file and read content
    template_f = open(template_path, 'r')
    template_html = template_f.read()
    template_f.close()
    #Data transform the src data
    srcNode = markdown_to_html_node(src_md)
    src_html = srcNode.to_html()
    FileTitle = extract_title(src_md)
    #Replace place holders in templates
    template_html = template_html.replace("{{ Title }}", FileTitle)
    template_html = template_html.replace("{{ Content }}", src_html)
    #Write Final File
    final_html = open(dest_path, 'w')
    final_html.write(template_html)
    final_html.close()

def generate_pages_recursive(src_path_content, template_path, dest_dir_path):
    '''
    generate_pages_recursive

    :param src_path_content:
    :param template_path:
    :param des_dir_path: 
    '''
    if not os.path.exists(src_path_content): raise Exception("From Path doesnt' exist")
    if not os.path.exists(template_path): raise Exception("template Path doesnt' exist")
    if not os.path.exists(dest_dir_path): os.makedirs(dest_dir_path)
    for item in os.listdir(src_path_content):
        new_src_path = os.path.join(src_path_content, item)
        new_dest_path = os.path.join(dest_dir_path, item)
        if(os.path.isfile(new_src_path)):
            base, ext = os.path.splitext(item)
            new_dest_path = os.path.join(dest_dir_path, f"{base}.html")
            generate_page(new_src_path, template_path, new_dest_path)
        else: 
            new_dest_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(new_src_path,template_path,new_dest_path)

if __name__ == "__main__":
    main()