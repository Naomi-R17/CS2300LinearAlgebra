'''
Name: Naomi Rodriguez
Date: November 26th, 2023
Description: Leontief Input-Output Model
    A small community includes a farmer, baker, and a grocer and has the input-ouput matrix D and external
    demand matrix E. This program will find the output matrix X. This program can handle any 3x3 matrix as
    D and any 3x1 matrix as E, read in as files.
'''
import numpy

# Identity Matrix
i = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
identityMatrix = numpy.array(i)

'''
FOR THESE TO GIVE THE SAME ANSWER, MUST CHANGE THE ROUNDED INVERSE TO DECIMAL = 2
# f = open("Example_D", "r")
# f2 = open("Example_E", "r")
'''

# reading in D and E matrices and formatting them
f = open("D_p3_part1", "r")
f2 = open("E_p3_part1", "r")

# list of each character in the file
text = f.read()
# 0.4 0.5 0.5
# 0.3 0.0 0.3
# 0.2 0.2 0.0

number = text.split('\n')
# ['0.4 0.5 0.5', '0.3 0.0 0.3', '0.2 0.2 0.0']
numberList = [[float(x) for x in line.split()] for line in number if line.strip()]
# [[0.4, 0.5, 0.5], [0.3, 0.0, 0.3], [0.2, 0.2, 0.0]]

matrixD = numpy.array([numberList[i:i+3] for i in range(0, len(numberList), 3)])
# [[0.4 0.5 0.5]
#  [0.3 0.  0.3]
#  [0.2 0.2 0. ]]

text2 = f2.readline()
number2 = text2.split()
numberList2 = [[int(x)] for x in number2]
matrixE = numpy.array(numberList2)

# 1) i - D
result1 = identityMatrix - matrixD
# [[ 0.6 -0.5 -0.5]
#  [-0.3  1.  -0.3]
#  [-0.2 -0.2  1. ]]

# 2) (i - D)^-1
inverseResult1 = numpy.linalg.inv(result1)
inverseRounded = numpy.round(inverseResult1, decimals=1)
# [[3.7 2.4 2.6]
#  [1.4 2.  1.3]
#  [1.  0.9 1.8]]

# 3) X = (i - D)^-1 * E
matrixX = numpy.dot(inverseRounded, matrixE)
print(matrixX)
# [[8700.]
#  [4700.]
#  [3700.]]
