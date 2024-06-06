class Set:
    def __init__(self, _set=None):
        if _set != None and not isinstance(_set, set):
            raise TypeError("you must provide a set")
        self.table = {}
        if _set != None:
            for item in _set:
                self.add(item)

    def __str__(self):
        return str(set(self.table.values()))

    def __len__(self):
        return len(self.table)

    def __contains__(self, item):
        try:
            self.table[item]
            return True
        except KeyError:
            return False

    def __iter__(self):
        return iter(self.table.values())

    def add(self, item):
        if item not in self:
            self.table.update({item: item})

    def copy(self):
        return set(self.table.copy())

    def pop(self):
        return self.table.popitem()[0]

    def discard(self, item):
        if item in self:
            self.table.pop(item)

    def remove(self, item):
        self.table.pop(item)

    def clear(self):
        self.table.clear()

    def issubset(self, _set):
        for item in self:
            if item not in _set:
                return False
        return True

    def issuperset(self, _set):
        for item in _set:
            if item not in self:
                return False
        return True

    def isdisjoint(self, _set):
        for item in _set:
            if item in self:
                return False
        return True

    def difference(self, _set):
        difference = Set()
        for item in self:
            if item not in _set:
                difference.add(item)
        return difference

    def difference_update(self, _set):
        for item in _set:
            if item in self:
                self.remove(item)

    def intersection(self, _set):
        intersection = Set()
        if len(self) < len(_set):
            for item in self:
                if item in _set:
                    intersection.add(item)
        else:
            for item in _set:
                if item in self:
                    intersection.add(item)
        return intersection

    def intersection_update(self, _set):
        intersection = self.intersection(_set)
        for item in self:
            if item not in intersection:
                self.remove(item)

    def symmetric_difference(self, _set):
        symmetric_difference = Set(set(self))
        for item in _set:
            if item in self:
                symmetric_difference.remove(item)
            else:
                symmetric_difference.add(item)
        return symmetric_difference

    def symmetric_difference_update(self, _set):
        for item in _set:
            if item in self:
                self.remove(item)
            else:
                self.add(item)

    def union(self, _set):
        union = self.copy()
        for item in _set:
            if item not in union:
                union.add(item)
        return union

    def update(self, _set):
        for item in _set:
            if item not in self:
                self.add(item)
