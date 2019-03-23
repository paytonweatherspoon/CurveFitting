def matrixDim(matrix):
    rowCount = 0
    columnCount = 0
    for i in matrix:
        rowCount += 1
    for j in matrix[0]:
        columnCount += 1
    return (rowCount, columnCount)


def matrixScalar(matrix, scalar):
    for i in matrix:
        for a in range(len(i)):
            i[a] = float(i[a]) * scalar

    return matrix

# wrote this because could not use matrix scalar on a single row


def rowScalar(row, scalar):

    returnRow = []

    for i in range(len(row)):

        returnRow.append(float(row[i]) * scalar)

    return returnRow

# for vectors


def rowSubtract(row, row2):

    for i in range(len(row)):

        row[i] = float(row[i]) - float(row2[i])

    return(row)


def rowAddition(row, row2):
    for i in range(len(row)):

        row[i] = float(row[i]) - float(row2[i])

    return(row)


# matricies must have the same dimensions for this operation
def matrixAddition(mat1, mat2):
    returnMat = []

    for i in range(len(mat1)):  # since they are the same size you can do this with either matrix
        row = []
        for j in range(len(mat1[i])):

            value = float(mat1[i][j]) + float(mat2[i][j])
            row.append(value)

        returnMat.append(row)

    return(returnMat)


def matrixSubtraction(mat1, mat2):
    returnMat = []

    for i in range(len(mat1)):  # since they are the same size you can do this with either matrix
        row = []
        for j in range(len(mat1[i])):

            value = float(mat1[i][j]) - float(mat2[i][j])
            row.append(value)
        returnMat.append(row)

    return (returnMat)


# they need to be conformable for this operation to work
def matrixMult(mat1, mat2):

    if matrixDim(mat1)[1] == matrixDim(mat2)[0]:

        returnMat = []

        for i in range(len(mat1)):
            newrow = []
            for j in range(len(mat2[0])):
                sum = 0
                for k in range(len(mat1[i])):
                    sum += float(mat1[i][k]) * float(mat2[k][j])
                newrow.append(sum)  # add the value to the row

            returnMat.append(newrow)

        return (returnMat)

    else:
        print('invalid. matrices are not conformable')


def rowSwap(matrix, orgRow, newRow):

    copyRow = matrix[newRow]

    matrix[newRow] = matrix[orgRow]

    matrix[orgRow] = copyRow

    return (matrix)


def inverseMatrix(matrix):

    n = matrixDim(matrix)

    for j in range(len(matrix)):

        largestRowInd = 0
        largestValue = 0

        for p in range(j, n[0]):

            if abs(float(matrix[p][j])) > abs(largestValue):
                largestValue = float(matrix[p][j])
                largestRowInd = p

        if largestValue == 0:
            print("Escape loop")
            break

        rowSwap(matrix, j, largestRowInd)

        firstValue = float(matrix[j][j])

        for i in range(n[1]):
            matrix[j][i] = float(matrix[j][i]) / firstValue

        for p in range(len(matrix)):

            if p != j:

                scalarValue = float(matrix[p][j])

                if scalarValue > 0:

                    elimRow = rowScalar(matrix[j], scalarValue)

                    rowSubtract(matrix[p], elimRow)

                else:

                    elimRow = rowScalar(matrix[j], scalarValue)

                    rowAddition(matrix[p], elimRow)

    return (matrix)


def augmentCoefMat(mat, mat2):

    augmentedMat = []

    for i in range(len(mat)):
        row = []
        for j in range(len(mat[i])):
            row.append(mat[i][j])

        for j in range(len(mat2[i])):
            row.append(mat2[i][j])

        augmentedMat.append(row)

    return augmentedMat


def createIdentity(size):

    idMat = []
    for i in range(size):

        row = []
        # creates each row as big as it needs to be fill of 0s
        while len(row) != size:
            row.append(0)
        # replaces the necessary spot with a 1
        row[i] = 1

        idMat.append(row)

    return idMat


def fixAugMat(matrix, columns):

    for i in range(len(matrix)):

        matrix[i] = matrix[i][columns:]

    return matrix


points = [[-1, -11], [0, -5], [1, -5], [2, 1]]


def weierstrass(data):

    n = len(data)

    matrix = []

    for i in range(len(data)):
        row = []
        n = len(data)
        for j in range(len(data)):

            row.append(data[i][0]**(n-1))
            n -= 1
        matrix.append(row)

    weiridmat = createIdentity(matrixDim(matrix)[0])
    weirmat = augmentCoefMat(matrix, weiridmat)

    invweir = inverseMatrix(weirmat)

    invweir = fixAugMat(invweir, matrixDim(weirmat)[0])

    y = []

    for i in range(len(data)):
        y.append([data[i][1]])

    solution = matrixMult(invweir, y)

    return(solution)


print(weierstrass(points))

linear = [[2,3],[3,5],[4,7]]

print(weierstrass(linear))
