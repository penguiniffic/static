from textnode import TextNode, TextType


def main():
    test_text = TextNode("test anchor text",
                         TextType.LINK_TEXTTYPE, "https://boot.dev")
    print(test_text)


if __name__ == "__main__":
    main()
