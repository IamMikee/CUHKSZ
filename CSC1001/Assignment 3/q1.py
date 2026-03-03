from typing import List
Matrix = List[List[float]]  # Define Matrix


class Matrix3x3:
    """
    A class representing a 3×3 matrix with basic arithmetic operations.

    Attributes
    ----------
    matrix : List[List[float]]
        A 3×3 matrix stored as a list of three lists, each containing three floats.
    """

    def __init__(self,) -> None:
        """
        Initialize the matrix class.
        """
        # self.matrix = Matrix
        self.matrix = [[0,0,0],[0,0,0],[0,0,0]]


    def add(self, a: Matrix, b: Matrix) -> Matrix:
        """
        Add two 3×3 matrices element-wise.
        Parameters
        ----------
        a : Matrix
            A 3×3 matrix represented as a list of three lists of floats.
        b : Matrix
            Another 3×3 matrix.
        Returns
        -------
        Matrix
            A new 3×3 matrix representing element-wise sum of a and b.
        """
        # TODO: Implement matrix addition
        for i in range(3):
            for j in range(3):
                self.matrix[i][j] = a[i][j] + b[i][j]
        return self.matrix


    def subtract(self, a: Matrix, b: Matrix) -> Matrix:
        """
        Subtract one 3×3 matrix from another (a - b).
        Parameters
        ----------
        a : Matrix
        b : Matrix

        Returns
        -------
        Matrix
            A new 3×3 matrix representing (a - b).
        """
        # TODO: Implement matrix subtraction
        for i in range(3):
            for j in range(3):
                self.matrix[i][j] = a[i][j] - b[i][j]
        return self.matrix


    def multiply(self, a: Matrix, b: Matrix) -> Matrix:
        """
        Multiply two 3×3 matrices using standard matrix multiplication.
        Parameters
        ----------
        a : Matrix
        b : Matrix

        Returns
        -------
        Matrix
            The resulting 3×3 matrix product.
        """
        # TODO: Implement matrix multiplication
        for i in range(3):
            for j in range(3):
                sumRow = 0
                for k in range(3):
                    sumRow += a[i][k] * b[k][j]
                self.matrix[i][j] = sumRow
        return self.matrix


    def transpose(self, a: Matrix) -> Matrix:
        """
        Compute the transpose of a 3×3 matrix.

        Parameters
        ----------
        a : Matrix

        Returns
        -------
        Matrix
            The 3×3 transpose of matrix a.
        """
        # TODO: implement matrix transpose
        for i in range(3):
            for j in range(3):
                self.matrix[i][j] = a[j][i]
        return self.matrix