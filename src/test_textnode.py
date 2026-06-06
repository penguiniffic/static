import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is the first text node", TextType.ITALIC)
        node2 = TextNode("This is the second text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node with a link",
                        TextType.BOLD, "https://www.boot/dev")
        node2 = TextNode("This is a text node with a link", TextType.BOLD,
                         "https://www.boot/dev")
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node with a link",
                        TextType.BOLD, "https://www.boot/dev")
        node2 = TextNode("This is a text node with a link", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff_type(self):
        node = TextNode("This is a text node with a link",
                        TextType.BOLD, "https://www.boot/dev")
        node2 = TextNode("This is a text node with a link", TextType.IMAGE,
                         "https://www.boot/dev")
        self.assertNotEqual(node, node2)

    def test_diff_text(self):
        node = TextNode("This is a text node with a link",
                        TextType.BOLD, "https://www.boot/dev")
        node2 = TextNode("This is a text node with a different link", TextType.BOLD,
                         "https://www.boot/dev")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold(self):
        node = TextNode("This is a BOLD node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a BOLD node")

    def test_text_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_text_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_text_link(self):
        node = TextNode("This is a link node", TextType.LINK,
                        "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_text_image(self):
        node = TextNode("This is an image node", TextType.IMAGE,
                        "https://www.boot.dev/img/bear.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {
                         "src": "https://www.boot.dev/img/bear.jpg", "alt": "This is an image node"})


if __name__ == "__main__":
    unittest.main()
