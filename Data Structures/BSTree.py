class BSTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return str(self.value)

        def __lt__(self, other):
            return self.value < other.value

        def __gt__(self, other):
            return self.value > other.value

        def is_valid(self):
            if (
                (self.left == None or self.left < self) and
                (self.right == None or self.right > self)
            ):
                return True
            return False

        def left0_right1(self):
            return self.left == None and self.right != None

        def left1_right0(self):
            return self.right == None and self.left != None

        def left1_right1(self):
            return self.right != None and self.left != None

        def replace_with_successor(self):
            first = self.right
            second = first.left
            if second == None:
                self.value = first.value
                self.right = first.right
            else:
                while second.left != None:
                    first, second = second, second.left
                self.value = second.value
                first.left = second.right
            return self

    def __init__(self):
        self.root = None

    def is_BST(self):
        def _is_BST(node):
            if node == None:
                return True
            if not node.is_valid():
                return False
            return (_is_BST(node.left) and _is_BST(node.right))
        return _is_BST(self.root)

    def equals(self, tree):
        def _equals(node1, node2):
            if node1 == node2:
                return True
            if node1 != None and node2 != None:
                return (node1.value == node2.value and
                        _equals(node1.left, node2.left) and
                        _equals(node1.right, node2.right))
            return False
        return _equals(self.root, tree.root)

    def insert(self, value):
        def _insert(node):
            if node == None:
                node = self.Node(value)
            elif value < node.value:
                node.left = _insert(node.left)
            elif value > node.value:
                node.right = _insert(node.right)
            else:
                return
            return node
        self.root = _insert(self.root)

    def remove(self, value):
        def _remove(node):
            if node == None:
                raise ValueError("node not found")
            if value < node.value:
                node.left = _remove(node.left)
            elif value > node.value:
                node.right = _remove(node.right)
            else:
                if node.left1_right0():
                    node = node.left
                elif node.left0_right1():
                    node = node.right
                elif node.left1_right1():
                    node = node.replace_with_successor()
                else:
                    node = None
            return node
        self.root = _remove(self.root)

    def contains(self, value):
        def _contains(node):
            if node == None:
                return False
            if value < node.value:
                return _contains(node.left)
            elif value > node.value:
                return _contains(node.right)
            return True
        return _contains(self.root)

    # depth-first
    def traverse_pre_order(self):
        def _traverse_pre_order(node):
            if node == None:
                return
            print(node.value)
            _traverse_pre_order(node.left)
            _traverse_pre_order(node.right)
        _traverse_pre_order(self.root)

    # depth-first
    def traverse_in_order(self):
        def _traverse_in_order(node):
            if node == None:
                return
            _traverse_in_order(node.left)
            print(node.value)
            _traverse_in_order(node.right)
        _traverse_in_order(self.root)

    # depth-first
    def traverse_post_order(self):
        def _traverse_post_order(node):
            if node == None:
                return
            _traverse_post_order(node.left)
            _traverse_post_order(node.right)
            print(node.value)
        _traverse_post_order(self.root)

    # breadth-first
    def traverse_level_order(self):
        def _traverse_level_order(node):
            for level in range(self.height(node) + 1):
                self.nodes_at_distance(level)
        _traverse_level_order(self.root)

    def nodes_at_distance(self, distance):
        def _nodes_at_distance(node, distance):
            if node == None:
                return
            if distance == 0:
                print(node.value)
            else:
                _nodes_at_distance(node.left, distance - 1)
                _nodes_at_distance(node.right, distance - 1)
        _nodes_at_distance(self.root, distance)

    def height(self, node=None):
        def _height(node):
            if node == None or node.left == node.right:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(node if node else self.root)

    def minimum(self, node=None):
        current = node or self.root
        while current.left is not None:
            current = current.left
        return current

    def maximum(self, node=None):
        current = node or self.root
        while current.right is not None:
            current = current.right
        return current
