class Node:
    __slots__ = ('key', 'value', 'prev', 'next')

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class Cache:
    """Least Recently Used cache with O(1) average get/put operations."""

    def __init__(self, capacity: int):
        if not isinstance(capacity, int) or isinstance(capacity, bool) or capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        self.capacity = capacity
        self._nodes = {}
        self._head = Node()  # MRU sentinel
        self._tail = Node()  # LRU sentinel
        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key):
        node = self._nodes.get(key)
        if node is None:
            return -1
        self._move_to_mru(node)
        return node.value

    def put(self, key, value):
        node = self._nodes.get(key)
        if node is not None:
            node.value = value
            self._move_to_mru(node)
            return None

        node = Node(key, value)
        self._nodes[key] = node
        self._add_after_head(node)

        if len(self._nodes) > self.capacity:
            lru = self._tail.prev
            self._remove(lru)
            del self._nodes[lru.key]
            return lru.key, lru.value
        return None

    def keys_mru_to_lru(self):
        keys = []
        node = self._head.next
        while node is not self._tail:
            keys.append(node.key)
            node = node.next
        return keys

    def _move_to_mru(self, node):
        self._remove(node)
        self._add_after_head(node)

    def _add_after_head(self, node):
        first = self._head.next
        node.prev = self._head
        node.next = first
        self._head.next = node
        first.prev = node

    @staticmethod
    def _remove(node):
        node.prev.next = node.next
        node.next.prev = node.prev
