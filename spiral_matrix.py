results = []

counter = 1
start_col = start_row = 0
end_col = end_row = 2
for i in range(3):
    results.append([])

while start_col <= end_col and start_row <= end_row:
    for i in range(start_col, end_col+1):
        results[start_row][i] = counter
        counter += 1

    start_row += 1
    for i in range(start_row, end_row+1):
        results[i][end_col] = counter
        counter += 1

    end_col -= 1

    for i in range(end_col, start_col+1, -1):
        results[end_row][i] = counter
        counter += 1

    end_row -= 1

    for i in range(end_row, start_row+1, -1):
        results[i][start_col] = counter
        counter += 1

    start_col += 1

print(results)

