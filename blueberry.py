#задача 24

row = [4, 5, 3, 5, 5, 7, 3, 5, 3]
max_result = 0
for index in range(0, len(row)):
    result = row[index-2] + row[index-1] + row[index]
    if result > max_result:
        max_result = result
print("Max: " + str(max_result))
