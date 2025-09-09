def getRow(rowIndex):
    row = [1] * (rowIndex + 1)
    for i in range(2, rowIndex + 1):
        for j in range(i - 1, 0, -1):  # update backwards
            row[j] += row[j - 1]
    return row
#in
rowIndex = int(input("Enter row index (0-indexed): "))
print("Pascal's Triangle Row:", getRow(rowIndex))
