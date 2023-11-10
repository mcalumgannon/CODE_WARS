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

# expression = ['5', '6', '+', ['9', '+', '5'], '-', ['1', '+', ['2', '-', ['3', '4']]]]
# merged_result = flatten_single_element_sublists(merge_numbers(split_expression(expression)))
# print(merged_result)  # Output: ['56', '+', ['9', '+', '5'], '-', ['1', '+', ['2', '-', ['34']]]]

