'''
Name: Naomi Rodriguez
Date: October 17th, 2023
Description: Reads a message from a text file, encrypt it using the Hill Cipher method
            This portion decrypts the message
'''
import numpy

# Matrix A
A = [[1, -1, -1, 1],
     [2, -3, -5, 4],
     [-2, -1, -2, 2],
     [3, -3, -1, 2]]
matrixA = numpy.array(A)
inverseA = numpy.linalg.inv(matrixA)
# to round then delete the decimal point from each number
roundedInverse = numpy.round(inverseA)
roundedInverseA = inverseA.astype(int)

print(roundedInverseA)
rows = 4

f = open("C-matrix", "r")

# list of each character in the file
text = f.readline()
# -89 15 -6  ... -218 -39 35 156

number = text.split()
numberList = [int(x) for x in number]

# If the number of elements in B is not a multiple of 4, add 0s to the list until it is
while len(numberList) % rows != 0:
    numberList.append(0)

# Start at the first element, each list being a column of 4 elements
matrixC = [numberList[element: element + rows] for element in range(0, len(numberList), rows)]
matrixC = numpy.array(matrixC)
transposeC = matrixC.transpose()
print("The following is matrix C:")
print(transposeC)
# matrix C from part A

C = numpy.dot(roundedInverseA, transposeC)
print()
print(C)
# back to matrix B

decodedMessage = ''
cWidth = len(C)
cLength = len(C[0])

for col in range(cLength):
    for row in range(cWidth):
        number = C[row][col]
        # Stop appending if a null character is encountered
        if number == 0:
            break
        decodedMessage += chr(number)

print("The decoded message is:", decodedMessage)
# The decoded message is: The password is: NCS-2014

