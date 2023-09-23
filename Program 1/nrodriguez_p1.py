'''
Name: Naomi Rodriguez
Date: September 19th, 2023
    Part 1

I have not written to a file in python before, so I used the following link as reference:
https://www.w3schools.com/python/python_file_write.asp
'''

# PART A: ALGEBRA OF MATRICES

# Part 1
Naomi = 5
Rodriguez = 9

# Matrix 1
rows = Rodriguez
cols = Naomi
# First value that will be at the [0,0] position
current = 1

# fills list with 0s, 2d matrix of 9x5
matrixOne = [[0 for i in range(cols)] for j in range(rows)]

# Columns first (inner loop), then rows (outer loop)
print('Matrix One:')
for r in range(rows):
    for c in range(cols):
        # Matrix{row][column] = 1, adding one each time
        matrixOne[r][c] = current
        current += 1

# Create and write to a file
f = open("nrodriguez_mat1.txt", "w")
for rows in matrixOne:
    print(rows)

    # In order to format the 2d array correctly, need to join with whitespace and a new line
    f.write(" ".join(map(str, rows)) + '\n')
f.close()


# Matrix 2
# All matrices are very similar, just switching the starting point,
# whether we increment between row or col first, and incrementation.
rows = Rodriguez
cols = Naomi
current = 2

matrixTwo = [[0 for i in range(cols)] for j in range(rows)]

print('\n')
print('Matrix Two:')
# Rows first (inner loop), then columns (outer loop)
for c in range(cols):
    for r in range(rows):
        matrixTwo[r][c] = current
        current += 3

f = open("nrodriguez_mat2.txt", "w")
for rows in matrixTwo:
    print(rows)
    f.write(" ".join(map(str, rows)) + '\n')
f.close()


# Matrix 3
rows = 2
cols = 4
current = 10

matrixThree = [[0 for i in range(cols)] for j in range(rows)]

print('\n')
print('Matrix Three:')
# Columns first (inner loop), then rows (outer loop)
for r in range(rows):
    for c in range(cols):
        matrixThree[r][c] = current
        current += (-2)

f = open("nrodriguez_mat3.txt", "w")
for rows in matrixThree:
    print(rows)
    f.write(" ".join(map(str, rows)) + '\n')
f.close()

# Matrix 4
rows = 4
cols = 2
current = -6

matrixFour = [[0 for i in range(cols)] for j in range(rows)]

print('\n')
print('Matrix Four:')
# Rows first (inner loop), then columns (outer loop)
for c in range(cols):
    for r in range(rows):
        matrixFour[r][c] = current
        current += 1.5

f = open("nrodriguez_mat4.txt", "w")
for rows in matrixFour:
    print(rows)
    f.write(" ".join(map(str, rows)) + '\n')
f.close()