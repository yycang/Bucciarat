# 根据前序遍历和中序遍历来判断一颗树的结构


class Tree:
    def __init__(self, node, left_child=None, right_child=None):
        self.node = node
        self.left_child = left_child
        self.right_child = right_child


def create_tree(preorder, inorder):
    if not preorder or not inorder or len(preorder) != len(inorder):
        return

    root = create_tree_node(preorder, inorder)
    return root


def create_tree_node(preorder, inorder):
    if len(preorder) == 0:
        return None

    root = Tree(preorder[0])

    root_index = inorder.index(preorder[0])
    root.left_child = create_tree_node(preorder[1:root_index + 1],
                                       inorder[:root_index])
    root.right_child = create_tree_node(preorder[root_index + 1:],
                                        inorder[root_index + 1:])
    return root


def print_tree(node):
    if node is None:
        return
    print_tree(node.left_child)
    print_tree(node.right_child)
    print(node.node)


if __name__ == '__main__':
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    root = create_tree(preorder, inorder)
    print_tree(root)