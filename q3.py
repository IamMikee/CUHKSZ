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


#### Q2
def evaluate_expression(expression: str) -> int:
    """
    Evaluate a mathematical expression containing integers, +, -, and parentheses.
    Parameters
    ----------
    expression : str
        A non-empty mathematical expression.
        Allowed:
        - Non-negative integers
        - '+' and '-' operators
        - Parentheses for grouping
        - Optional spaces

    Returns
    -------
    int
        The evaluated integer result
    Notes
    -----
    - Operator precedence: parentheses > left-to-right evaluation
    - No multiplication or division
    """
    # TODO: Implement expression evaluator using stack or recursion
    def recursion(pos):
        total = 0
        num = 0
        sign = 1

        while pos < len(expression):
            char = expression[pos]
            if char.isdigit():
                num = num*10 + int(char) #to update the num value as int (*10 to indicate tenths,hundreds,etc.)
            elif char == "+":
                total += num * sign
                num = 0
                sign = 1
            elif char == "-":
                total += num * sign
                num = 0
                sign = -1
            elif char == "(":
                num, pos = recursion(pos+1)
            elif char == ")":
                return total + sign*num, pos

            pos += 1
        return total + sign*num
    return recursion(0)



def quick_sort(arr: List[int]) -> List[int]:
    """
    Perform quick-sort on a list of integers while tracking all comparisons.
    Parameters
    ----------
    arr : List[int]
        The input list.
    Returns
    -------
    sorted_arr : List[int]
        Sorted version of arr.
    """
    # TODO: implement quick-sort with:
    #   - partitioning
    #   - recursive sorting
    #   - tracking (count, sequence)




if __name__ == '__main__':
    print("--- Test it yourself ---")

    print("=== Q1 Testing ===")
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    sol1 = Matrix3x3()
    q1_add = [[10, 10, 10, ],
               [10, 10, 10, ],
               [10, 10, 10, ]]
    q1_sub = [[-8, -6, -4, ],
               [-2, 0, 2, ],
               [4, 6, 8, ]]
    q1_mul = [[30, 24, 18, ],
               [84, 69, 54, ],
               [138, 114, 90, ]]

    # Matrix A transpose
    q1_trans = [[1, 4, 7, ],
                 [2, 5, 8, ],
                 [3, 6, 9, ]]
    # print(f"Q1 Answer is: matrix add: {q1_add == sol1.add(A, B)}\n"
    #       f"              matrix subtract: {q1_sub == sol1.subtract(A, B)}\n"
    #       f"              matrix multiply:{q1_mul == sol1.multiply(A, B)}\n"
    #       f"              matrix transpose: {q1_trans == sol1.transpose(A)}\n")




    print("=== Q2 Testing ===")
    expressions = "(1-(2-(3))) + 4"
    q2_ans = evaluate_expression(expressions)
    # print(f"Q2 Answer is {q2_ans}")
    # print(f"Q2 Answer is {q2_ans == 6}")
    #
    #
    # print("=== Q3 Testing ===")
    # arr = [5, 3, 8, 4, 2, 7]
    # q3_ans = quick_sort(arr)
    # ans = [2, 3, 4, 5, 7, 8]
    # print(f"Q3 Answer is {q3_ans == ans}")