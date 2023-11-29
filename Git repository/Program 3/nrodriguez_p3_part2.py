'''
Name: Naomi Rodriguez
Date: November 26th, 2023
Description: Least Squares Regression Analysis (Line of Best-Fit)

    A hardware retailer wants to know the demand for a rechargable power drill as a function of price.
    The ordered pairs (25, 82), (30, 75), (35, 67), and (40, 55). x represents price and y represents
    sales. Output includes the y = mx + b equation and a graph plotting the given data points and a
    straight line drawn for the linear equation y.
'''
import numpy, ast
import matplotlib.pyplot as plt

# f = open("Example_orderedPairs", "r")
f = open("orderedPairs_p3_part2", "r")
text = f.readlines()

points = [ast.literal_eval(s.strip()) for s in text]

matrixX = []
matrixY = []
xAdded = 0
xSquared = 0
xy = 0
yAdded = 0

for point in points:
    x, y = point
    xAdded += x
    xSquared += x**2
    xy += (x*y)
    yAdded += y

    matrixX.append([1, x])
    matrixY.append(y)

matrixX = numpy.array(matrixX)
# [[ 1 25]
#  [ 1 30]
#  [ 1 35]
#  [ 1 40]]
transposeX = numpy.transpose(matrixX)
# [[ 1  1  1  1]
#  [25 30 35 40]]

matrixY = numpy.array(matrixY)
matrixY = matrixY.reshape(-1, 1)
# [[82]
#  [75]
#  [67]
#  [55]]

# 1) X^T * X
result1 = numpy.dot(transposeX, matrixX)
# [[   4  130]
#  [ 130 4350]]
inverseResult1 = numpy.linalg.inv(result1)
inverseRounded = numpy.round(inverseResult1, decimals=1)
# [[ 8.7 -0.3]
#  [-0.3  0. ]]

# 2) X^T * Y
result2 = numpy.dot(transposeX, matrixY)
# [[ 279]
#  [8845]]

# finding m
elements = len(matrixY)

top = (elements * xy) - (xAdded * yAdded)
bottom = (elements * xSquared) - (xAdded**2)
m = top/bottom
# -1.78

# finding b
b = (yAdded - m * xAdded) / elements
# 127.6

# 3) m(X^T * X)^-1 * (X^T * Y)
scalarMultiplication = m * inverseRounded
scalarRounded = numpy.round(scalarMultiplication, decimals=1)
matrixA = numpy.dot(scalarRounded, result2)
matrixAFinal = numpy.array(matrixA)
# [[ 98. ]
#  [139.5]]

print('Linear equation:')
print('y = (' + str(b) + ') + (' + str(m) + ')x')

# Plotting points
plt.scatter(matrixX[:, 1], matrixY, label='Data Points')

xValues = numpy.linspace(min(matrixX[:, 1]), max(matrixX[:, 1]), 100)
yValues = m * xValues + b

plt.plot(xValues, yValues, color='red', label='Line of Best Fit')

plt.xlabel('Price')
plt.ylabel('Sales')
plt.title('Least Squares Regression Analysis')
plt.legend()

plt.show()
