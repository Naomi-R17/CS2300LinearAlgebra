'''
Name: Naomi Rodriguez
Date: September 22nd, 2023
    Part 5

'''

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
    vectorOne = vectorDict[inputOne]
    vectorTwo = vectorDict[inputTwo]

    if len(vectorOne) == len(vectorTwo):
        for i in range(len(vectorOne)):
            result += vectorOne[i] * vectorTwo[i]
        print(result)

    f = open("nrodriguez_p5_out" + inputOne + inputTwo + ".txt", "w")
    f.write(str(result))
    f.close()

else:
    print("This is not an acceptable vector!")

