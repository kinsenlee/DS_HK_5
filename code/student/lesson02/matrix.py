#import numpy as np 

m1 = [range(4),range(4,8),range(8,12)]

m2 = [range(1,4), range(2,5), range(3,6), range(4,7)]

v = [1,2,3,4]

i = 6

#matrix and vector mulitplication
def vectorMatrixMultiplication(matrix,vector):
    """
    Pre-requisite: 
    1. len(matrix[0]) = len(vector)
    2. all lists in matrix are of equal length 
    """
	#validate the arguments
    for n in range(len(matrix)):    	
    	if len(matrix[n]) <> len(vector):
    		print 'The matrix and vector are NOT valid for multiplication operation'
    		return
    	else:
    		0

    #determine dimension of the answer matrix, and create so as a zero matrix
    numOfRow = len(matrix)
    numOfColumn = len(matrix[0])

    answer = range(numOfRow)
    answer = [x*0 for x in answer]


    #calculate each element in the answer matrix		
    for n in range(len(answer)):
    		for col in range(numOfColumn):
    			answer[n] += matrix[n][col]*vector[col]

    return answer

#matrice multiplication
def matrixMultiplication (matrixA, matrixB):
	"""
	Pre-requisite
	1. len(matrixA[0]) = len(matrixB)
	2. matrixB is a vector, OR
		lists in matrixB are of same length AND list in matrixA are of same length   
	"""
	
	#validate matrixA and matrixB

	numOfRow = len(matrixA)
	numOfColumn = len(matrixB[0])

	answer = [[0 for col in range(numOfColumn)] for row in range(numOfRow)]

	for row in range(numOfRow):
		for col in range(numOfColumn):
			for n in range(4):
				answer[row][col] += matrixA[row][n] * matrixB[n][col]
	return answer

#create identify matrix
def identityMatrix(n):
	answer = [[0 for col in range(n)] for row in range(n)]

	for i in range(n):
		answer[i][i] = 1

	return answer

print 'matrix = ', m1
print 'vector = ', v
print 'matrix * vector = ', vectorMatrixMultiplication(m1,v)
print ''
print 'matrix1 = ', m1
print 'matrix2 = ', m2
print 'matrix1 * matrix 2 = ', matrixMultiplication(m1,m2)
print ''
print 'identity matrix with n = ', i, ':'
print identityMatrix(i)