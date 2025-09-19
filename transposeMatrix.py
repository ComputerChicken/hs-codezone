matrix = [input().split(",") for i in range(3)]

blankMatrix = [[0 for i in range(3)] for i in range(3)]

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        blankMatrix[y][x] = matrix[-x-1][y]

for x in range(len(blankMatrix)):
    print(",".join(blankMatrix[x]))