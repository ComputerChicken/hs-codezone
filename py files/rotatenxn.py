nextVal = ""
matrix = []
while nextVal != "stop":
    nextVal = input()
    matrix.append(nextVal.split(","))
matrix = matrix[:-1]

blankMatrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        blankMatrix[y][x] = matrix[-x-1][y]

for x in range(len(blankMatrix)):
    print(",".join(blankMatrix[x]))