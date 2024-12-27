input_file = "input.txt"

list1 = []
list2 = []

with open(input_file, 'r') as file:
    for line in file:
        parts = line.split()
        if len(parts) == 2:
            list1.append(int(parts[0]))
            list2.append(int(parts[1]))

# print(list1)
# print(list2)

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# print(sorted_list1)
# print(sorted_list1[0])

distance = 0
i = 0

while i < len(sorted_list1):
    # print("i = ", i)
    # print("list1 = ", sorted_list1[1])
    distance += abs(sorted_list1[i] - sorted_list2[i])
    i += 1

print("distance is ",distance)

similarity = 0

for location in sorted_list1:
    similarity += sorted_list2.count(location) * location

print(similarity)

