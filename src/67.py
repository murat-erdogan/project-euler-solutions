# I used bottom-up approach and calculated values only once.
# same solution applies to p18 as well. just set the rows value to 15.
rows = 100
f = open("p067_triangle.txt", "r")
strng = f.read()
matrix = {}
temp_matrix = {}
nums = strng.split()
k = 0
for i in range(rows):
    for j in range(i+1):
        matrix[i, j] = nums[k]
        temp_matrix[i, j] = 0
        k += 1

for i in range(rows-1, -1, -1):
    for j in range(i+1):
        if i == rows-1:
            temp_matrix[i, j] = matrix[i, j]
        else:
            a = int(matrix[i, j]) + int(temp_matrix[i+1, j])
            b = int(matrix[i, j]) + int(temp_matrix[i+1, j+1])
            if a >= b:
                temp_matrix[i, j] = a
            else:
                temp_matrix[i, j] = b

print(temp_matrix[0, 0])
