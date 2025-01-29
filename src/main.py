from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    tempNode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(tempNode)

    htmlNode = HTMLNode()
    print(htmlNode)

if __name__ == "__main__":
    main()
