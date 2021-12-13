import sys
import re

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2015', '15')
input = fetcher.fetch(rstrip=True, commasplit=False, small=False)

def compositions(s=2,t=2):
    q = [0] * t
    r = None
    q[0] = s
    while True:
        yield q
        if q[0] == 0:
            if r == (t-1):
                break
            else:
                q[0] = q[r] - 1
                q[r] = 0
                r = r + 1
        else:
            q[0] = q[0] - 1
            r = 1
        q[r] = q[r] + 1


def score(ingredients, ratios):
    ret = 1
    calories = 0
    for attribute in range(5):
        if attribute == 4:
            calories += sum([ ingredients[i][attribute] * ratios[i] for i in range(len(ingredients)) ])
        else:
            attribute_score = sum([ ingredients[i][attribute] * ratios[i] for i in range(len(ingredients)) ])
            if attribute_score < 0:
                attribute_score = 0
            ret *= attribute_score
    return (ret, calories)
            

pat = re.compile(r"\w+: \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+)")
ingredients = []
for line in input:
    m = re.match(pat, line)
    ingredient = list(m.group(1,2,3,4,5))
    ingredient = [ int(n) for n in ingredient ]
    ingredients.append(ingredient)

best_score = 0
recipes_500 = []
for c in compositions(100,len(ingredients)):
    s, calories = score(ingredients, c)
    best_score = max(s, best_score)
    if calories == 500:
        recipes_500.append(s) 
    
recipes_500.sort(reverse=True)
print("part 1", best_score)
print("part 2", recipes_500[0])