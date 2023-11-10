from solve_mini_expression import evaluate_expression
from split_string_into_list import flatten_single_element_sublists, merge_numbers, split_expression

def find_deepest(subexpression):
    expression_list = []
    for item in subexpression:
        if isinstance(item, list):
                find_deepest(item)
                item = merge_operators(item)
                print(item)
                evaluate_expression(item)
                print('doing')
                subexpression = merge_operators(subexpression)
                for i in range(len(subexpression)):
                    if subexpression[i] == item and subexpression:
                        print(item)
                        print('item above this')
                        subexpression[i] = evaluate_expression(item)
                        subexpression = merge_operators(subexpression)
                        if subexpression[0] == '-':
                            subexpression[0:2] = [-abs(float(subexpression[1]))]
                        print(subexpression)
                    subexpression = merge_operators(subexpression)
                    print(subexpression)
        else:
            print('no more found')
    return evaluate_expression(subexpression)

expression = '10- 2- -5'
def add_parenthesis(expression):
     return '('+ expression + ')'
def remove_whitespace(expression):
     return expression.replace(' ', '')
def merge_operators(expression):
    merged_expression = []
    i = 0
    while i < len(expression):
        if i < len(expression) - 1 and expression[i] in ('*', '/', '-', '+') and expression[i + 1] in ('*', '/', '-', '+'):
            print('yea')
            expression[i:i + 2] = [str((expression[i] + expression[i + 1]))]
            i = 0
        else:
            print('nah')
            i += 1
    return expression
     
     
print(add_parenthesis(remove_whitespace(expression)))
print(split_expression(add_parenthesis(remove_whitespace(expression))))
print(merge_numbers(split_expression(add_parenthesis(remove_whitespace(expression)))))
print(find_deepest(merge_operators(merge_numbers(split_expression(remove_whitespace(expression))))))










