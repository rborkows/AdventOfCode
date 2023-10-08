class Judge1():
    def __init__(self) -> None:
        self.subject = ""

    def is_nice(self, string):
        self.subject = string
        return self._has_three_vowels() and self._has_double_letter() and self._no_disallowed_combos()

    def _has_three_vowels(self):
        vowels = set("aeiou")
        vowel_count = 0
        for c in self.subject:
            if c in vowels:
                vowel_count += 1
        return vowel_count >= 3
    
    def _has_double_letter(self):
        for i in range(1,len(self.subject)):
            if self.subject[i] == self.subject[i-1]:
                return True
        return False
    
    def _no_disallowed_combos(self):
        disallowed_combos = ['ab', 'cd', 'pq', 'xy']
        for disallowed_combo in disallowed_combos:
            if disallowed_combo in self.subject:
                return False
        return True
    
class Judge2():
    def __init__(self) -> None:
        self.subject = ""

    def is_nice(self, string):
        self.subject = string
        return self._has_double_letter() and self._has_repeat_letter()
    
    def _has_double_letter(self):
        for i in range(2,len(self.subject)-1):
            if self.subject[i-1] == self.subject[i-2]:
                next
            if self.subject[i-2:i] in self.subject[i:]:
                return True
        return False
    
    def _has_repeat_letter(self):
        for i in range(2,len(self.subject)):
            if self.subject[i] == self.subject[i-2]:
                return True
        return False

        
judge1 = Judge1()
judge2 = Judge2()
#test_cases = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
#test_cases = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]
#for test_case in test_cases:
#    print(test_case, judge2.is_nice(test_case))

part1 = 0
part2 = 0
with open("AdventOfCode/2015/5/input","r") as f:
    for line in f.readlines():
        line = line.rstrip()
        if judge1.is_nice(line):
            part1 += 1
        if judge2.is_nice(line):
            part2 += 1

print("part1 =", part1)
print("part2 =", part2)