import unittest

class sjTest(unittest.TestCase):
    def setUp(self):
        self.sj = StringJudge()

    def test_naughty_is_not_nice(self):
        self.assertFalse(self.sj.is_naughty('ugknbfddgicrmopn'))

    def test_sj_case1(self):
        self.assertTrue(self.sj.is_nice('ugknbfddgicrmopn'))
    
    def test_sj_case2(self):
        self.assertTrue(self.sj.is_nice('aaa'))

    def test_sj_missingdouble(self):
        self.assertTrue(self.sj.is_naughty('jchzalrnumimnmhp'))

    def test_sj_missingxy(self):
        self.assertTrue(self.sj.is_naughty('haegwjzuvuyypxyu'))

    def test_sj_missing3vowels(self):
        self.assertTrue(self.sj.is_naughty('dvszwmarrgswjxmb'))

class sj2Test(unittest.TestCase):
    def setUp(self):
        self.sj2 = StringJudge2()
    
    def test_sj2_case1(self):
        self.assertTrue(self.sj2.is_nice('qjhvhtzxzqqjkmpb'))
    def test_sj2_case2(self):
        self.assertTrue(self.sj2.is_nice('xxyxx'))
    def test_sj2_case3(self):
        self.assertTrue(self.sj2.is_naughty('uurcxstgmygtbstg'))
    def test_sj2_case4(self):
        self.assertTrue(self.sj2.is_naughty('ieodomkazucvgmuy'))



class StringJudge:
    def is_naughty(self, perp: str) -> bool:
        return not self.is_nice(perp)

    def is_nice(self, perp: str) -> bool:
        perp = perp.rstrip()
        banned_substrings = ['ab', 'cd', 'pq', 'xy']
        for substring in banned_substrings:
            if substring in perp:
                return False
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_count = 0
        for c in perp:
            if c in vowels:
                vowel_count += 1
        if vowel_count < 3:
            return False
        for p in range(1,len(perp)):
            if perp[p] == perp[p-1]:
                return True
        return False

class StringJudge2(StringJudge):
    def is_nice(self, perp: str) -> bool:
        repeating_substring = False
        repeating_with_between = False
        for p in range(2,len(perp)-1):
            if perp[p-2] == perp[p-1]:
                next
            if perp[p-2:p] in perp[p:]:
                repeating_substring = True
                break

        for p in range(2,len(perp)):
            if perp[p] == perp[p-2]:
                repeating_with_between = True
                break
        return repeating_with_between and repeating_substring
       
        
#unittest.main()

sj = StringJudge()
sj2 = StringJudge2()


nice_count_1 = 0
nice_count_2 = 0
with open("AdventOfCode/2015/5/input.txt", "r") as f:
    for line in f:
        if sj.is_nice(line):
            nice_count_1 += 1
        if sj2.is_nice(line):
            nice_count_2 += 1

print(f"part1: {nice_count_1}")
print(f"part2: {nice_count_2}")