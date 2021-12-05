import unittest
import hashlib

class solutionTest(unittest.TestCase):
    def setUp(self):
        self.hasher = Hasher()

    def test_part1_case1(self):
        self.assertEqual(609043, self.hasher.mine('abcdef'))
    
    def test_part1_case2(self):
        self.assertEqual(1048970, self.hasher.mine('pqrstuv'))
    

class Hasher:
    def __init__(self):
        pass

    def mine(self, prefix: str, zeroes=5):
        n = 0
        hash = ""
        while not hash.startswith("0" * zeroes):
            hash = hashlib.md5(f"{prefix}{n}".encode("utf-8")).hexdigest()
            n += 1
        return(n-1)

    
        
#unittest.main()

h = Hasher()
part1 = h.mine("ckczppom")
part2 = h.mine("ckczppom", 6)

print(f"part1: {part1}")
print(f"part2: {part2}")