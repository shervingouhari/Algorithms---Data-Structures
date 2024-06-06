from collections import deque


class AVLTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 0

        def __str__(self):
            return str(self.value)

        def __lt__(self, other):
            return self.value < other.value

        def __gt__(self, other):
            return self.value > other.value

        def is_valid(self):
            left_height, right_height = self.get_height()
            if (
                (self.left == None or self.left < self) and
                (self.right == None or self.right > self) and
                abs(left_height - right_height) <= 1
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

        def set_height(self):
            left_height, right_height = self.get_height()
            self.height = max(left_height, right_height) + 1

        def get_height(self):
            left_height = self.left.height if self.left else -1
            right_height = self.right.height if self.right else -1
            return left_height, right_height

        def rotation(self):
            left_height, right_height = self.get_height()
            is_left_heavy = (left_height - right_height) > 1
            is_right_heavy = (right_height - left_height) > 1
            if is_left_heavy:
                if self.left.left != None:
                    return "R"
                return "LR"
            elif is_right_heavy:
                if self.right.right != None:
                    return "L"
                return "RL"
            return None

        def right_rotation(self):
            new_node = self.left
            self.left = new_node.right
            new_node.right = self
            self.set_height()
            new_node.set_height()
            return new_node

        def left_rotation(self):
            new_node = self.right
            self.right = new_node.left
            new_node.left = self
            self.set_height()
            new_node.set_height()
            return new_node

        def balance(self):
            protocol = self.rotation()
            if protocol == None:
                return self
            elif protocol == "L":
                return self.left_rotation()
            elif protocol == "R":
                return self.right_rotation()
            elif protocol == "LR":
                self.left = self.left.left_rotation()
                return self.right_rotation()
            elif protocol == "RL":
                self.right = self.right.right_rotation()
                return self.left_rotation()

    def __init__(self):
        self.root = None

    def is_AVLTree(self):
        def _is_AVLTree(node):
            if node == None:
                return True
            if not node.is_valid():
                return False
            return (_is_AVLTree(node.left) and _is_AVLTree(node.right))
        return _is_AVLTree(self.root)

    def insert(self, value):
        def _insert(node):
            if node == None:
                return self.Node(value)
            if value < node.value:
                node.left = _insert(node.left)
            elif value > node.value:
                node.right = _insert(node.right)
            else:
                return
            node.set_height()
            return node.balance()
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
                    return None
            node.set_height()
            return node.balance()
        self.root = _remove(self.root)

    def traverse_level_order(self):
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
