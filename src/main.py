from textnode import TextNode, TextType

def main():
    tempNode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(tempNode)

if __name__ == "__main__":
    main()
