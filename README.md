# LRU Cache — Task 2

A production-quality Least Recently Used (LRU) cache implementing `Cache(capacity)`, `get(key)`, and `put(key, value)` with **O(1) average time** for both operations.

## Requirements implemented

- Capacity must be a positive integer; otherwise `ValueError` is raised.
- `get(key)` returns the stored value, or `-1` when the key does not exist.
- A successful `get()` marks the key as most recently used (MRU).
- `put(key, value)` inserts or updates a value and marks the key MRU.
- Inserting beyond capacity evicts the least recently used (LRU) entry.
- The assignment example and comprehensive automated tests are included.

## Data structures and why

The cache combines a **hash map (Python dictionary)** with a **doubly linked list**. The dictionary maps each key directly to its linked-list node, giving O(1) average lookup. The doubly linked list stores recency order and permits O(1) removal/reinsertion because each node has direct `prev` and `next` references.

Two sentinel nodes simplify boundary handling. The node immediately after `head` is the **MRU** item; the node immediately before `tail` is the **LRU** item.

## How LRU ordering is maintained

A successful `get()` removes the accessed node from its current list position and inserts it immediately after `head`. `put()` does the same for an updated key. A newly inserted key is also placed after `head`. If insertion exceeds capacity, the node immediately before `tail` is removed from both the linked list and dictionary.

## Complexity

| Operation | Average time | Extra space |
| --- | --- | --- |
| `get(key)` | O(1) | O(1) |
| `put(key, value)` | O(1) | O(1) per stored entry |
| Whole cache | — | O(capacity) |

Python dictionaries provide O(1) **average** lookup/insertion/deletion. Linked-list moves and eviction are O(1).

## Project structure

```text
lru-cache-assignment/
├── src/
│   ├── lru_cache.py
│   └── demo.py
├── tests/
│   └── test_lru_cache.py
├── .gitignore
└── README.md
```

## Run the required example

Python 3.9+ is sufficient; there are no third-party dependencies.

From the project root:

```bash
python src/demo.py
```

The terminal output shows every `put()`, every `get()` and returned value, the MRU→LRU order, and the real eviction of `B` when `C` is inserted.

## Run all tests

```bash
python -m unittest discover -s tests -v
```

The test suite covers normal operations, missing keys, updates, capacity 1, repeated gets, repeated puts, eviction, capacity validation, and recency ordering.

## Output screenshot for submission

Run:

```bash
python src/demo.py
```

Take one clear screenshot of the terminal from the heading through the final `get('A') -> 10`. This is real program output and visibly demonstrates the required put/get operations, returned values, and LRU eviction.

## Assignment example

```text
Cache(2)
put("A", 10)
put("B", 20)
get("A") -> 10
put("C", 30)   # evicts B
get("B") -> -1
get("C") -> 30
get("A") -> 10
```

## Vercel

Vercel deployment is **not required** for this assignment. The submission asks for a GitHub repository and an output screenshot, and this is a CLI/data-structure project with no web-server requirement. Adding a web UI would introduce unnecessary functionality beyond the task.
