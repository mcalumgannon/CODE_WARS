def balanced_parens(n):
    def generate_parentheses(partial, left, right):
        if len(partial) == 2 * n:
            result.append(partial)
            return
        if left < n:
            generate_parentheses(partial + '(', left + 1, right)
        if right < left:
            generate_parentheses(partial + ')', left, right + 1)

    result = []
    generate_parentheses("", 0, 0)
    return result
