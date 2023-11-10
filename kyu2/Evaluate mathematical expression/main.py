def calc(expression):
    
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

                elif operator == '--':
                    result = abs(prev + next_num)

                elif operator == '*-':
                    result = -(prev * next_num)

                elif operator == '/-':
                    if next_num == 0:
                        raise ZeroDivisionError("Division by zero")
                    result = -(prev / next_num)

                tokens[i - 1:i + 2] = [str(result)]

                i = 0
                continue
            if tokens[i] in ("+", "-", "*", "/"):

                next_num = float(tokens[i + 1])
                operator = tokens[i]    
                prev = float(tokens[i - 1])


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
    def split_expression(expression):
        parts = []  # List to store the parts of the expression
        stack = []  # Stack to handle parentheses

        for char in expression:
            if char == '(':  # If we encounter an opening parenthesis
                stack.append(parts)  # Push the current 'parts' list onto the stack
                parts = []  # Start a new 'parts' list
            elif char == ')':  # If we encounter a closing parenthesis
                current_part = parts  # Save the current 'parts' list
                parts = stack.pop()  # Pop the previous 'parts' list from the stack
                parts.append(current_part)  # Add the saved 'current_part' to the current 'parts'
            else:
                parts.append(char)  # If it's not a parenthesis, add the character to the current 'parts'

        return parts  # Return the list of parts after processing the expression


    # expression = '(56+(9+5)-(1+(2-(34)))'
    # result = split_expression(expression)
    # print(result)  # Output: ['56', '+', ['9', '+', '5'], '-', ['1', '+', ['2', '-', ['34']]]]

    def merge_numbers(expression):
        merged_expression = []
        current_number = ""

        for item in expression:
            if isinstance(item, list):
                merged_expression.append(merge_numbers(item))
            else:
                if item.isdigit():
                    current_number += item
                else:
                    if current_number:
                        merged_expression.append(current_number)
                        current_number = ""
                    merged_expression.append(item)

        if current_number:
            merged_expression.append(current_number)

        return merged_expression

    def flatten_single_element_sublists(expression):
        if isinstance(expression, list) and len(expression) == 1:
            return flatten_single_element_sublists(expression[0])
        elif isinstance(expression, list):
            return [flatten_single_element_sublists(elem) for elem in expression]
        else:
            return expression
    def find_deepest(subexpression):
        expression_list = []
        for item in subexpression:
            if isinstance(item, list):
                    find_deepest(item)
                    item = merge_operators(item)

                    evaluate_expression(item)
                    subexpression = merge_operators(subexpression)
                    for i in range(len(subexpression)):
                        if subexpression[i] == item and subexpression:

                            subexpression[i] = evaluate_expression(item)
                            subexpression = merge_operators(subexpression)
                            if subexpression[0] == '-':
                                subexpression[0:2] = [-abs(float(subexpression[1]))]

                        subexpression = merge_operators(subexpression)

            else:
                pass
        return evaluate_expression(subexpression)
    
    def add_parenthesis(expression):
        return '('+ expression + ')'
    def remove_whitespace(expression):
        return expression.replace(' ', '')
    def merge_operators(expression):
        merged_expression = []
        i = 0
        while i < len(expression):
            if i < len(expression) - 1 and expression[i] in ('*', '/', '-', '+') and expression[i + 1] in ('*', '/', '-', '+'):
                expression[i:i + 2] = [str((expression[i] + expression[i + 1]))]
                i = 0
            else:
                i += 1
        return expression

    return find_deepest(merge_operators(merge_numbers(split_expression(remove_whitespace(expression)))))
print(calc('10- 2- -5'))