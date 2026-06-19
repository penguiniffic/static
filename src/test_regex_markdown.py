import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links


class TestRegexMarkdown(unittest.TestCase):
    def test_extract_markdown_images_singular(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with a multiple images. This is the first ![image](https://i.imgur.com/zjjcJKZ.png). And here is the second ![image_two](https://i.imgur.com/abcdeg.jpg)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png"), ("image_two", "https://i.imgur.com/abcdeg.jpg")], matches)

    def test_extract_markdown_links_singular(self):
        matches = extract_markdown_links(
            "This is text with a single link [to some rando site](https://espn.com)"
        )
        self.assertListEqual(
            [("to some rando site", "https://espn.com")], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)


if __name__ == "__main__":
    unittest.main()
