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