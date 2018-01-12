########
# 二叉树
########

"""

二叉树是最简单的树型结构, 每个节点最多含有两个子树的树称为二叉树

完全二叉树: 除了最底层之外, 上面各个层的节点数都达到最大的节点

满二叉树: 所有层都要达到最大的节点

平衡二叉树: 即节点的两颗子树的高度差不大于1的二叉树

排序二叉树: 若左子树不空, 则左子树所有节点皆小于或等于根节点的值, 相反, 若右子树不空, 则都大于或等于根节点的值

应用场景:

1.xml,html
2.路由协议
3.Mysql数据库索引
4.文件系统的目录结构
5.AI算法


性质:
1. 在二叉树的第i层最多有2^(i-1)个结点
2. 深度为K的二叉树最多有2^k-1个结点(k>0)
3. 任意一个二叉树, 叶子结点的数目为度数为2的结点数目+1
4. 具有n个结点的完全二叉树的深度必为log2(n+1)
5. 一个完全二叉树, 从上到下, 从左到右编号, 那么编号为i的节点, 左孩子编号为2i, 右孩子编号为2i+1, 双亲编号为i/2

"""


class Node(object):
    """结点"""
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None


class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.lchild:
                queue.append(cur_node.lchild)
            if cur_node.rchild:
                queue.append(cur_node.rchild)

    # 先序遍历: 中->左->右
    # 中序遍历: 左->中->右
    # 后序遍历: 左->右->中
    def preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.elem, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def midorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.midorder(node.lchild)
        print(node.elem, end=' ')
        self.midorder(node.rchild)

    def endorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.endorder(node.lchild)
        self.endorder(node.rchild)
        print(node.elem, end=' ')


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(' ')
    tree.preorder(tree.root)
    print(' ')
    tree.midorder(tree.root)
    print(' ')
    tree.endorder(tree.root)

