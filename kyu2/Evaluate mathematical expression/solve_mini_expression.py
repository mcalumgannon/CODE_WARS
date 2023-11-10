
def solve_mini_expression(tokens):
    i = 0
    while i < len(tokens):
        if i == 0 and tokens[0] == '-':
            tokens[0:2] = [-abs(int(tokens[1]))]
        if tokens[i] in ('+-', '--', '*-', '/-'):
            prev = float(tokens[i - 1])
            next_num = float(tokens[i + 1])
            operator = tokens[i]
            if operator == '+-':
                result = (prev - next_num)
                print(result)
            elif operator == '--':
                result = abs(prev + next_num)
                print(result)
            elif operator == '*-':
                result = -(prev * next_num)
                print(result)
            elif operator == '/-':
                if next_num == 0:
                    raise ZeroDivisionError("Division by zero")
                result = -(prev / next_num)
                print(result)
            tokens[i - 1:i + 2] = [str(result)]
            print(tokens)
            i = 0
            continue
        if tokens[i] in ("+", "-", "*", "/"):

            next_num = float(tokens[i + 1])
            operator = tokens[i]    
            prev = float(tokens[i - 1])

            print(operator)
            if operator == '+':
                result = prev + next_num
            elif operator == '-':
                result = prev - next_num
            elif operator == '*':
                result = prev * next_num
            elif operator == '/':
                if next_num == 0:
                    raise ZeroDivisionError("Division by zero")
                result = prev / next_num
            # Replace the mini expression with the result
            tokens[i - 1:i + 2] = [str(result)]
            i = 0
        else:
            i += 1

def evaluate_expression(expression):
    solve_mini_expression(expression)
    return float(expression[0])

    



# expression = ['2', '+-', '2']
# solved_expression = evaluate_expression(expression)
# print("Solved Expression:", solved_expression)
