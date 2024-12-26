def plus_one(A):
    for i in reversed(range(len(A))):
        A[i] += 1
        if A[i] == 10:
            A[i] = 0
        if A[i] != 0:
            break
    if A[0] == 0:
        return [1] + A
    return A