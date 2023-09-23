'''
Name: Naomi Rodriguez
Date: September 22nd, 2023
    Part 7

'''
import numpy as np

# Dot product

# 'menu selection'
vectorDict = {'r': [-1, -2],
                's': [-3, 3],
                'u': [2, -1],
                'v': [3, 1],
                'w': [1, 3]}

result = 0

print('Please enter a vector: ')
inputOne = input()
print('Please enter a second vector: ')
inputTwo = input()

if inputOne and inputTwo in vectorDict:
    vectorOne = np.array(vectorDict[inputOne])
    vectorTwo = np.array(vectorDict[inputTwo])

    result = np.dot(vectorOne, vectorTwo)

    print(result)
    f = open("nrodriguez_p7_outD" + inputOne + inputTwo + ".txt", "w")
    f.write(str(result))
    f.close()

else:
    print("This is not an acceptable vector!")

# Transpose
print('Please enter the matrix text file: ')
userMatrix = input()
matOne = 'nrodriguez_' + userMatrix + '.txt'

with open(matOne, "r") as matrixOneFile:
    matrixOne = np.array([list(map(float, line.split())) for line in matrixOneFile])

matrixOne = matrixOne.astype(int)
transposed_matrix = matrixOne.transpose()

f = open("nrodriguez_p7_outT" + userMatrix + ".txt", "w")
for row in transposed_matrix:
    formatted_row = ' '.join(map(str, row))
    print(formatted_row)
    f.write(formatted_row + '\n')
f.close()
