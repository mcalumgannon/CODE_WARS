from solve_mini_expression import evaluate_expression
from split_string_into_list import flatten_single_element_sublists, merge_numbers, split_expression
from solve_subexpressions_as_nested_lists import find_deepest

expression = '56 + (9 + 5) - 1 + (2 -(34 + 8))'
expression_in_list = flatten_single_element_sublists(merge_numbers(split_expression(expression)))
print(expression_in_list)
print(find_deepest(expression_in_list))
