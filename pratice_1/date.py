class Bag():

    def __init__(self):
        self._items = list()
        self._curr = -1

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        assert item in self._items, 'This item must be in the bag'
        i = self._items.index(item)
        self._items.pop(i)

    def __iter__(self):
        return self

    def __next__(self):
        self._curr += 1
        if self._curr < len(self._items):
            return self._items[self._curr]
        else:
            raise StopIteration
    def __getitem__(self, i):
        if i >= len(self._items):
            raise IndexError('out if index')
        else:
            return self._items[i]

from array import Array