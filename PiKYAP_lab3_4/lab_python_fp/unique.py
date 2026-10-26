
class Stop: pass

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.bilo = set()
        pass

    def __next__(self):
        while True:
            item = next(self.items, Stop)
            if item is Stop:
                raise StopIteration

            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in self.bilo:
                self.bilo.add(key)
                return item

    def __iter__(self):
        return self

if __name__ == '__main__':
    import gen_random
    print(list(Unique([1, 1, 1, 1, 1, 2, 2, 2, 2, 2])))
    print(list(Unique(gen_random.gen_random(10, 1, 3))))
    print(list(Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'])))
    print(list(Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'], ignore_case=True)))
