'''
        Programming Assignment 2: Cryptography

Name: Naomi Rodriguez
Date: October 15th, 2023
Description: Reads a message from a text file, encrypt it using the Hill Cipher method
            This portion encrypts a message.

Question 1: We need to multiply A and B, so they need to have at least one edge in common,
            so a 4x4 matrix has to bu multiplied by a 4xm or a nx4 matrix!
'''

import numpy

# Matrix A
A = [[1, -1, -1, 1],
     [2, -3, -5, 4],
     [-2, -1, -2, 2],
     [3, -3, -1, 2]]
matrixA = numpy.array(A)
transposeA = matrixA.transpose()

B = []
C = []
matrixC = []
baseHex = 16
rows = 4

# read from a file
f = open("input-A21.txt", "r")

# list of each character in the file
text = [i for message in f for i in message]

# to get rid of the last element in the file, which is a newline char
plaintext = text[0:-1]

for letter in plaintext:
    # ord() converts the letter into its ASCII value, then we have to turn that into hexadecimal
    hexUnicode = hex(ord(letter))
    # digit at the hundreds place, multiply it by 16
    result = int(hexUnicode[2]) * baseHex
    # make sure digit at the tens place is in uppercase; int(value, base)
    tensPlace = int(hexUnicode[3].upper(), baseHex)
    asciiValue = result + tensPlace
    B.append(asciiValue)

# If the number of elements in B is not a multiple of 4, add 0s to the list until it is
while len(B) % rows != 0:
    B.append(0)

# Start at the first element, and add the 4th element in B to a list, each list being a column of 4 elements
matrixB = [B[element: element + rows] for element in range(0, len(B), rows)]

# numpy to transpose matrixB
matrixB = numpy.array(matrixB)
transposeB = matrixB.transpose()
print("The following is matrix B:")
print(transposeB)

# C = AB
C = numpy.matmul(matrixA, transposeB)
print()
print("The following is matrix C:")
print(C)











