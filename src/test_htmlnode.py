import unittest

from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "text", ["a", "b"], {"a1":"b1", "a2":"b2"})
        node2 = HTMLNode("p", "text", ["a", "b"], {"a1":"b1", "a2":"b2"})
        self.assertEqual(node, node2)

    def test_not_eq_enum(self):
        node = HTMLNode("p", "text", ["a", "b"], {"a1":"b1", "a2":"b2"})
        node3 = HTMLNode(props=None)
        self.assertNotEqual(node, node3)

    def test_not_eq_link(self):
        node = HTMLNode("p", "text", ["a", "b"], {"a1":"b1", "a2":"b2"})
        node4 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node4)
    
    def test_eq(self):
        node = LeafNode("p", "text", {"a1":"b1", "a2":"b2"})
        node2 = LeafNode("p", "text", {"a1":"b1", "a2":"b2"})
        self.assertEqual(node, node2)

    def test_not_eq_enum(self):
        node = LeafNode("p", "text", {"a1":"b1", "a2":"b2"})
        node3 = LeafNode("a", "other text", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node3)


if __name__ == "__main__":
    unittest.main()
