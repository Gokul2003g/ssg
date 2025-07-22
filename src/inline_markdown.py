from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []

        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Markdown not closed properly")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.NORMAL_TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    alt_texts = re.findall(r"\[(.*?)\]", text)
    urls = re.findall(r"\((.*?)\)", text)
    alt_text_and_urls = list(tuple(zip(alt_texts, urls)))
    return alt_text_and_urls


def extract_markdown_links(text):
    anchor_texts = re.findall(r"\[(.*?)\]", text)
    urls = re.findall(r"\((.*?)\)", text)
    anchor_text_and_urls = list(tuple(zip(anchor_texts, urls)))
    return anchor_text_and_urls


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        sections = re.split(r"\[.*?\]\(.*?\)", old_node.text)
        if sections[-1] == "":
            sections.pop()
        alt_text_and_urls = extract_markdown_images(old_node.text)
        markdown_index = 0
        for _, section in enumerate(sections):
            new_nodes.append(TextNode(section, TextType.NORMAL_TEXT))
            new_nodes.append(
                TextNode(
                    alt_text_and_urls[markdown_index][0],
                    TextType.LINK,
                    alt_text_and_urls[markdown_index][1],
                )
            )
            markdown_index += 1

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        sections = re.split(r"\!\[.*?\]\(.*?\)", old_node.text)
        if sections[-1] == "":
            sections.pop()
        alt_text_and_urls = extract_markdown_images(old_node.text)
        markdown_index = 0
        for _, section in enumerate(sections):
            new_nodes.append(TextNode(section, TextType.NORMAL_TEXT))
            new_nodes.append(
                TextNode(
                    alt_text_and_urls[markdown_index][0],
                    TextType.IMAGE,
                    alt_text_and_urls[markdown_index][1],
                )
            )
            markdown_index += 1

    return new_nodes
