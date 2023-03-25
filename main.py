class FlatIterator:

    def __init__(self, list_of_list):
        self.whole_list = []
        for list in list_of_list:
            self.whole_list += list
        self.finish = len(self.whole_list)

    def __iter__(self, n = 0):
        self.cursor = n - 1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.finish:
            raise StopIteration
        item = self.whole_list[self.cursor]
        return item

def test_1(list_of_lists):

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for item in FlatIterator(list_of_lists_1):
        print(item)

    test_1(list_of_lists_1)