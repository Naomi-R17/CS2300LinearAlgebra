'''
Name: Naomi Rodriguez
Date: September 21st, 2023
    Part 4

'''
import numpy as np


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

    # if they can be added
    if len(matrixOne) == len(matrixTwo):
        addOutput = np.add(matrixOne, matrixTwo)
        addOutput = addOutput.astype(int)  # Convert to integers

        # Create and write to a file
        f = open("nrodriguez_p4_outA12.txt", "w")
        for row in addOutput:
            formatted_row = ' '.join(map(str, row))
            print(formatted_row)
            f.write(formatted_row + '\n')
        f.close()
    else:
        print("Matrices cannot be added!")

    # if they can be multiplied
    if len(matrixOne[0]) == len(matrixTwo):
        mulOutput = np.matmul(matrixOne, matrixTwo)
        mulOutput = mulOutput.astype(int)   # Convert to integers

        # Create and write to a file
        f = open("nrodriguez_p4_outM34.txt", "w")
        for row in mulOutput:
            formatted_row = ' '.join(map(str, row))
            print(formatted_row)
            f.write(formatted_row + '\n')
        f.close()
    else:
        print("Matrices cannot be multiplied!")


except FileNotFoundError:
    print('File was not found')

except ValueError:
    print('Error')

