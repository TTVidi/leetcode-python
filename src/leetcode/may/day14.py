# Implement Trie (Prefix Tree)

# Implement a trie with insert, search, and startsWith methods.
import functools


class Trie:

    def __init__(self):
        self.first = {'0': None}

    def insert(self, word: str) -> None:
        functools.reduce(lambda n, c: n.setdefault(c, {}), word, self.first)['0'] = 0

    def search(self, word: str) -> bool:
        return self.startsWith(word) and '0' in functools.reduce(lambda n, c: n[c], word, self.first)

    def startsWith(self, prefix: str) -> bool:
        return functools.reduce(lambda n, c: n.get(c, {}), prefix, self.first)
