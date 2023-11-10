def solve_expression(expression):
    try:
        def apply_operator(operators, values, operator):
            while (operators and operators[-1] in "+-" and
                   operator in "*/" and operators[-1] in "*/"):
                b, a = values.pop(), values.pop()
                op = operators.pop()
                if op == '*':
                    values.append(a * b)
                elif op == '/':
                    if b == 0:
                        raise ZeroDivisionError("Division by zero")
                    values.append(a / b)
                elif op == '+':
                    values.append(a + b)
                elif op == '-':
                    values.append(a - b)

        operators = []
        values = []
        i = 0

        while i < len(expression):
            if expression[i].isdigit() or (expression[i] == '-' and (i == 0 or expression[i - 1] in "+-*/")):
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] in "+-*/"):
                    j += 1
                token = expression[i:j]
                if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                    values.append(int(token))
                elif token in "+-*/":
                    apply_operator(operators, values, token)
                    operators.append(token)
                else:
                    raise ValueError("Invalid token: " + token)
                i = j
            else:
                raise ValueError("Invalid character: " + expression[i])

        while operators:
            apply_operator(operators, values, operators[-1])

        if len(values) == 1:
            return values[0]
        else:
            raise ValueError("Malformed expression")
    except Exception as e:
        return str(e)

expression = "2+3*4-6"
solved_expression = solve_expression(expression)
print("Solved Expression:", solved_expression)
