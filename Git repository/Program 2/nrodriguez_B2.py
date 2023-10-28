'''
Name: Naomi Rodriguez
Date: October 26th, 2023
Description: Gauss-Jordan Traffic Flow
'''

import numpy

print('Please input four different flows into the roundabout')
print('Output Flow 1:')
flow1 = float(input())
print('Input Flow 2:')
flow2 = float(input())
print('Output Flow 3:')
flow3 = float(input())
print('Input Flow 4:')
flow4 = float(input())

# Part B2.1, augmented matrix
augMatrix = numpy.array(
    [[1, 1, 0, 0, flow1],
            [1, 0, 0, 1, flow2],
            [0, 1, 1, 0, flow3],
            [0, 0, 1, 1, flow4]], dtype=float)

print('Augmented Matrix:')
numpy.set_printoptions(precision=2, suppress=True)
print(augMatrix)

# Part B2.2 Reduced Row echelon form
rrefMatrix = augMatrix.shape[0]

for number in range(rrefMatrix):
    pivot = number

    while pivot < rrefMatrix and augMatrix[pivot, number] == 0:
        pivot += 1

    if pivot == rrefMatrix:
        continue

    # swapping row with pivot
    augMatrix[number], augMatrix[pivot] = augMatrix[pivot].copy(), augMatrix[number].copy()

    # Normalize
    augMatrix[number] //= augMatrix[number, number]

    for j in range(rrefMatrix):
        if j != number:
            augMatrix[j] -= augMatrix[j, number] * augMatrix[number]


print('rref form:')
print(augMatrix)

