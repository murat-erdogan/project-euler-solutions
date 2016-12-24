f = open("p011_matrix.txt", "r")
strg = f.read()
nums = strg.split()
x = 0
y = 0
matrix = {}
k = 0
for i in range(23):
    for j in range(23):
        if i > 19 or j > 19:
            matrix[i, j] = 0
        else:
            matrix[i, j] = nums[k]
            k += 1

max = 0
for i in range(19):
    for j in range(19):
        local_max = 0
        right = 0
        down = 0
        diagonal = 0
        ldiagonal = 0
        right = int(matrix[i, j]) * int(matrix[i, j+1]) * int(matrix[i, j+2]) * int(matrix[i, j+3])
        down = int(matrix[i, j]) * int(matrix[i+1, j]) * int(matrix[i+2, j]) * int(matrix[i+3, j])
        diagonal = int(matrix[i, j]) * int(matrix[i+1, j+1]) * int(matrix[i+2, j+2]) * int(matrix[i+3, j+3])
        if j > 2:
            ldiagonal = int(matrix[i, j]) * int(matrix[i+1, j-1]) * int(matrix[i+2, j-2]) * int(matrix[i+3, j-3])
        else:
            ldiagonal = 0
        if right > down and right > diagonal > ldiagonal:
            local_max = right
        elif down > right and down > diagonal > ldiagonal:
            local_max = down
        elif diagonal > right and diagonal > down > ldiagonal:
            local_max = diagonal
        elif ldiagonal > right and ldiagonal > down > diagonal:
            local_max = ldiagonal
        if local_max > max:
            max = local_max
print(max)