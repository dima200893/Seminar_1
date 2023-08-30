class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        return "\n".join(" ".join(str(element) for element in row) for row in self.data)

    def __eq__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            return all(self.data[i][j] == other.data[i][j] for i in range(self.rows) for j in range(self.cols))
        return False

    def __add__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return result
        else:
            raise ValueError("Matrices must have the same dimensions for addition.")

    def __mul__(self, other):
        if isinstance(other, Matrix) and self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            result.data = [
                [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in
                range(self.rows)]
            return result
        else:
            raise ValueError(
                "Number of columns in the first matrix must match the number of rows in the second matrix.")


matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

matrix3 = Matrix(3, 2)
matrix3.data = [[7, 8], [9, 10], [11, 12]]

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

sum_matrix = matrix1 + matrix2
print("Sum of matrices:")
print(sum_matrix)

product_matrix = matrix1 * matrix3
print("Product of matrices:")
print(product_matrix)