with open('day') as f: txt = f.read()

# Make the mischief
def generate_monkeys():
    monkeys = []
    for monkey_txt in txt.split('\n\n'):
        monkey = monkey_txt.splitlines()
        monkeys.append({
            'items': [int(item) for item in monkey[1][len('  Starting items: '):].split(',')],
            'operation': monkey[2][len('  Operation: new = '):],
            'test': int(monkey[3][len('  Test: divisible by '):]),
            'if_true': int(monkey[4][len('    If true: throw to monkey '):]),
            'if_false': int(monkey[5][len('    If false: throw to monkey '):]),
            'inspections': 0
        })
    return monkeys


# Monkeys make a mockery out of mere mortals
def do_monkey_things(monkeys, hakkunamatata):
    for monkey in monkeys:
        items = monkey['items']
        op = monkey['operation'].split(' ')
        
        for item in items:
            delta = item if op[2] == 'old' else int(op[2])
            worry = (item + delta) if op[1] == '+' else (item * delta)
            # There's definitely better ways to do this
            worry = hakkunamatata(worry)
            
            throw_to_monkey = monkey['if_true'] if not worry % monkey['test'] else monkey['if_false']
            monkeys[throw_to_monkey]['items'].append(worry)
            monkey['inspections'] += 1
            
        monkey['items'] = []


def run_rounds(num, monkeys, hakkunamatata):
    for i in range(num):
        do_monkey_things(monkeys, hakkunamatata)
    
    active_monkeys = sorted(monkeys, key=lambda x:x['inspections'], reverse=True)
    print(active_monkeys[0]['inspections'] * active_monkeys[1]['inspections'])
    
    
#Part 1
run_rounds(20, generate_monkeys(), lambda x: x // 3)

#Part 2
monkeys = generate_monkeys()
# I could have used math.prod() here,
# but I'm trying to avoid using additional libraries if I can help it.
monkey_no_like_big_number = 1 # Needed for Part 2
for test in [monkey['test'] for monkey in monkeys]:
    monkey_no_like_big_number *= test
        
run_rounds(10000, monkeys, lambda x: x % monkey_no_like_big_number)
