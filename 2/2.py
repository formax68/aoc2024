input = "input.txt"

reports = []

with open(input, 'r') as file:
    for line in file:
        numbers = list(map(int, line.split()))
        reports.append(numbers)


def check_report_sorted(lst):
    if len(lst) < 2:
        return True
    if (lst == sorted(lst)) or (lst == sorted(lst, reverse= True)):
        if all(1 <= abs(lst[i] - lst[i-1]) <= 3 for i in range(1, len(lst))):
            return True


safe_reports = 0

for report in reports:
    if check_report_sorted(report):
        safe_reports += 1
    elif any(check_report_sorted(report[:i] + report[i+1:]) for i in range(0, len(report))):
        safe_reports += 1

print(safe_reports)
