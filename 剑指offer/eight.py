# 给定一颗二叉树和其中的一个节点，找出中序遍历的下一个节点


class Tree:
    def __init__(self, node, parent=None, left_child=None, right_child=None):
        self.node = node
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


def find_next_node(node):
    if node is None:
        return None

    # 有右子树的话，则返回右子树中的最左边的节点

    if node.right_child:
        next_node = node.right_child
        while next_node.left_child:
            next_node = next_node.left_child
        return next_node

    if node.parent:
        parent = node.parent

        # 节点是父节点的左节点，则返回父节点
        if id(node) == id(parent.left_child):
            return parent

        # 节点是父节点的右节点，则返回左节点的祖先节点的父节点
        if id(node) == id(parent.right_child):
            while parent.parent:
                if id(parent) == id(parent.parent.left_child):
                    return parent.parent
                parent = parent.parent
    return None
