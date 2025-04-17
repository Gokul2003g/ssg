from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    textNode = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(textNode)

    htmlNode = HTMLNode(
        tag="a",
        props={"href": "https://example.com", "target": "_blank"},
    )
    htmlNode.props_to_html()
    print(htmlNode)


main()
