updates_file = "updates.txt"
rules_file = "rules.txt"
rules = []
updates = []

with open(rules_file, 'r') as file:
    for rule in file:
        rule = rule.strip()
        rules.append([int(x) for x in rule.split("|")])

with open(updates_file, 'r') as file:
    for update in file:
        update = update.strip()
        updates.append([int(x) for x in update.split(',')])

rules_dict = {}

def parse_rule(rule):
    if rule[0] not in rules_dict:
        rules_dict[rule[0]] = {"after":[],"before":[]}
    if rule[1] not in rules_dict:
        rules_dict[rule[1]] = {"after":[],"before":[]}
    rules_dict[rule[0]]["before"].append(rule[1])
    rules_dict[rule[1]]["after"].append(rule[0])

def check_updates(update):
    for rule in rules:
        if all(r in update for r in rule):
            if update.index(rule[1]) < update.index(rule[0]):
                return False
    return True

def sum_middle_pages(updates):
    result = 0
    for update in updates:
        result += update[(len(update)// 2 )]
    return result


def fix_update(update):
    # print(update)
    fixed_update = []
    while len(update) > 0:
        for page in update:
            if not set(rules_dict[page]["after"]).intersection(update):
                fixed_update.append(page)
                update.remove(page)
    # print(fixed_update)
    return fixed_update

# correct_updates = []
# for update in updates:
#    if check_updates(update):
#         correct_updates.append(update)

for rule in rules:
    parse_rule(rule)

fixed_updates = []
for update in updates:
    if not check_updates(update):
        fixed_updates.append(fix_update(update))
print(sum_middle_pages(fixed_updates))

# print(correct_updates)

