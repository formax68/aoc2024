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
    for rule in rules:
        for page in update:
            index = update.index(page)
            if page == rule[1] and rule[0] in update[index:]:
                print("Moving {page} because of {rule}")

correct_updates = []
for update in updates:
   if check_updates(update):
        correct_updates.append(update)

result = sum_middle_pages(correct_updates)

# print(correct_updates)
print(result)

