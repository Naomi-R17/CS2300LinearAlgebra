'''
Name: Naomi Rodriguez
Date: September 22nd, 2023
    Part 6

'''

print('Please enter the matrix text file: ')
userOne = input()
matOne = 'nrodriguez_' + userOne + '.txt'

with open(matOne, "r") as matrixOneFile:
    matrixOne = [list(map(float, line.split())) for line in matrixOneFile]

transposeMatrix = []

# the number of items in the first row of the list
for i in range(len(matrixOne[0])):
    row = []    # empty list
    for number in matrixOne:
        row.append(int(number[i]))  # append the number to this list
    transposeMatrix.append(row)     # append list to matrix

# print and print to file
f = open("nrodriguez_p6_mat4.txt", "w")
for row in transposeMatrix:
    formatted_row = ' '.join(map(str, row))
    print(formatted_row)
    f.write(formatted_row + '\n')
f.close()