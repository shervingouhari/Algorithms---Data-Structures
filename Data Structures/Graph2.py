from collections import deque
from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.index = {}
        self.label = {}
        self.matrix = []
        self.size = 0

    def display(self):
        labels = "  ".join(self.label.values())
        print("  ", labels)
        for label, index in self.index.items():
            print(f"{label} {self.matrix[index]}")

    def add_node(self, label):
        node = self.index.get(label)
        if node == None:
            self.index.update({label: self.size})
            self.label.update({self.size: label})
            self.size += 1
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * self.size)
        else:
            raise ValueError("node already exists")

    def remove_node(self, label):
        index = self.index[label]
        del self.index[label]
        del self.matrix[index]
        for row in self.matrix:
            del row[index]

    def add_edge(self, fr, to, distance=1):
        if distance < 1:
            raise ValueError("distance must be a positive number")
        fr = self.index[fr]
        to = self.index[to]
        if self.matrix[fr][to] == 0:
            self.matrix[fr][to] = distance
        else:
            raise ValueError("edge already exists")

    def remove_edge(self, fr, to):
        fr = self.index[fr]
        to = self.index[to]
        if self.matrix[fr][to] > 0:
            self.matrix[fr][to] = 0
        else:
            raise ValueError("edge does not exist")

    # pre-order
    def depth_first_traversal(self, fr):
        node = self.index[fr]
        _stack, _set, _array = [node], set({node}), []
        while _stack:
            index = _stack[-1]
            _array.append(self.label[_stack.pop()])
            for edge in range(self.size):
                if self.matrix[index][edge] > 0 and edge not in _set:
                    _stack.append(edge)
                    _set.add(edge)
        return _array

    def breadth_first_traversal(self, fr):
        node = self.index[fr]
        _queue = deque([node])
        _set = set({node})
        _array = [self.label[node]]
        while _queue:
            index = _queue.popleft()
            for edge in range(self.size):
                if self.matrix[index][edge] > 0 and edge not in _set:
                    _queue.append(edge)
                    _set.add(edge)
                    _array.append(self.label[edge])
        return _array

    # depth-first
    def has_cycle(self):
        all_nodes = set(self.index.values())
        while all_nodes:
            node = all_nodes.pop()
            _stack, _set = [node], set({node})
            while _stack:
                index = _stack.pop()
                for edge in range(self.size):
                    if self.matrix[index][edge] > 0 and edge not in _set:
                        all_nodes.discard(edge)
                        _stack.append(edge)
                        _set.add(edge)
                    elif self.matrix[index][edge] > 0 and edge == node:
                        return True
        return False

    # Dijkstra's algorithm (greedy)
    def shortest_path(self, fr, to):
        distance = {label: float("inf") for label in self.label.values()}
        previous = {label: None for label in self.label.values()}
        visiting = PriorityQueue()
        visited = set()
        path = deque()
        distance.update({fr: 0})
        visiting.put([0, self.index[fr]])

        while not visiting.empty():
            index = visiting.get()[1]
            for edge in range(self.size):
                if self.matrix[index][edge] > 0 and edge not in visited:
                    visiting.put([self.matrix[index][edge], edge])
                    total_distance = self.matrix[index][edge] + \
                        distance[self.label[index]]
                    if total_distance < distance[self.label[edge]]:
                        distance.update({self.label[edge]: total_distance})
                        previous.update({self.label[edge]: self.label[index]})
            visited.add(index)

        current = to
        while current != None:
            path.appendleft(current)
            current = previous[current]
        return path, distance[to]

    # Prim's algorithm (greedy)
    def minimum_spanning_tree(self, fr):
        '''only works on undirected graphs'''
        index = self.index[fr]
        graph = Graph()
        graph.add_node(fr)
        visited = set()
        minimum_distance = 0
        while len(visited) != self.size:
            visiting = PriorityQueue()
            visited.add(index)
            for edge in range(self.size):
                if self.matrix[index][edge] > 0 and edge not in visited:
                    visiting.put([self.matrix[index][edge], self.label[edge]])
            if not visiting.empty():
                new_distance, new_label = visiting.get()
                minimum_distance += new_distance
                graph.add_node(new_label)
                graph.add_edge(self.label[index], new_label, new_distance)
                graph.add_edge(new_label, self.label[index], new_distance)
                index = self.index[new_label]
            else:
                break
        return graph, minimum_distance
