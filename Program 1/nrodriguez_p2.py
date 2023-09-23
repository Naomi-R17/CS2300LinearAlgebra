'''
Name: Naomi Rodriguez
Date: September 19th, 2023
    Part 2

I have also never read text files in python so the following link was used as reference:
https://www.geeksforgeeks.org/how-to-open-a-file-using-the-with-statement/
'''
import sys

outputMatrix = []

# so user can just enter 'mat#', I'll add the rest of the file name
print('Please enter the your first matrix text file: ')
userOne = input()
matOne = 'nrodriguez_' + userOne + '.txt'

print('Please enter the your second matrix text file: ')
userTwo = input()
matTwo = 'nrodriguez_' + userTwo + '.txt'

# if the file was found, continue to add files, otherwise quit
try:
    # first read the file and add values into an empty list
    with open(matOne, "r") as matrixOne:
        # for line in matrixOne: iterating through matrix one
        # Need to split the line to get the individual values in the list
        # map needed to make each line an int
        matrixOne = [list(map(int, line.split())) for line in matrixOne]

    with open(matTwo, "r") as matrixTwo:
        matrixTwo = [list(map(int, line.split())) for line in matrixTwo]

    # Check whether the dimensions of each of the matrices are equal
    if len(matrixOne) == len(matrixTwo):

        for i in range(len(matrixOne)):
            # each row is its own list, adding to it number by number
            row = []
            # len(matrixOne[0]: how many items are in the first row of matrixOne
            for j in range(len(matrixOne[0])):
                row.append(matrixOne[i][j] + matrixTwo[i][j])
            outputMatrix.append(row)

        # Create and write to a file
        f = open("nrodriguez_p2_out12.txt", "w")
        for row in outputMatrix:
            formatted_row = ' '.join(map(str, row))
            print(formatted_row)
            f.write(formatted_row + '\n')
        f.close()
    else:
        print("Matrices are not equal and cannot be added.")
        sys.exit()


except FileNotFoundError:
    print('File was not found')

except ValueError:
    print('Error')
