import numpy as np
keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
 
cipherMatrix = [[0] for i in range(3)]
def keyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j]= 0
            k+=1
def encrypt(messageVector):
    for i in range(3):
        for j in range(3):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x]*messageVector[x][j])
            cipherMatrix[i][j]