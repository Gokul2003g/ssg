from blocktype import Markdown

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block) -> Markdown:
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return Markdown.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return Markdown.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return Markdown.PARAGRAPH
        return Markdown.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return Markdown.PARAGRAPH
        return Markdown.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return Markdown.PARAGRAPH
            i += 1
        return Markdown.ORDERED_LIST
    return Markdown.PARAGRAPH


    