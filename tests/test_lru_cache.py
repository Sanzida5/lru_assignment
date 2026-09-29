import unittest
from src.lru_cache import Cache


class TestLRUCache(unittest.TestCase):
    def test_normal_operations_and_eviction(self):
        cache = Cache(2)
        cache.put('A', 10)
        cache.put('B', 20)
        self.assertEqual(cache.get('A'), 10)
        self.assertEqual(cache.put('C', 30), ('B', 20))
        self.assertEqual(cache.get('B'), -1)
        self.assertEqual(cache.get('C'), 30)
        self.assertEqual(cache.get('A'), 10)

    def test_missing_key(self):
        self.assertEqual(Cache(2).get('missing'), -1)

    def test_update_existing_key(self):
        cache = Cache(2)
        cache.put('A', 1)
        cache.put('B', 2)
        cache.put('A', 99)
        cache.put('C', 3)
        self.assertEqual(cache.get('A'), 99)
        self.assertEqual(cache.get('B'), -1)

    def test_capacity_one(self):
        cache = Cache(1)
        cache.put('A', 10)
        self.assertEqual(cache.put('B', 20), ('A', 10))
        self.assertEqual(cache.get('A'), -1)
        self.assertEqual(cache.get('B'), 20)

    def test_repeated_gets_change_recency(self):
        cache = Cache(2)
        cache.put('A', 1)
        cache.put('B', 2)
        self.assertEqual(cache.get('A'), 1)
        self.assertEqual(cache.get('A'), 1)
        cache.put('C', 3)
        self.assertEqual(cache.get('B'), -1)
        self.assertEqual(cache.get('A'), 1)

    def test_repeated_puts_update_recency(self):
        cache = Cache(2)
        cache.put('A', 1)
        cache.put('B', 2)
        cache.put('A', 10)
        cache.put('C', 3)
        self.assertEqual(cache.get('B'), -1)
        self.assertEqual(cache.get('A'), 10)

    def test_positive_capacity_required(self):
        for invalid in (0, -1, -10, 1.5, '2', True):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    Cache(invalid)

    def test_lru_order(self):
        cache = Cache(3)
        cache.put('A', 1)
        cache.put('B', 2)
        cache.put('C', 3)
        self.assertEqual(cache.keys_mru_to_lru(), ['C', 'B', 'A'])
        cache.get('A')
        self.assertEqual(cache.keys_mru_to_lru(), ['A', 'C', 'B'])


if __name__ == '__main__':
    unittest.main()
