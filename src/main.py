import os
import shutil
from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from nodefuncs import *
from markdown_blocks import *

def main():
    copy_static("static", "public")
    
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
    
if __name__ == "__main__":
    main()