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
