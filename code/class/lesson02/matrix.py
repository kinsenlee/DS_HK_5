import operator
import itertools

v = [5, 6, 7, 8]
m1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
m2 = [[1, 2], [3, 4], [5, 6], [7, 8]]

def matrix_vector_mult1(m, v):
    """
    basic function to multiply matrix with a vector
    prints each step for inspection.
    @param list m     matrix of m*n items
    @param list v     vector of n items
    """

    rows = len(m)
    w = [0]*rows

    print 'Result Vector Shape', w

    irange = range(len(v))

    print 'Irange,', irange

    sum = 0

    for j in range(rows):
        print 'iteration j ', j
        r = m[j]
        print 'row, ', r
        for i in irange:
            prod = r[i]*v[i]
            print r[i], '*', v[i], '=', prod
            sum += prod
        w[j],sum = sum,0
    return w

def dot(x, y):
    """
    dot product of a matrix row and a vector
    checks for equal length
    @param list x     matrix row n items
    @param list y     vector of n items
    """
    assert len(x) == len(y)
    return sum(itertools.starmap(operator.mul, itertools.izip(x, y)))

def matrix_vector_mult2(m, v):
    """
    advanced function to multiply a matrix with a vector
    @param list m     matrix of m*n items
    @param list v     vector of n items
    """
    return [dot(row, v) for row in m]


def matrix_mult1(a, b):
    """
    basic function to multiply two matrices
    @param list a     matrix of i*k items
    @param list b     matrix of k*j items
    """
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])

    assert cols_a == rows_b

    # create the result matrix
    # Dimensions would be rows_a x cols_b
    c = [[0 for row in range(cols_b)] for col in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                c[i][j] += a[i][k]*b[k][j]
    return c


def matrix_mult2(a,b):
    """
    advanced function to multiply two matrices
    @param list a     matrix of i*k items
    @param list b     matrix of k*j items
    """
    zip_b = zip(*b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]


def transpose_matrix1(matrix):
    """
    verbose function to transpose matrix
    @param list matrix     matrix to be transposed
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def transpose_matrix2(matrix):
    """
    concise function to transpose matrix
    @param list matrix     matrix to be transposed
    """
    return zip(*matrix)


def i_matrix(size):
    """
    @param int size     size of the matrix to generate
    """
    size = range(size)
    return [[ 1 if  x == y else 0 for x in size] for y in size]


def is_identity_matrix(matrix):
    """
    @param list matrix     matrix to be checked for identity
    """
    return all(val == (x == y)
        for y, row in enumerate(matrix)
            for x, val in enumerate(row))


# Commented version of the Matrix * Vector Multiplication

def matrix_vector_mult3(m, v):
    # Count the number of rows in the matrix     
    rows = len(m)
    # Prepare a vector to store the results, it will be the same length as the matrix has rows.
    result = [0]*rows
    # Count the number of colums in the matrix, it's the same as the length of the vector
    cols = len(v)
    # Matrix multiplication is about summing the item-by-item results of a matrix-row and vector multiplication
    # So initialise the counter to 0     
    sum = 0
    # Now comes the iteration logic. We multiple row for row with the vector, so we first iterate through the matrix' rows
    for row in range(rows):
        # 'row' isn't actually the row, but merely refers to the position of the row, so let's save the actual row.         
        r = m[row]
        # The second step of the iteration logic is to loop through all the items in both the matrix' row and the vector,
        # and to multiple them
        for col in range(cols):
            # with each iteration, the result of m[row][col] and v[col] is added to the sum
            # the sum is 'complete' when all items are iterated through.             
            sum = sum + r[col] * v[col]
        # Now we drop back to the outer loop, and store the result of the inner loop, that is the 'sum' into the right 
        # position in the result vector. The sum is reset to 0 and the next iteration of the outer loop is ready to begin.
        # If this is still cryptic, read up on multiple assignment in python.
        result[row], sum = sum, 0
    # Now that also the outer loop is finished, we can return the full result.
    return result