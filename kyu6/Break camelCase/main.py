def solution(s):
    result = ""
    for char in s:
        if char.isupper() and result != "":
            result += " " + char
        else:
            result += char
    return result