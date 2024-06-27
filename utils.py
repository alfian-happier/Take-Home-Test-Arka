import unittest
def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicates(['a', 'b', 'a', 'c', 'b']), ['a', 'b', 'c'])
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
