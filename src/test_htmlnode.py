import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    
    '''
    dummy_3 = HTMLNode("p", "text", ["a", "b"], {"a1":"b1", "a2":"b2"})
    print(dummy_3.__repr__())

    line = ""
    line = dummy_3.props_to_html()
    print(line)

    node = HTMLNode(props=None)
    print(node.__repr__())
    print(node.props_to_html())

    node2 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    print(node2.__repr__())
    print(node2.props_to_html())

    leaf1 = LeafNode("p", "text", {"a1":"b1", "a2":"b2"})
    print(leaf1.__repr__())
    print(leaf1.to_html())

    leaf2 = LeafNode("p", "text")
    print(leaf2.__repr__())
    print(leaf2.to_html())
    

    leaf1 = LeafNode("p", "text", {"a1":"b1", "a2":"b2"})
    print(leaf1.__repr__())

    leaf2 = LeafNode("b", "text2")
    print(leaf2.__repr__())

    parent = ParentNode("a", [leaf1])
    print(parent.__repr__())
    print(parent.to_html())

    parent2 = ParentNode("c", [leaf1, leaf2], {"c1":"d1"})
    print(parent2.__repr__())
    print(parent2.to_html())
    '''
    
    
""" 
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
    
    def test_eq_leaf(self):
        node = LeafNode("p", "text", {"a1":"b1", "a2":"b2"})
        node2 = LeafNode("p", "text", {"a1":"b1", "a2":"b2"})
        self.assertEqual(node, node2)

    def test_not_eq_enum_leaf(self):
        node = LeafNode("p", "text", {"a1":"b1", "a2":"b2"})
        node3 = LeafNode("a", "other text", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node3)

    def test_eq_parent(self):
        leaf1 = LeafNode("b", "text2")
        leaf2 = LeafNode("b", "text2")
        node = ParentNode("a", [leaf1])
        node2 = ParentNode("a", [leaf2])
        self.assertEqual(node, node2)

    def test_eq_parent_value(self):
        leaf1 = LeafNode("b", "text2")
        node = ParentNode("a", [leaf1])
        self.assertEqual(node.value, None)

    def test_eq_parent_props(self):
        leaf1 = LeafNode("b", "text2")
        node = ParentNode("a", [leaf1], {"a": "b"})
        self.assertEqual(node.props, {"a": "b"})

    def test_eq_parent_props_2(self):
        leaf1 = LeafNode("b", "text2")
        node = ParentNode("a", [leaf1])
        self.assertEqual(node.props, None)

    def test_eq_parent_children(self):
        leaf1 = LeafNode("b", "text2")
        leaf2 = LeafNode("b", "text2")
        node = ParentNode("a", [leaf1])
        self.assertEqual(node.children[0], leaf2)
"""

if __name__ == "__main__":
    unittest.main()
