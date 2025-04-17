class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html_str = " "
        if self.props is None:
            raise Exception("Props is empty")

        for prop in self.props:
            html_str += f'{prop}="{self.props[prop]}" '
        print(html_str)
        return html_str.rstrip()

    def __repr__(self) -> str:
        return f"Tag=[{self.tag}]\nValue=[{self.value}]\nChildren=[{self.children}]\nProps=[{self.props}]"
