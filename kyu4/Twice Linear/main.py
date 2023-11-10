def dbl_linear(n):
    sequence = [1]  
    i, j = 0, 0  

    while len(sequence) <= n:
        y = 2 * sequence[i] + 1
        z = 3 * sequence[j] + 1

        if y < z:
            sequence.append(y)
            i += 1
        elif y > z:
            sequence.append(z)
            j += 1
        else:
            sequence.append(y)
            i += 1
            j += 1

    return sequence[n]