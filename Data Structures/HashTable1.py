from utils import next_prime, previous_prime, hash1, hash2


class HashTable:
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __repr__(self):
            return str(f"{{{self.key}: {self.value}}}")

    def __init__(self, strategy="l"):
        self.length = 7
        self.size = 0
        self.grow_threshold = 0.5
        self.shrink_threshold = 0.125
        self.marker = object()
        self.table = [self.marker] * 7
        match(strategy):
            case "l":
                self.strategy = self.linear_probing
            case "q":
                self.strategy = self.quadratic_probing
            case "d":
                self.strategy = self.double_probing

    def __str__(self):
        return str(self.table)

    def linear_probing(self, key, iteration):
        return (hash1(key, self.length) + iteration) % self.length

    def quadratic_probing(self, key, iteration):
        return (hash1(key, self.length) + iteration ** 2) % self.length

    def double_probing(self, key, iteration):
        return (hash1(key, self.length) + (iteration * hash2(key, self.length))) % self.length

    def grow_condition(self, kwarg):
        return (self.size + len(kwarg) / self.length) > self.grow_threshold

    def shrink_condition(self, kwarg):
        return (self.size + len(kwarg) / self.length) < self.shrink_threshold and self.length > 7

    def grow(self):
        entries = [entry for entry in self.table if entry != self.marker]
        self.length = next_prime(self.length * 2)
        self.table = [self.marker] * self.length
        for entry in entries:
            self.update({entry.key: entry.value})

    def shrink(self):
        entries = [entry for entry in self.table if entry != self.marker]
        self.length = max(previous_prime(self.length / 2), 7)
        self.table = [self.marker] * self.length
        for entry in entries:
            self.update({entry.key: entry.value})

    def update(self, kwarg):
        def _update(key, value):
            for i in range(self.length):
                index = self.strategy(key, i)
                if self.table[index] == self.marker or self.table[index].key == key:
                    self.table[index] = self.Entry(key, value)
                    self.size += 1
                    return
            raise ValueError("hash table is full")
        if self.grow_condition(kwarg):
            self.grow()
        elif self.shrink_condition(kwarg):
            self.shrink()
        for key, value in kwarg.items():
            _update(key, value)

    def remove(self, key):
        if self.size == 0:
            raise ValueError("hash table is empty")
        for i in range(self.length):
            index = self.strategy(key, i)
            if self.table[index] != self.marker and self.table[index].key == key:
                self.table[index] = self.marker
                self.size -= 1
                return
        raise KeyError("entry not found")

    def get(self, key, default=None):
        if self.size == 0:
            raise ValueError("hash table is empty")
        for i in range(self.length):
            index = self.strategy(key, i)
            if self.table[index] != self.marker and self.table[index].key == key:
                return self.table[index].value
        return default
