import sys

sys.path.append("AdventOfCode/lib")
import adventutil

fetcher = adventutil.InputFetcher('2022', '11')
input = fetcher.fetch(rstrip=True, commasplit=False, small=True)


class Monkey:
    def __init__(self, id, items, operation, divisible, true_target, false_target):
        self.id = id
        self.items = items
        self.operation = operation
        self.divisible = divisible
        self.true_target = true_target
        self.false_target = false_target
        self.inspection_count = 0

    def inspect(self):
        print(f"Monkey {self.id}:")
        self.inspection_count += len(self.items)
        for item in self.items:
            print(f"\tMonkey inspects an item with a worry level of {item}")
            new_worry = self.op(item)
            print(f"\t\tWorry level is increased to {new_worry}")
            new_worry //= 3
            print(f"\t\tMonkey gets bored with item. Worry level is divided by 3 to {new_worry}")
            if(new_worry % self.divisible == 0):
                print(f"\t\tCurrent worry level is divisible by {self.divisible}")
                target = self.true_target
            else:
                print(f"\t\tCurrent worry level is not divisible by {self.divisible}")
                target = self.false_target
            print(f"\t\tItem with worry level {new_worry} is thrown to monkey {target}")
            monkeys[target].catch(new_worry)
        self.items=[]


    def op(self, item):
        if self.operation[4].isnumeric():
            operand = int(self.operation[4])
        else:
            operand = item
        if self.operation[3] == "*":
            return item * operand
        else:
            return item + operand

    def catch(self, item):
        self.items.append(item)

part1=0
part2=0
global monkeys
monkeys = []
input = [ e for e in input if e != ""]
monkey_count = len(input) // 6

for monkey_id in range(monkey_count):
    starting_items=input[monkey_id*6+1].replace(",", "").split()[2:]
    starting_items = [ int(e) for e in starting_items ]
    operation = input[monkey_id*6+2].split()[1:]
    divisible = int(input[monkey_id*6+3].split()[3])
    true_target = int(input[monkey_id*6+4].split()[5])
    false_target = int(input[monkey_id*6+5].split()[5])
    #starting_items = input[monkey_id*6+1].split
    monkeys.append(Monkey(monkey_id, starting_items, operation, divisible, true_target, false_target))

for round in range(20):
    for monkey_id in range(monkey_count):
        monkeys[monkey_id].inspect()

    for monkey_id in range(monkey_count):
        print(f"Monkey {monkey_id}: {monkeys[monkey_id].items}")

ic = []
for monkey_id in range(monkey_count):
    ic.append(monkeys[monkey_id].inspection_count)
    print(f"Monkey {monkey_id} inspected items : {monkeys[monkey_id].inspection_count}")
ic.sort(reverse=True)
part1 = ic[0] * ic[1]
print("part1:", part1)
print("part2:", part2)
