import csv

# Writing to CSV
with open("second.csv", 'a', newline="") as f:
    wo = csv.writer(f)
    data = [
        ['a', 'b', 'c', 'd', 'e'],
        [16, 16, 45, 24, 134, 14, 41, 414, 1414, 141],
        [34, 234, 243, 2342, 3434, 234, 234, 23]
    ]
    wo.writerows(data)

# Reading from CSV
with open("second.csv", 'r') as file:
    re = csv.reader(file)
    for row in re:
        print(len(row))

