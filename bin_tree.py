class Node:
    def __init__(self, value, par_node=None):
        self.value = value
        self.parent = par_node
        self.left_child: Node = None
        self.right_child: Node = None
        self.high = 0

    def set_left_child(self, node):
        self.left_child = node

    def set_right_child(self, node):
        self.right_child = node

    def hasRightChild(self):
        if self.right_child:
            return True
        return False

    def hasLeftChild(self):
        if self.left_child:
            return True
        return False

    def hasBothChild(self):
        if self.right_child and self.left_child:
            return True
        return False

    def isRoot(self):
        if not self.parent:
            return True
        return False

    def isLeftChild(self):
        if self.parent.left_child == self:
            return True
        return False

    def isRightChild(self):
        if self.parent.right_child == self:
            return True
        return False


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0
        self.high = 0

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
        self.count += 1

    def _insert(self, cur_node, value):
        if cur_node.value > value:
            if not cur_node.left_child:
                cur_node.set_left_child(Node(value, cur_node))
            else:
                self._insert(cur_node.left_child, value)
        else:
            if not cur_node.right_child:
                cur_node.set_right_child(Node(value, cur_node))
            else:
                self._insert(cur_node.right_child, value)

    def print_in_order(self):
        if self.root:
            answer_list = []
            self._print_in_order(self.root, answer_list)
            return answer_list

    def _print_in_order(self, cur_node, answer_list):
        if cur_node.left_child:
            self._print_in_order(cur_node.left_child, answer_list)
        answer_list.append(
            [
                cur_node.value,
                cur_node.parent.value if cur_node.parent is not None else None,
            ]
        )
        if cur_node.right_child:
            self._print_in_order(cur_node.right_child, answer_list)

    def postOrder(self):
        if self.root:
            answer_list = []
            self._postOrder(self.root, answer_list)
            return answer_list

    def _postOrder(self, cur_node, answer_list):
        if cur_node.left_child:
            self._postOrder(cur_node.left_child, answer_list)
        if cur_node.right_child:
            self._postOrder(cur_node.right_child, answer_list)
        answer_list.append(cur_node.value)

    def preOrder(self):
        if self.root:
            answer_list = []
            self._preOrder(self.root, answer_list)
            return answer_list

    def _preOrder(self, cur_node, answer_list):
        answer_list.append(cur_node.value)
        if cur_node.left_child:
            self._preOrder(cur_node.left_child, answer_list)
        if cur_node.right_child:
            self._preOrder(cur_node.right_child, answer_list)

    def find(self, value):
        cur_node = self.root
        return self._find(value, cur_node)

    def _find(self, value, cur_node):
        if not cur_node:
            return False

        if value == cur_node.value:
            return True
        elif value < cur_node.value:
            return self._find(value, cur_node.left_child)
        else:
            return self._find(value, cur_node.right_child)

    def find_node(self, value):
        cur_node = self.root
        return self._find_node(value, cur_node)

    def _find_node(self, value, cur_node):
        if not cur_node:
            return None
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value:
            return self._find_node(value, cur_node.left_child)
        else:
            return self._find_node(value, cur_node.right_child)

    def delete(self, value):
        cur_node = self.find_node(value)
        if not cur_node:
            return False
        self._delete_node(cur_node)
        self.count -= 1

    def _delete_node(self, cur_node):
        if cur_node.isRoot():
            if cur_node.hasBothChild():
                self._delleteIfRootHasBoth(cur_node)
            elif cur_node.hasLeftChild():
                self._delleteIfRootHasLeft(cur_node)
            elif cur_node.hasRightChild():
                self._delleteIfRootHasRight(cur_node)
            else:
                self.root = None
        else:
            parent = cur_node.parent
            if cur_node.hasBothChild():
                self._delleteIfHasBoth(parent, cur_node)
            elif cur_node.hasLeftChild():
                self._delleteIfHasLeft(parent, cur_node)
            elif cur_node.hasRightChild():
                self._delleteIfHasRight(parent, cur_node)
            else:
                self._delleteIfHasNot(parent, cur_node)

    def _delleteIfRootHasBoth(self, cur_node: Node):
        left_child = cur_node.left_child
        right_child = cur_node.right_child
        if right_child.hasLeftChild():
            min_node_right = self._find_min(right_child)
            min_node_right.parent.left_child = None
            min_node_right.parent = None
            min_node_right.left_child = left_child
            left_child.parent = min_node_right
            min_node_right.right_child = right_child
            right_child.parent = min_node_right
            self.root = min_node_right
        else:
            right_child.parent = None
            right_child.left_child = left_child
            left_child.parent = right_child
            self.root = right_child

    def _delleteIfRootHasLeft(self, cur_node):
        left_child = cur_node.left_child
        left_child.parent = None
        self.root = left_child

    def _delleteIfRootHasRight(self, cur_node):
        right_child = cur_node.right_child
        right_child.parent = None
        self.root = right_child

    def _delleteIfHasNot(self, parent, cur_node):
        if cur_node.isRightChild():
            parent.right_child = None
        else:
            parent.left_child = None

    def _delleteIfHasBoth(self, parent, cur_node):
        left_child = cur_node.left_child
        right_child = cur_node.right_child
        if right_child.hasLeftChild():
            min_node_right = self._find_min(right_child)
            min_node_right.parent.left_child = None
            min_node_right.parent = parent
            min_node_right.left_child = left_child
            left_child.parent = min_node_right
            min_node_right.right_child = right_child
            right_child.parent = min_node_right
        else:
            right_child.parent = parent
            parent.left_child = right_child
            right_child.left_child = left_child
            left_child.parent = right_child

    def _delleteIfHasLeft(self, parent, cur_node):
        left_child = cur_node.left_child
        left_child.parent = parent
        parent.left_child = left_child

    def _delleteIfHasRight(self, parent, cur_node):
        right_child = cur_node.right_child
        right_child.parent = parent
        parent.right_child = right_child

    def _find_min(self, cur_node):
        if cur_node.left_child:
            cur_node = cur_node.left_child
            return self._find_min(cur_node)
        return cur_node

    def count_node(self):
        return self.count

    def hight_tree(self):
        return self._hight_tree(self.root)

    def _hight_tree(self, cur_node):
        if cur_node:
            return (
                max(
                    self._hight_tree(cur_node.left_child),
                    self._hight_tree(cur_node.right_child),
                )
                + 1
            )
        return 0

    def width_tree(self):
        return self._width_tree(self.root, 0, {})

    def _width_tree(self, cur_node, floor, width_list):
        if cur_node:
            width_list[floor] = width_list.get(floor, 0) + 1
            self._width_tree(cur_node.right_child, floor + 1, width_list)
            self._width_tree(cur_node.left_child, floor + 1, width_list)
            return max(width_list.values())
