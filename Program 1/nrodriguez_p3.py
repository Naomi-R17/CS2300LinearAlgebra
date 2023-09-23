'''
Name: Naomi Rodriguez
Date: September 19th, 2023
    Part 3

'''
outputMatrix = []

# Majority of this code is the same as Part 2, just changed the if statement
print('Please enter the your first matrix text file: ')
userOne = input()
matOne = 'nrodriguez_' + userOne + '.txt'

print('Please enter the your second matrix text file: ')
userTwo = input()
matTwo = 'nrodriguez_' + userTwo + '.txt'

try:
    # first read the file and add values into an empty list
    # only change was from int to float to accommodate mat4
    with open(matOne, "r") as matrixOneFile:
        matrixOne = [list(map(float, line.split())) for line in matrixOneFile]

    with open(matTwo, "r") as matrixTwoFile:
        matrixTwo = [list(map(float, line.split())) for line in matrixTwoFile]

    # if the number of items in the first row of the first matrix is equal to the number of items in the second matrix
    # if # of cols in matrixOne == rows in matrixTwo
    if len(matrixOne[0]) == len(matrixTwo):
        # # of rows and columns of new output matrix
        rows = len(matrixOne)
        cols = len(matrixTwo[0])
        outputMatrix = [[0 for i in range(cols)] for j in range(rows)]

        # Multiplication
        for i in range(rows):
            for j in range(cols):
                # needed to convert output from float to int
                number = 0.0
                # loops through the items in matrixTwo
                for k in range(len(matrixTwo)):
                    # item at row i, col k * row k at col j
                    number += int(matrixOne[i][k] * matrixTwo[k][j])
                outputMatrix[i][j] = int(number)
    else:
        print("Matrices cannot be multiplied!")

    # Create and write to a file
    f = open("nrodriguez_p3_out34.txt", "w")
    for row in outputMatrix:
        formatted_row = ' '.join(map(str, row))
        print(formatted_row)
        f.write(formatted_row + '\n')
    f.close()


except FileNotFoundError:
    print('File was not found')

except ValueError:
    print('Error')

