from lru_cache import Cache


def show_put(cache, key, value):
    evicted = cache.put(key, value)
    print(f'put({key!r}, {value})')
    if evicted is not None:
        evicted_key, evicted_value = evicted
        print(f'  LRU eviction: {evicted_key!r} -> {evicted_value}')
    print(f'  order MRU -> LRU: {cache.keys_mru_to_lru()}')


def show_get(cache, key):
    value = cache.get(key)
    print(f'get({key!r}) -> {value}')
    print(f'  order MRU -> LRU: {cache.keys_mru_to_lru()}')
    return value


def main():
    print('LRU Cache demonstration (capacity = 2)')
    print('-' * 42)
    cache = Cache(2)
    show_put(cache, 'A', 10)
    show_put(cache, 'B', 20)
    show_get(cache, 'A')
    show_put(cache, 'C', 30)
    show_get(cache, 'B')
    show_get(cache, 'C')
    show_get(cache, 'A')


if __name__ == '__main__':
    main()
