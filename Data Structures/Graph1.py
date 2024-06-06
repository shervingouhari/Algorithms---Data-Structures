from collections import deque
from queue import PriorityQueue


class Graph:
    class Node:
        def __init__(self, label):
            self.label = label
            self.edges = set()
            self.distances = {}

        def __repr__(self):
            return str(f"{self.label} => {[f'{node.label}^{self.distances[node]}' for node in self.edges]}")

        def __lt__(self, other):
            return True

    def __init__(self):
        self.nodes = {}

    def __repr__(self):
        return str([node for node in self.nodes.values()])

    def __len__(self):
        return len(self.nodes)

    def add_node(self, label):
        node = self.nodes.get(label)
        if node == None:
            self.nodes.update({label: self.Node(label)})
        else:
            raise ValueError("node already exists")

    def remove_node(self, label):
        node = self.nodes[label]
        self.nodes.pop(label)
        for _node in self.nodes.values():
            if node in _node.edges:
                _node.edges.remove(node)
                _node.distances.pop(node)

    def add_edge(self, fr, to, distance=0):
        if distance < 0:
            raise ValueError("distance must be a positive number")
        fr = self.nodes[fr]
        to = self.nodes[to]
        if to in fr.edges:
            raise ValueError("edge already exists")
        fr.edges.add(to)
        fr.distances.update({to: distance})

    def remove_edge(self, fr, to):
        fr = self.nodes[fr]
        to = self.nodes[to]
        fr.edges.remove(to)
        fr.distances.pop(to)

    # pre-order
    def depth_first_traversal(self, fr):
        node = self.nodes[fr]
        _stack, _set, _array = [fr], set({node}), []
        while _stack:
            _list = self.nodes[_stack[-1]].edges
            _array.append(_stack.pop())
            for edge in _list:
                if edge not in _set:
                    _stack.append(edge.label)
                    _set.add(edge)
        return _array

    def breadth_first_traversal(self, fr):
        _queue = deque([fr])
        _set = set({self.nodes[fr]})
        _array = [fr]
        while _queue:
            linked_list = self.nodes[_queue.popleft()].edges
            for edge in linked_list:
                if edge not in _set:
                    _queue.append(edge.label)
                    _set.add(edge)
                    _array.append(edge.label)
        return _array

    # depth-first
    def has_cycle(self):
        all_nodes = set(self.nodes.values())
        while all_nodes:
            node = all_nodes.pop()
            _stack, _set = [node], set({node})
            while _stack:
                _list = _stack.pop().edges
                for edge in _list:
                    if edge not in _set:
                        _stack.append(edge)
                        _set.add(edge)
                        all_nodes.discard(edge)
                    elif edge == node:
                        return True
        return False

    # Dijkstra's algorithm (greedy)
    def shortest_path(self, fr, to):
        distance = {label: float("inf") for label in self.nodes.keys()}
        previous = {label: None for label in self.nodes.keys()}
        visiting = PriorityQueue()
        visited = set()
        path = deque()
        distance.update({fr: 0})
        visiting.put([0, self.nodes[fr]])

        while not visiting.empty():
            node = visiting.get()[1]
            for edge in node.edges:
                if edge not in visited:
                    visiting.put([node.distances[edge], edge])
                    total_distance = distance[node.label] + \
                        node.distances[edge]
                    if total_distance < distance[edge.label]:
                        distance.update({edge.label: total_distance})
                        previous.update({edge.label: node})
            visited.add(node)

        current = self.nodes[to]
        while current != None:
            path.appendleft(current.label)
            current = previous[current.label]
        return path, distance[to]

    # Prim's algorithm (greedy)
    def minimum_spanning_tree(self, fr):
        '''only works on undirected graphs'''
        node = self.nodes[fr]
        graph = Graph()
        graph.add_node(node.label)
        visited = set()
        minimum_distance = 0
        while len(visited) != len(self):
            visiting = PriorityQueue()
            visited.add(node)
            for edge in node.edges:
                if edge not in visited:
                    visiting.put([node.distances[edge], edge])
            if not visiting.empty():
                new_distance, new_node = visiting.get()
                minimum_distance += new_distance
                graph.add_node(new_node.label)
                graph.add_edge(node.label, new_node.label, new_distance)
                graph.add_edge(new_node.label, node.label, new_distance)
                node = new_node
            else:
                break
        return graph, minimum_distance
