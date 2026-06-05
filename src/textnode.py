from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str = None):
        if not isinstance(text_type, TextType):
            raise TypeError(
                f"text_type must be an instance of the TextType Enum, not {type(text_type)}")

        self.text = text
        self.text_type = text_type
        if not url:
            self.url = None
        else:
            self.url = url

    def __eq__(self, other) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
